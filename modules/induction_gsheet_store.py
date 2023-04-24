import datetime
import logging
from typing import TypedDict, Dict

import gspread
from discord import User, Member
from oauth2client.service_account import ServiceAccountCredentials

from modules.induction import Induction, State
from modules.tool import Tool


def next_available_row(worksheet) -> int:
    str_list = list(filter(None, worksheet.col_values(1)))
    return len(str_list) + 1


class InductionGsheetStore:
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
    client = gspread.authorize(credentials)
    db = client.open("InductionDatabase")

    def create(self, thread_id: int, tool: Tool, requestor: Member):

        sheet = self.db.sheet1
        # db.share('dave.lush@gmail.com', perm_type='user', role='writer')
        row_num = next_available_row(sheet)
        row_data = [thread_id, requestor.id, requestor.display_name, "", "", State.NEW.value, tool.value,
                    datetime.datetime.now().isoformat(), "", ""]
        sheet.insert_row(row_data, row_num)
        logging.info(f"CREATED by {requestor.display_name} for {tool} in {thread_id}")

    def claim(self, thread_id: int, claimer: Member):

        if thread_id in self.store:
            self.store[thread_id].claim(claimer)
            logging.info(f"CLAIMED by {claimer.display_name} in {thread_id}")
        else:
            logging.error(f"thread {thread_id} does not exist to be claimed by {claimer.display_name}")

    def get(self, thread_id) -> Induction:
        if thread_id in self.store:
            return self.store.get(thread_id)
        else:
            return None

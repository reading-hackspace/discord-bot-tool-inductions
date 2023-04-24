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
        row_data = [str(thread_id), str(requestor.id), requestor.display_name, " ", " ", State.NEW.value, tool.value,
                    datetime.datetime.now().isoformat(), " ", " "]
        sheet.insert_row(row_data, row_num)
        logging.info(f"CREATED by {requestor.display_name} for {tool} in {thread_id}")

    def claim(self, thread_id: int, claimer: Member):
        thread_id_str = str(thread_id)
        sheet = self.db.sheet1
        thread_id_list = sheet.col_values(1)
        # ValueRenderOption
        if thread_id_str in thread_id_list:
            row_num = thread_id_list.index(thread_id_str) + 1
            cells = sheet.get(f"A{row_num}:J{row_num}")
            cells[0][3] = str(claimer.id)
            cells[0][4] = claimer.display_name
            if len(cells[0]) <= 7:
                 list(cells[0]).append(datetime.datetime.now().isoformat())
            else:
                cells[0][8] = datetime.datetime.now().isoformat()
            sheet.update(f"A{row_num}:J{row_num}", cells)
            logging.info(f"CLAIMED by {claimer.display_name} in {thread_id_str}")
        else:
            logging.error(f"thread {thread_id} does not exist to be claimed by {claimer.display_name}")

    def get(self, thread_id:int) -> Induction:
        thread_id_str = str(thread_id)
        sheet = self.db.sheet1
        thread_id_list = sheet.col_values(1)
        if thread_id_str in thread_id_list:
            row_num = thread_id_list.index(thread_id_str) + 1
            cells = sheet.get(f"A{row_num}:J{row_num}")
            return Induction(cells[0])
        else:
            return None

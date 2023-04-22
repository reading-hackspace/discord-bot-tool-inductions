import logging
from typing import TypedDict, Dict

from discord import User, Member

from modules.induction import Induction
from modules.tool import Tool


class InductionStore:
    store: dict[str, Induction] = {}

    def create_induction(self, thread_id: str, tool: Tool, requestor: Member):
        self.store[thread_id] = Induction(tool, requestor)
        logging.info(f"CREATED by {requestor.display_name} for {tool} in {thread_id}")

    def claim_induction(self, thread_id: str, claimer: Member):
        if thread_id in self.store:
            self.store[thread_id].claim(claimer)
            logging.info(f"CLAIMED by {claimer.display_name} in {thread_id}")
        else:
            logging.error(f"thread {thread_id} does not exist to be claimed by {claimer.display_name}")

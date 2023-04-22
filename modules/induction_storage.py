import logging
from typing import TypedDict, Dict

from discord import User

from modules.induction import Induction
from modules.tool import Tool


class InductionStore:
    store: dict[str, Induction] = {}

    def create_induction(self, thread_id: str, tool: Tool, requestor: User):
        self.store[thread_id] = Induction(tool, requestor)

    def claim_induction(self, thread_id: str, claimer: User):
        if thread_id in self.store:
            self.store[thread_id].claim(claimer)
        else:
            logging.error(f"thread {thread_id} does not exist to be claimed by {claimer.display_name}")

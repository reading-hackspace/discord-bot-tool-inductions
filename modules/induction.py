from datetime import datetime
from enum import Enum
from modules.tool import Tool


class State(Enum):
    NEW = 1
    CLAIMED = 2
    DONE = 3
    CANCELLED = 4


class Induction:
    requestor_id: str
    requestor_name: str
    claimer_id: str
    claimer_name: str
    state: State
    tool: Tool
    request_datetime: datetime
    claim_datetime: datetime
    close_datetime: datetime

    def __init__(self,  state: State, tool: Tool, requestor_id: str, requestor_name: str, claimer_id: str, claimer_name: str):
        self.tool = tool
        self.state = state
        self.requestor_id = requestor_id
        self.requestor_name = requestor_name
        self.claimer_id = claimer_id
        self.claimer_name = claimer_name

    def __init__(self, row: list):
        self.requestor_id = row[1]
        self.requestor_name = row[2]
        self.claimer_id = row[3]
        self.claimer_name = row[4]
        self.status = row[5]
        self.tool = row[6]

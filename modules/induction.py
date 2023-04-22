from enum import Enum
from discord.user import User

from modules.tool import Tool


class State(Enum):
    NEW = 1
    CLAIMED = 2
    DONE = 3
    CANCELLED = 4


class Induction:
    requestor: User
    claimer: User
    state: State
    tool: Tool

    def __init__(self, tool:Tool, user:User):
        self.tool = tool
        self.requestor = user
        state = State.NEW

    def claim(self, user: User):
        self.claimer = User
        self.state = State.CLAIMED



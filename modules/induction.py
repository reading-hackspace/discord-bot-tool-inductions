from enum import Enum

from discord import Member
from discord.user import User

from modules.tool import Tool


class State(Enum):
    NEW = 1
    CLAIMED = 2
    DONE = 3
    CANCELLED = 4


class Induction:
    requestor: Member
    claimer: Member
    state: State
    tool: Tool

    def __init__(self, tool:Tool, user:Member):
        self.tool = tool
        self.requestor = user
        state = State.NEW

    def claim(self, user: Member):
        self.claimer = User
        self.state = State.CLAIMED



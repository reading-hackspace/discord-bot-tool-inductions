from enum import Enum
from discord.user import User


class State(Enum):
    NEW = 1
    CLAIMED = 2
    DONE = 3
    CANCELLED = 4


class Induction:
    requestor: User
    claimer: User
    state: State

from typing import TypedDict
from modules.induction import Induction


class InductionStorage(TypedDict):
    induction: Induction

def get_induction()
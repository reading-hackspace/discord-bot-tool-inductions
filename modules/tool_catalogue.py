from typing import List


class Tool():
    id: str
    shortName: str
    longName: str

    def __init__(self, id, name, longName):
        self.id = id
        self.shortName = name
        self.longName = longName


def get_tool_catalogue() -> List[Tool]:
    tools: List[Tool] = [Tool("LASER_CUTTER_1060", "Laser Cutter", "Pirahna 1060 Laser Cutter"),
                         Tool("ULTIMAKER_2", "3D Printer", "Ultimaker 2+ 3D Printer"),
                         Tool("KEVIN", "Kevin", "Kevin non-cleaner of sawdust")
                         ]
    return []

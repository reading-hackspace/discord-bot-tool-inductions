from typing import List


class Tool():
    id: str
    shortName: str
    longName: str
    induction_required: bool = True

    def __init__(self, id, name, longName):
        self.id = id
        self.shortName = name
        self.longName = longName


def get_tool_catalogue() -> List[Tool]:
    tools: List[Tool] = [Tool("LASER_CUTTER_1060", "Laser Cutter", "Pirahna 1060 Laser Cutter", True),
                         Tool("ULTIMAKER_2", "3D Printer", "Ultimaker 2+ 3D Printer", True),
                         Tool("VINYL_CUTTER", "Vinyl Cutter (ROBO)", "Graphtec Craft ROBO Vinyl Cutter", False),
                         Tool("SMALL_SEWING_MACHINE", "Small Sewing Machine", "Small Sewing Machine", False),
                         Tool("VACUUM_FORMER", "Vacuum Former", "Mayku Formbox Vacuum Former", False),
                         Tool("MICROSCOPE", "Inspection Microscope", "SZM7045TR Binocular Inspection Microscope", False),
                         Tool("HARDNESS_TESTER", "Hardness Tester", "Instron DynaTestor 10 Ultrasonic Hardness Tester", False),
                         Tool("A3_LASER_PRINTER", "Laser Printer", "Xerox C7000DN Printer", False),
                         Tool("KEVIN", "Kevin", "Kevin non-cleaner of sawdust", True),
                         Tool("PROJECTOR", "Projector", "Mitsubishi HC1100 DLP Video Projector", False),
                         Tool("DESIGN_STATION_1", "Design Station 1", "Design Station 1", False),
                         Tool("DESIGN_STATION_2", "Design Station 2", "Design Station 2", False),
                         Tool("VINYL_CUTTER_2", "Vinyl Cutter (Cameo 4)", "Silhouette Cameo 4 Vinyl Cutter", False),
                         Tool("LARGE_SEWING_MACHINE", "Large Sewing Machine", "Large Sewing Machine", False),
                         Tool("AIRBRUSH", "Airbrush", "Miniature Airbrush", False),
                         Tool("METAL_LATHE", "Metal Lathe", "Harrison M300 Light-industrial Metal Lathe", True),
                         Tool("PLASMA_CUTTER", "Plasma Cutter", "CUT-50 Plasma cutter", True),
                         Tool("MIG_WELDER", "MIG Welder", "ESAB Rebel EMP235ic MIG Welder", True),
                         Tool("TIG_WELDER", "TIG Welder", "ThermalArc 202AC/DC TIG Welder", True),
                         Tool("WOOD_LATHE", "Wood Lathe", "Record Power Coronet Herald Lathe", True),
                         Tool("CHEMICALS", "Chemical Storage", "Chemical Storage", False),
                         Tool("BANDSAW", "Bandsaw", "Jet VBS-18MW Bandsaw", True),
                         Tool("PEDESTAL_GRINDER", "Pedestal Grinder", "Viceroy TDS Pedestal Grinder", False),
                         Tool("MORTICER", "Morticer", "DK2096 Morticer", False),
                         Tool("AIR_COMPRESSOR", "Air Compressor", "Wolf Dakota 100 Air Compressor", False),
                         Tool("CNC_MILL", "CNC Mill", "Boxford 260 VMC CNC Milling Machine", True),
                         Tool("CRUCIBLE_FURNACE", "Crucible Furnace", "CM450PB Safety Tilt Crucible Furnace", True),
                         Tool("FORGE", "Forge", "Propane Tunnel Forge", True),
                         Tool("INDUCTION_HEATER", "Induction Heater", "EVE Induction Heater", False),
                         Tool("AIR_CLEANER", "Air Cleaner", "Laguna A12 Air cleaner", False),
                         Tool("METAL_CHOP_SAW", "Metal Chop Saw", "DeWalt DW872 Metal Chop Saw", True),
                         Tool("MITRE_SAW", "Mitre Saw", "SIP Sliding Mitre Saw", True),
                         Tool("LARGE_LINISHER", "Large Linisher", "Clarke CS6-9C Belt Linisher", False),
                         Tool("SMALL_LINISHER", "Small Linisher", "Scheppach 490 Belt Linisher", False),
                         Tool("ROUTER_TABLE", "Router Table", "Router Table", True),
                         Tool("TABLE_SAW", "Table Saw", "Record Power TS250-C Table Saw", True),
                         Tool("PLANNER_THICKNESSER", "Planner Thicknesser", "Axminster AT260SPT Planer-Thicknesser", True),
                         Tool("OVEN", "Oven", "R302-A Materials Testing Oven", False),
                         Tool("DRILL_PRESS", "Drill Press", "Nu-Way CF25 Drill press", False),
                         Tool("SCROLL_SAW", "Scroll Saw", "Record Power SS16V Scroll Saw", False),
                         Tool("MINI_MILL", "Mini Mill", "Chester Cobra Mini Mill", False),
                         Tool("BLASTING_CABINET", "Blasting Cabinet", "PowerKing SBC1 Blasting Cabinet", False),
                         Tool("FUME_HOOD", "Fume Hood", "Fume Hood", False),
                         Tool("CLEANING_BATH", "Ultrasound Cleaning Bath", "Kemet Gem-25D Ultrasound Cleaning Bath", False),
                         Tool("HORIZONTAL_BANDSAW", "Horizontal Bandsaw", "HV-128 Horizontal Bandsaw", False),
                         Tool("POLISHING_WHEEL", "Polishing Wheel", "8\" Polishing and Buffing Wheel", False),
                         Tool("INSPECTION_MICROSCOPE", "Tool Inspection Microscope", "Tool Inspection Microscope", False),
                         Tool("GRINDER", "Grinder", "Axminster AP200SRG Grinder", False)
                         ]
    return []

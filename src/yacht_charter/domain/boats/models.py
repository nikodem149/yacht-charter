from dataclasses import dataclass

from src.yacht_charter.enums import SailBoatStatus


@dataclass
class Sailboat:
    boat_id: int
    name: str
    boat_type: str
    length: float
    price: float
    status: SailBoatStatus = SailBoatStatus.AVAILABLE
    charter_dates = []







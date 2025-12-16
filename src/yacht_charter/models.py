from dataclasses import dataclass
from datetime import date

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

@dataclass
class Charter:
    start_date: date
    end_date: date
    boat_id: int

    def is_overlapping(self, other_start: date, other_end: date) -> bool:
        return not (self.end_date < other_start or self.start_date > other_end)





from ..enums import SailBoatStatus, can_change_status
from ..models import Sailboat
#add boat
# remove boat
# list boats
# set boat status
# get boat

class BoatStorage:
    def __init__(self):
        # Słownik zamiast bazy danych. Normalnie konektor do bazy danych
        self.boats: dict[int, Sailboat] = {}

    def add_boat(self, boat_id: int, type_of_boat: str, name: str, boat_type: str, length: float, price: float) -> Sailboat:
        if boat_id in self.boats:
            raise ValueError("Boat already in storage.")
        new_boat = Sailboat(boat_id, type_of_boat, name, boat_type, length, price)
        self.boats[boat_id] = new_boat
        return new_boat

    def remove_boat(self, boat_id: int) -> bool:
        if boat_id in self.boats:
            del self.boats[boat_id]
            return True
        return False

    def list_boat(self, include_inactive: bool = True) -> list[Sailboat]:
        if include_inactive:
            return list(self.boats.values())

        active_statuses = frozenset({
            SailBoatStatus.AVAILABLE,
            SailBoatStatus.BOOKED,
            SailBoatStatus.IN_USE,
            SailBoatStatus.MAINTENANCE
        })
        return [boat for boat in self.boats.values() if boat.status in active_statuses]

    def set_boat_status(self, boat_id: int, status: SailBoatStatus) -> None:
        boat = self.get_boat(boat_id)
        if not can_change_status(boat.status, status):
            raise ValueError('Unable to change status.')
        boat.status = status

    def get_boat(self, boat_id: int) -> Sailboat | None:
        return self.boats.get(boat_id)

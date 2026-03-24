from ..domain.boats.repository import BoatRepository
from ..enums import SailBoatStatus, can_change_status
from src.yacht_charter.domain.boats.models import Sailboat


class BoatStorage:
    def __init__(self, boat_repository: BoatRepository):
        # Dictionary instead of database connection.
        self.boats: BoatRepository = boat_repository
        # TODO: Replace the dictionary with database connector

    def add_boat(self, boat_id: int, name: str, boat_type: str, length: float,
                 price: float, status: SailBoatStatus | None = None) -> Sailboat:
        if status is None:
            status = SailBoatStatus.AVAILABLE
        if boat_id in self.boats:
            raise ValueError("Boat already in storage.")
        new_boat = Sailboat(boat_id, name, boat_type, length, price, status)
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

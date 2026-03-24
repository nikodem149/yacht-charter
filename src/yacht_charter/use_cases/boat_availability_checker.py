# is boat available
# list available boats
from datetime import date
from .boat_storage import Sailboat
from ..domain.charters.models import Charter
from ..enums import SailBoatStatus

class AvailabilityChecker:

    @staticmethod
    def is_available_term(charters: list[Charter], boat_id: int, start_date: date, end_date: date) -> bool:
        """
        Checks if the boat of given id is available for charter in given dates.
        :param charters:
        :param boat_id:
        :param start_date:
        :param end_date:
        :return:
        """
        for charter in charters:
            if charter.boat_id == boat_id and charter.is_overlapping(start_date, end_date):
                return False
        return True

    @staticmethod
    def is_boat_status_available(boat_id: int, boats: list[Sailboat]) -> bool:
        """
        Checks if status of boat of given id is AVAILABLE.
        :param boats:
        :param boat_id:
        :return:
        """
        for boat in boats:
            if boat.boat_id == boat_id and boat.status == SailBoatStatus.AVAILABLE:
                return True
        return False

    @staticmethod
    def list_available_boats(
        boats: list[Sailboat], charters: list[Charter], start_date: date, end_date: date
    ) -> list[Sailboat]:
        """
        Returns the list of all boats available for charter between given dates.
        :param boats:
        :param charters:
        :param start_date:
        :param end_date:
        :return:
        """
        # można zamiast list comprehension więcej linijek
        # available boats = []
        return [
            boat
            for boat in boats
            if (
                is_available_term(charters, boat.boat_id, start_date, end_date)
                and is_boat_status_available(boat.boat_id, boats)
            )
        ]


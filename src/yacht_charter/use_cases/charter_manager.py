from datetime import date

from .boat_availability_checker import AvailabilityChecker
from ..domain.charters.models import Charter


class CharterManager:
    # TODO: add docstring for CharterManager class
    def __init__(self, availability_checker: AvailabilityChecker):
        self.charters: list[Charter] = []
        self.availability_checker = availability_checker

    def add_charter(self, boat_id: int, start_date: date, end_date: date) -> bool:
        # TODO: Zamiast trzech poniższych linii odwołanie do self.availability_checker
        for charter in self.charters:
            if charter.boat_id == boat_id and charter.is_overlapping(start_date, end_date):
                return False

        self.charters.append(Charter(start_date, end_date, boat_id))
        return True

    def remove_charter(self, boat_id: int, start_date: date, end_date: date) -> bool:
        for charter in self.charters:
            if charter.boat_id == boat_id and charter.start_date == start_date and charter.end_date == end_date:
                self.charters.remove(charter)
                return True
        return False

    def remove_charter_v2(self, **criteria):
        to_remove = []
        for charter in self.charters:
            if all(getattr(charter, field) == value for field, value in criteria.items()):
                to_remove.append(charter)

        for charter in to_remove:
            self.charters.remove(charter)

    def list_charters(self, boat_ids: list[int] = None) -> list[Charter]:
        """
        Return the list of all charters for all boats of given ids.
        :param boat_ids:
        :return:
        """
        # Test what if boat_ids is empty list or None
        return [charter for charter in self.charters if charter.boat_id in boat_ids]



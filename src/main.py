from datetime import date, datetime

from src.yacht_charter.domain.boats.models import Sailboat
from src.yacht_charter.domain.charters.schemas import CharterRequest

# last day for which charter is currently available
END_DATE = date(2026, 9, 30)

SAILBOATS = [
    Sailboat(0, "Sunset", "catamaran", 37, 7330.0),
    Sailboat(1, "Sea Lion", "monohull", 46, 2700.0)
]

charters = [{"boat_id": 0,
             "start_date": date(2025, 6, 1),
             "end_date": date(2025, 6, 14)}]


def select_term():
    charter_request = CharterRequest(start_date=date(2025, 9, 3),
                                     end_date=date(2025, 9, 10))
    print(charter_request)


def show_boats() -> None:
    print(get_available_boats(date(2025, 5, 7), date(2025, 9, 12)))


def get_available_boats(start_date: date, end_date: date) -> list[Sailboat]:
    return [boat for boat in SAILBOATS if is_available(boat.boat_id, start_date, end_date)]


def is_available(boat_id: int, requested_start: date, requested_end: date) -> bool:
    for charter in charters:
        if charter["boat_id"] == boat_id:
            if not (requested_end < charter["start_date"] or requested_start > charter["end_date"]):
                return False
    return True


def select_boat(start_date: datetime = None, end_date: datetime = None):
    """
    Select from list of available boats with price.
    :return:
    """
    # for each boat take every charter dates and check if they overlap with start_date, end_date



def book_a_boat():
    """
    Make a boat unavailable until user finally decides to rent it.
    Display info about it.
    :return:
    """


def add_additional_equipment():
    """

    :return:
    """


def display_charter_summary():
    """
    Display total price and info about the boat.
    Display additional costs.
    :return:
    """


def charter_approval():
    """

    :return:
    """

def main() -> None:
    """
    Aplikacja, która obsługuje czarter jachtów.
    Potrzebujemy mieć termin i jacht.
    :return:
    """
    select_term()
    # show_boats()
    # select_boat()
    # book_a_boat()
    # add_additional_equipment()
    # display_charter_summary()
    # charter_approval()


if __name__ == "__main__":
    main()

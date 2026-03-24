# from ..src.yacht_charter.main import *

# Tak najlepiej

# albo tak


# # from unittest import TestCase
# from datetime import date
#
# import pytest
# from pydantic import ValidationError
#
# from yacht_charter.main import Sailboat, CharterRequest
# from yacht_charter.main import show_boats, get_available_boats
# from yacht_charter.main import main
#
#
# class TestCharter(TestCase):
#     def test_get_available_boats(self):
#         available_boats = get_available_boats(date(2025, 7, 1), date(2025, 7, 14))
#         self.assertEqual(available_boats, [
#             Sailboat(0, "Sunset", "catamaran", 37, 7330.0),
#             Sailboat(1, "Sea Lion", "monohull", 46, 2600.0)
#         ])
#
# def test_get_available_boats():
#     available_boats = get_available_boats(date(2025, 7, 1), date(2025, 7, 14))
#     assert available_boats == [
#         Sailboat(0, "Sunset", "catamaran", 37, 7330.0),
#         Sailboat(1, "Sea Lion", "monohull", 46, 2700.0)
#     ]
#
# def test_main():
#     assert main() == None
#
# def test_charter_request_dates():
#     with pytest.raises(ValueError) as error:
#         chart_req = CharterRequest(start_date=date(2025,8,15), end_date=date(2025,8,1))
#     # Komunikat do błędu
#     print(error.value)
#     assert False
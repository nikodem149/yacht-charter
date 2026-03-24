from unittest import TestCase

from src.yacht_charter.enums import SailBoatStatus
from src.yacht_charter.use_cases.boat_storage import BoatStorage


class TestBoatStorage(TestCase):
    # Za konstrukcję obiektu odpowiada __new__ a __init__ za przypisanie atrybutów
    # Dopiero obie metody razem to konstruktor

    # Metoda, która przygotowuje testy
    def setUp(self):
        self.store = BoatStorage()

    def test_add_new_boat(self):
        new_boat = self.store.add_boat(1, "name", "type", 10.0, 100)
        self.assertEqual(new_boat.boat_id, 1)
        self.assertEqual(new_boat.name, "name")
        self.assertEqual(new_boat.boat_type, "type")
        self.assertEqual(new_boat.length, 10.0)
        self.assertEqual(new_boat.price, 100)

    def test_add_existing_id_should_fail(self):
        self.store.add_boat(1, "name", "type", 10.0, 100)
        with self.assertRaises(ValueError):
            self.store.add_boat(1, "name", "type", 10.0, 100)

    def test_remove_existing_boat(self):
        self.store.add_boat(1, "name", "type", 10.0, 100)
        ok = self.store.remove_boat(1)
        self.assertTrue(ok)
        self.assertEqual(len(self.store.list_boat()), 0)

    def test_remove_non_existing_boat(self):
        ok = self.store.remove_boat(1)
        self.assertFalse(ok)

    def test_list_include_inactive(self):
        self.store.add_boat(1, "name", "type", 10.0, 100)
        self.store.add_boat(2, "name2", "type2", 10.0, 100, SailBoatStatus.INACTIVE)
        boats = self.store.list_boat(include_inactive=True)
        self.assertEqual(len(boats), 2)

    def test_list_only_active(self):
        self.store.add_boat(1, "name", "type", 10.0, 100)
        self.store.add_boat(2, "name2", "type2", 10.0, 100, SailBoatStatus.INACTIVE)
        boats = self.store.list_boat(include_inactive=False)
        self.assertEqual(len(boats), 1)
        self.assertEqual(boats[0].name, "name")

    def test_get_boat(self):
        boat = self.store.add_boat(1, "name", "type", 10.0, 100)
        found_boat = self.store.get_boat(1)
        self.assertIs(boat, found_boat)

    def test_get_boat_returns_none_if_missing(self):
        self.assertIsNone(self.store.get_boat(1))

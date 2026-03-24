# schema i models powinny być na poziomie repository

from src.yacht_charter.domain.boats.models import Sailboat
import sqlite3


# problem z charter_dates

class BoatRepository(dict):
    def __init__(self, db_path: str):
        super().__init__()
        self.db_path = db_path
        # Co jak nie będzie tabel w bazie? Upewnić się, czy są, jak nie to stworzyć
        self._load_all()

    def _load_all(self):
        with self._connect() as connection:
            cursor = connection.execute(
                """
                SELECT boat_id, name, boat_type, length, price, status, charter_dates
                FROM boats
                """
            )
            for boat_id, name, boat_type, length, price, status, charter_dates in cursor.fetchall():
                boat = Sailboat(boat_id, name, boat_type, length, price, status, charter_dates)
                super().__setitem__(boat_id, boat)

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def __setitem__(self, key: int, value: Sailboat):
        if key != value.boat_id:
            raise ValueError("Key must be equal boat id")

        super().__setitem__(key, value)

        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO boats (boat_id, name, boat_type, length, price, status, charter_dates)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    value.boat_id,
                    value.name,
                    value.boat_type,
                    value.length,
                    value.price,
                    value.charter_dates
                )
            )


    def __getitem__(self, boat_id: int) -> Sailboat:
        try:
            return super().__getitem__(boat_id)
        except KeyError:
            with self._connect() as connection:
                row = connection.execute(
                    """
                    SELECT boat_id, name, boat_type, length, price, status, charter_dates 
                    FROM boats WHERE boat_id = ?
                    """,
                    (boat_id,)
                ).fetchone()

            if row is None:
                raise KeyError(boat_id)

            boat = Sailboat(*row)
            super().__setitem__(boat_id, boat)
            return boat

    def __delitem__(self, boat_id: int) -> None:
        super().__delitem__(boat_id)

        with self._connect() as connection:
            connection.execute(
                """
                DELETE FROM boats WHERE boat_id = ?
                """,
                (boat_id,)
            )



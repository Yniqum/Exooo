from dataclasses import dataclass
# Task (1); (2); (3).

"""This module contains class with normal method, static and class methods"""


class NightClub:
    """This class night club different normal, static and class methods"""

    NAME = 'Malibu'

    def __init__(self, address: str, rating: int):
        self.address = address
        self.rating = rating

    def get_full_info(self) -> str:
        """Full info about current night club"""
        return f'NightClub {self.NAME} located at {self.address} and has a rating - {self.rating}.'

    @classmethod
    def get_name_night_club(cls) -> str:
        """Get current name night club"""
        return f'The one and only night_club -> {cls.NAME}.'

    @staticmethod
    def entry_by_age(age: int) -> bool:
        """Check age person for entry to current night club"""
        if 18 <= age <= 100:
            return True
        return False


@dataclass
class Bill:
    """storing the waiter's name and table number"""
    waiter: str
    table: int


vika = Bill("Vika", 3)

print(NightClub.get_name_night_club())
print(NightClub.entry_by_age(19))
print(NightClub('Street 1', 11).get_full_info())
print(f"Waiter: {vika.waiter}  Table: {vika.table}")

from typing import Dict

from constants import ___

Users_ids = set[int]
Users_ids_to_users_map = dict[int, tuple[str, int, list[int]]]

def calculate_total_spent_for_users(users_ids: Users_ids, users_ids_to_users_map: Users_ids_to_users_map) -> int:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_users(
        users_ids={3, 6, 12, 15},
        users_ids_to_users_map={
            3: ("Ilya", 32, [102, 15, 63, 12]),
        },
    ) == 192

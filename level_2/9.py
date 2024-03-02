import datetime

from constants import ___

Raw_receipt= str

def parse_receipt(raw_receipt: Raw_receipt) -> tuple[int, datetime.date, list[tuple[str, int, float]]]:
    pass


if __name__ == "__main__":
    assert (parse_receipt(raw_receipt="Кассовый чек 12 Продажа Позиции: ...",)
            == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)]))

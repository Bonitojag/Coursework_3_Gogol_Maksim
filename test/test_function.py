import json
from function import mask_card_number, format_iso_date,  format_and_print_operations, read_data_from_file


def test_mask_card_number():
    assert mask_card_number("Visa Classic 1234567812345678") == "Visa Classic 1234 56** **** 5678"
    assert mask_card_number("Счет 12345678901234567890") == "Счет **7890"
    assert  mask_card_number("Maestro 1234123412340000") == "Maestro 1234 12** **** 0000"
    assert mask_card_number("") == "N/A"



def test_format_iso_date():
    assert format_iso_date('2022-01-01T12:00:00') == '01-01-2022'
    assert format_iso_date('2022-12-31T23:59:59') == '31-12-2022'


def test_read_data_from_file(tmp_path):
    operations_file = tmp_path / "operations.json"
    with open(operations_file, "w", encoding="utf-8") as f:
        json.dump([], f)
    assert read_data_from_file(operations_file) == []


def test_format_and_print_operations():
    operations = [
        {
            "id": 269462132,
            "state": "EXECUTED",
            "date": "2018-08-14T05:42:30.104666",
            "operationAmount": {
                "amount": "19010.50",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 18125798580985711166",
            "to": "Счет 98841213648056852372"
        }
    ]
    format_and_print_operations(operations)
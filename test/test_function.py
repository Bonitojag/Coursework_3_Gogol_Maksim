
from function import mask_card_number, mask_account_number, format_and_print_operations, read_data_from_file


def test_mask_card_number():
    assert mask_card_number("1234 5678 1234 5678") == "N/A"
    assert mask_card_number("N/A") == "N/A"
    assert mask_card_number("12345678901234567890") == "N/A"
    assert mask_card_number("") == "N/A"

def test_mask_account_number():
    assert mask_account_number("1234 5678 1234 5678") == "N/A"
    assert mask_account_number("N/A") == "N/A"
    assert mask_account_number("12345678901234567890") == "N/A"
    assert mask_account_number("") == "N/A"



def test_format_and_print_operations(capsys):
    operations = [
        {
            "date": "2019-03-29T10:57:20.635567",
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1203921041964079",
            "to": "Счет 34616199494072692721",
            "operationAmount": {"amount": "30234.99", "currency": {"name": "RUB", "code": "USD"}}
        }
    ]
    format_and_print_operations(operations)
    captured = capsys.readouterr()
    assert "29.03.2019 Перевод с карты на счет\nVisa Classic 1203 **** **** 4079 -> Счет **** 2721\n30234.99 RUB\n\n" in captured.out



def test_read_data_from_file(mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data='[{"state": "EXECUTED"}]'))
    data = read_data_from_file('fake_path')
    assert data == [{"state": "EXECUTED"}]


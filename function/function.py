import json
from operator import itemgetter
import re



def mask_card_number(card_number):
    """Функция для маскировки номера карты или счета"""
    parts = card_number.split(' ')
    if len(parts) < 2:
        return "N/A"

    if len(parts[-1]) == 16:
        masked_last_part = f"**** **** {parts[-1][-4:]}"
    elif len(parts[-1]) == 20:
        masked_last_part = f"**** **** **** {parts[-1][-4:]}"
    else:
        return "N/A"

    if len(parts) == 2:
        masked_number = f"{parts[0]} {parts[1][:4]} {masked_last_part}"
    elif len(parts) == 3:
        masked_number = f"{parts[0]} {parts[1]} {parts[2][:4]} {masked_last_part}"
    else:
        return "N/A"
    return masked_number


def mask_account_number(account_number):
    """ Функция для маскировки номера счета или карт на который осуществляется перевод """
    parts = account_number.split(' ')

    if len(parts[-1]) == 16 or len(parts[-1]) == 20:
        mask_account_number = f"**** {parts[-1][-4:]}"
    else:
        return "N/A"

    if len(parts) == 2:
        account_number = f"{parts[0]} {mask_account_number}"
    elif len(parts) == 3:
        account_number = f"{parts[0]} {parts[1]} {mask_account_number}"
    else:
        return "N/A"
    return account_number

def format_and_print_operations(operations):
    """ Функция для форматирования и печати операций """
    operations.sort(key=itemgetter('date'), reverse=True)

    for operation in operations[:5]:
        # Преобразование даты из ISO формата в формат DD.MM.YYYY
        date = operation['date'][:10].split('-')
        formatted_date = f"{date[2]}.{date[1]}.{date[0]}"

        # Получение описания операции
        description = re.sub('<.*?>', '', operation['description'])

        # Маскировка номеров счетов и карт
        from_account = mask_card_number(operation.get('from', 'N/A'))
        to_account = mask_account_number(operation.get('to', 'N/A'))

        # Форматирование суммы операции и валюты
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        # Вывод информации
        print(f"{formatted_date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")

def read_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data




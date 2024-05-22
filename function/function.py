import json
from operator import itemgetter
import re
from datetime import datetime

def format_iso_date(iso_date: str) -> str:
    """Функция преобразует дату в формат 'DD-MM-YYYY'"""
    dt = datetime.fromisoformat(iso_date)
    return dt.strftime('%d-%m-%Y')

def mask_card_number(card_number):
    """Функция для маскировки номера карт и номера счета"""
    card_list = card_number.split()
    if len(card_list) < 2:
        return 'N/A'

    if len(card_list) == 2:
        if card_list[0] == 'Счет':
            return f'{card_list[0]} **{card_list[1][-4:]}'
        else:
            return f'{card_list[0]} {card_list[1][:4]} {card_list[1][4:6]}** **** {card_list[1][-4:]}'
    name = ' '.join(card_list[:-1])
    return f'{name} {card_list[-1][:4]} {card_list[-1][4:6]}** **** {card_list[-1][-4:]}'

def format_and_print_operations(operations):
    """Функция для форматирования и печати операций"""
    operations.sort(key=itemgetter('date'), reverse=True)

    for operation in operations[:5]:
        # преобразование даты из iso-формата в формат DD.MM.YYYY
        date = format_iso_date(operation['date'][:10])

        # получение описания операции
        description = re.sub('<.*?>', '', operation['description'])

        # маскировка номеров счетов и карт
        from_account = mask_card_number(operation.get('from', 'N/A'))
        to_account = mask_card_number(operation.get('to', 'N/A'))

        # форматирование суммы операции и валюты
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        # вывод информации
        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")

def read_data_from_file(file_path):
    """Функция для чтения данных из файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


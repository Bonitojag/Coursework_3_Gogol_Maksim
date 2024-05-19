from function import read_data_from_file, format_and_print_operations
import os
from pathlib import Path



if os.name == 'nt':
    OPERATIONS_PATH = Path('C:\\Users\\Maksim Gogol\\Desktop\\Coursework _3_ Gogol_Maksim\\operations.json')
else:
    OPERATIONS_PATH = Path('/mnt/c/Users/Maksim Gogol/Desktop/Coursework _3_ Gogol_Maksim/operations.json')

data = read_data_from_file(OPERATIONS_PATH)
executed_operations = [op for op in data if op.get("state") == 'EXECUTED']
format_and_print_operations(executed_operations)
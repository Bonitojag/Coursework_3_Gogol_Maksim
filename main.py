from function import read_data_from_file, format_and_print_operations
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OPERATIONS_PATH = BASE_DIR.joinpath('operations.json')


def main():
    operations = read_data_from_file(OPERATIONS_PATH)
    executed_operations = [
        op for op in operations
        if op.get("state") == 'EXECUTED'
    ]
    format_and_print_operations(executed_operations)


if __name__ == '__main__':
    main()

from .tree import data_from_gendiff
from .parser import parsing
from .data import prepare_data
from .formatters import get_formatter


def generate_diff(file_path1: str, file_path2: str,
                  format_name: str = 'stylish') -> str:
    data1, format1 = prepare_data(file_path1)
    data2, format2 = prepare_data(file_path2)
    parced_data1 = parsing(data1, format1)
    parced_data2 = parsing(data2, format2)
    diff = data_from_gendiff(parced_data1, parced_data2)
    return get_formatter(format_name)(diff)

from gendiff.create_diff_files import generate_diff_list
from gendiff.define_extension import split_filename
from gendiff.open_file import open_file


def generate_diff(file1, file2):
    result_str = '{\n'
    data1, extension1 = split_filename(file1)
    data2, extension2 = split_filename(file2)
    parsed_file1 = open_file(data1, extension1)
    parsed_file2 = open_file(data2, extension2)
    result_list = generate_diff_list(parsed_file1, parsed_file2)
    for k in result_list:
        if k['operator'] == 'remove':
            result_str += '- '
        elif k['operator'] == 'add':
            result_str += '+ '
        else:
            result_str += '  '
        result_str += k['key'] + ': '
        result_str += str(k['value']) + '\n'
    result_str += '}'
    result_str_1 = result_str.replace('True', 'true')
    result_str_2 = result_str_1.replace('False', 'false')
    return result_str_2

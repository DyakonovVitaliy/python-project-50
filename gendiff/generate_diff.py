from gendiff.diff_files_json import generate_diff_list


def generate_diff(file1, file2):
    result_str = '{\n'
    result_list = generate_diff_list(file1, file2)
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

def generate_diff_list(first_file, second_file):    # noqa: C901
    result_list = []
    list_everything_keys = sorted(
        list(set(first_file.keys()) | set(second_file.keys())))
    for key in list_everything_keys:
        if key not in first_file:
            result_list.append(
                {'operator': 'add', 'key': key, 'value': second_file[key]}
            )
        elif key not in second_file:
            result_list.append(
                {'operator': 'remove', 'key': key, 'value': first_file[key]}
            )
        elif isinstance(first_file[key], dict) and isinstance(
                second_file[key], dict):
            child = generate_diff_list(first_file[key], second_file[key])
            result_list.append(
                {'operator': 'nested', 'key': key, 'value': child}
            )
        elif first_file[key] == second_file[key]:
            result_list.append(
                {'operator': 'nothing', 'key': key, 'value': first_file[key]}
            )
        elif first_file[key] != second_file[key]:
            result_list.append(
                {'operator': 'changed', 'key': key,
                 'old': first_file[key], 'new': second_file[key]}
            )
    return result_list

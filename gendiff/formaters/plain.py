def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def build_plain(diff, path=""):
    result_str = list()
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"

        if dictionary['operator'] == 'add':
            result_str.append(f"Property '{property}' "
                              f"was added with value: "
                              f"{to_str(dictionary['value'])}")

        if dictionary['operator'] == 'remove':
            result_str.append(f"Property '{property}' was removed")

        if dictionary['operator'] == 'nested':
            new_value = build_plain(dictionary['value'], f"{property}.")
            result_str.append(f"{new_value}")

        if dictionary['operator'] == 'changed':
            result_str.append(f"Property '{property}' was updated. "
                              f"From {to_str(dictionary['old'])} to "
                              f"{to_str(dictionary['new'])}")
    return '\n'.join(result_str)


def render_plain(diff):
    return build_plain(diff)

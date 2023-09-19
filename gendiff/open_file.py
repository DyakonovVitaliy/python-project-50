import json
import yaml


def open_file(data, extension):
    if extension == 'json':
        return yaml.safe_load(data)
    if extension in ('yml', 'yaml'):
        return json.loads(data)

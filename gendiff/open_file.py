import json
import yaml


def open_file(data, extension):
    if extension == 'json':
        return json.loads(data)
    if extension in ('yml', 'yaml'):
        return yaml.safe_load(data)

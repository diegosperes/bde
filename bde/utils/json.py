import json


def parse_json_file(path):
    with open(path) as json_file:
        content = "".join(json_file.readlines())
        return json.loads(content)

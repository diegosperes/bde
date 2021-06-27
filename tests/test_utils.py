from json.decoder import JSONDecodeError

import pytest

from bde import utils


@pytest.mark.parametrize("file_object", [("/tmp/json.json", "{}")], indirect=True)
def test_parse_json_file(file_object):
    path = file_object.name
    assert {} == utils.parse_json_file(path)


@pytest.mark.parametrize("file_object", [("/tmp/json.json", "{")], indirect=True)
def test_parse_malformed_json_file(file_object):
    path = file_object.name
    with pytest.raises(JSONDecodeError):
        utils.parse_json_file(path)


def test_parse_nonexistent_json_file():
    with pytest.raises(FileNotFoundError):
        utils.parse_json_file("/tmp/json.json")

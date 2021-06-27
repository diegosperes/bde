import pytest

from bde.utils import Configuration


@pytest.mark.parametrize(
    "file_object", [("/tmp/json.json", '{"default": true}')], indirect=True
)
def test_parse_configuration(file_object):
    path = file_object.name
    assert True == Configuration(path).default


@pytest.mark.parametrize("file_object", [("/tmp/json.json", "{}")], indirect=True)
def test_accessing_nonexisting_configuration(file_object):
    path = file_object.name
    with pytest.raises(AttributeError):
        assert True == Configuration(path).default

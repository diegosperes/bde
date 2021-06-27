import os
import json

import pytest


@pytest.fixture()
def file_object(request):
    """
    Create a json file in the system.
    """
    path, content = request.param

    if isinstance(content, str):
        _content = content
    else:
        raise ValueError(
            "content parameter must be an instance of dict, or list, or str."
        )

    with open(path, "w+") as _file_object:
        _file_object.writelines(_content)
        _file_object.seek(0, 0)
        yield _file_object

    os.remove(path)

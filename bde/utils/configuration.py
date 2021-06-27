import os
from typing import List

from bde.utils import parse_json_file


class Configuration:
    def __init__(self, path: str):
        self.__path = path
        self.__parse_configuration()

    def __parse_configuration(self):
        self.__content = parse_json_file(self.__path)

    def __getattr__(self, attribute):
        if attribute not in self.__content:
            raise AttributeError(
                f"'Configuration' object has not attribute {attribute}"
            )
        return self.__content[attribute]

from abc import abstractmethod
from dataclasses import dataclass
from tablebin.conditions import Condition
from tablebin.style import RowStyle


class TableFormatter(object):
    @abstractmethod
    def format(self, **kwargs) -> str:
        pass


class TableLinkFormatter(TableFormatter):
    def __init__(self, text="link", target="#", **kwargs):
        self._text = text
        self._target = target

    def format(self, **kwargs) -> str:
        return f'<a href="{self._target}">{self._text}</a>'


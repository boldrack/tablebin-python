from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Style:
    property: str
    value: str

    def serialize(self):
        return {self.property: self.value}

@dataclass
class RowStyle:
    styles: List[Style] # List[dict] # [{prop: v, ...}]

    @classmethod
    def from_dict(cls, _dict: Dict[str, str]):
        return cls(
            styles=[Style(property=property, value=value) for property, value in _dict.items()]
        )

    def serialize(self):
        return {style.property: style.value for style in self.styles}




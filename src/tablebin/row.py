from dataclasses import dataclass
from tablebin.conditions import Condition
from tablebin.style import RowStyle

@dataclass
class RowFormat: 
    rowstyle: RowStyle
    condition: Condition

    def serialize(self, ):
        ''' <elem style={{...}}'''
        return { 
            'style': self.rowstyle.serialize(),
            'condition': self.condition.serialize()
        }



from typing import Union
import json 


class Condition:
    '''
    column is an entity in the context of a condition
    same as expression
    perhaps we should have supported conditions on the frontend . 
    to start with . then just transmit it's identifiable slug for 
    identifier and resolvement
    '''
    slug = 'base_condition'

    def serialize(self, ):
        return {
                "name": self.slug, 
                "arguments": {
                }
            }


class ColumnValueGTCondition(Condition):
    '''
    This only works with a single column that needs to be specified
    and transmitted along as argument to the condition when resolved 
    on the FE
    '''
    slug = 'column_value_GT_condition'
    
    def __init__(self, column_name: str, gt_value: Union[int, float]):
        self.column_name = column_name
        self.gt_value = gt_value

    def serialize(self, ):
        return {
                "name": self.slug, 
                "arguments": {
                    "column_name": self.column_name,
                    "gt_value": self.gt_value
                }
            }

class ColumnValueLTCondition(Condition):
    '''
    This only works with a single column that needs to be specified
    and transmitted along as argument to the condition when resolved 
    on the FE
    '''
    slug = 'column_value_LT_condition'
    
    def __init__(self, column_name: str, lt_value: Union[int, float]):
        self.column_name = column_name
        self.lt_value = lt_value

    def serialize(self, ):
        return {
                "name": self.slug, 
                "arguments": {
                    "column_name": self.column_name,
                    "lt_value": self.lt_value
                }
            }
        



class ColumnValueGTECondition(ColumnValueGTCondition):
    slug = 'column_value_GTE_condition'




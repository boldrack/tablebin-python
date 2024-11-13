from dataclasses import dataclass, field
from typing import List, Optional, Union
import pprint

import requests
from tablebin.formatters import TableFormatter
from tablebin.row import RowFormat

FieldTypes = ('string', 'number', 'boolean')


@dataclass
class TableConfig:
    row_formatters: List[RowFormat] = field(default_factory=list)
    protected: bool = False

    def _serialize(self):
        return { 
            'protected': self.protected, 
            'row_formatters': [formatter.serialize() for formatter in self.row_formatters]
        }

    def set_rowformatters(self, formatters: List[RowFormat]):
        self.row_formatters = formatters


@dataclass
class TableColumn:
    name: str
    field_type: str = 'string' # validate this 
    sortable: bool = False
    formatter: Optional[TableFormatter] = None

    def __post_init__(self):
        assert(self.field_type in FieldTypes)


class TableHeader:
    '''
    container for table header. only requires table items on the minimum
    '''
    def __init__(self) -> None:
        self._columns: List[TableColumn] = []


    def add_column(self, column: TableColumn):
        self._columns.append(column)


    @property
    def columns(self):
        return self._columns


    def _serialize(self, ):
        
        return [
            {'name': column.name, 'field_type': column.field_type, 
             'sortable': column.sortable, 
             'formatter': column.formatter.format() if column.formatter else None
            } 
            for column in self._columns
        ]


class TableData: 
    '''
    a container for the table data along with validations and helper methods 
    '''
    def __init__(self, data: List[List[Union[str, int, bool]]], *args, **kwargs):
        self._data = data
        self._validated = False
        # TODO: perform validation here


    def validate(self, header: TableHeader):
        # TODO: validate the row length for each 
        pass


    def _serialize(self, ):
        return self._data


class TableBin:
    '''
    The main container / class for the table bin interactor 
    houses small components 
    '''
    API_HOST = 'http://localhost:8000'
    # API_HOST = 'https://api.tablebin.app'

    def __init__(self, api_key: str, *args, **kwargs):
        self._api_key = api_key


    def _make_tablebin_request(self, endpoint: str, data):
        # adds headers as appropriate 
        # handle failure with our exceptions
        # ... add more 
        url = '/'.join([self.API_HOST, endpoint])
        print(url)
        headers = {'Content-Type': 'application/json', 'X-API-KEY': self._api_key}
        print(headers)
        response = requests.post(url, json=data, headers=headers, timeout=60)
        print(f'{response.text=}')
        # return response.json()
        return response


    def create_table(self, header: TableHeader, data: TableData, row_formatters=None):
        '''
        what we expecting from these two containers . 
        header: 
            items: 
                field_type
                name
        data: 
            just the row of data but with validation

        -- 
        data wise what do we need to create a table at table bin
        - header.items[n]name,field_type -> need extrac this from the header instance 
        - config -> ought to be optional 
        - table_data -> a list of list 
        '''
        config = TableConfig() 
        if row_formatters:
            config.set_rowformatters(row_formatters)

        # TODO: validation ; assert the right container instance are passed 
        #   for both header and data

        json_data = {'header': {'items': header._serialize()}, 'config': config._serialize(), 
                     'data': data._serialize() }
        pprint.pprint(json_data)
        response = self._make_tablebin_request('tables/', json_data)
        return response



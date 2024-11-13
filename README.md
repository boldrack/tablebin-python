# tablebin-python
A light weight python api for the table bin platform. 

A sample code looks like below 

    with open('mylist.json') as f: 
        mylist = json.load(f)

    header = tablebin.TableHeader()

    hash_formatter = formatters.TableLinkFormatter(text="hash", target="https://etherscan.io/tx/{{this}}")
    header.add_column(tablebin.TableColumn(name='hash', field_type='string', formatter=hash_formatter))

    header.add_column(tablebin.TableColumn(name='owner', field_type='string'))
    header.add_column(tablebin.TableColumn(name='eth_value', field_type='string', sortable=True))
    header.add_column(tablebin.TableColumn(name='balance', field_type='string', sortable=True))
    header.add_column(tablebin.TableColumn(name='total', field_type='number', sortable=True))
    header.add_column(tablebin.TableColumn(name='count', field_type='number', sortable=True))

    header.add_column(tablebin.TableColumn(name='timestamp', field_type='string'))
    header.add_column(tablebin.TableColumn(name='buy_cap', field_type='string', sortable=True))

    config = tablebin.TableConfig()

    table_data = tablebin.TableData(mylist)

    table_bin = tablebin.TableBin(api_key=TABLE_BIN_API_KEY)
    # print(table_data._data)

    response = table_bin.create_table(header, table_data)

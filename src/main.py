import tablebin
from tablebin.conditions import ColumnValueLTCondition, ColumnValueGTCondition
from tablebin.style import RowStyle, Style
from tablebin.row import RowFormat

GreenBackgroundColorStyle = RowStyle.from_dict({'backgroundColor': 'green', 'color': 'white'})
RedBackgroundColorStyle = RowStyle(styles=[Style(property='backgroundColor', value='red')])

'''
we're creating a row level styling formatting. with a row style that paints our row green 
if the condition goes thus: the pnl column for that row is greater than zero
This then be passed into the table config.row_formatters 
'''
style_positive_pnl = RowFormat(
    rowstyle=GreenBackgroundColorStyle, 
    condition=ColumnValueGTCondition(column_name='pnl', gt_value=0)
)

style_negative_pnl = RowFormat(
    rowstyle=RedBackgroundColorStyle, 
    condition=ColumnValueLTCondition(column_name='pnl', lt_value=0)
)

# print(style_negative_pnl.serialize())
# print(style_positive_pnl.serialize())

mylist = [
    ['adfjakljfalkjflkasjdfklasjf', 232],
    ['adfjakljfalkjflkasjdfklasjf', 22],
    ['adfjakljfalkjflkasjdfklasjf', 32],
    ['adfjakljfalkjflkasjdfklasjf', -32],
    ['adfjakljfalkjflkasjdfklasjf', 52],
]

TABLE_BIN_API_KEY = '65ef2450-32ee-49f8-babf-03aaec2986f8'
header = tablebin.TableHeader()

header.add_column(tablebin.TableColumn(name='hash', field_type='string'))
header.add_column(tablebin.TableColumn(name='pnl', field_type='number'))

table_data = tablebin.TableData(mylist)

tablebin_o = tablebin.TableBin(api_key=TABLE_BIN_API_KEY)
tablebin_o.create_table(header, table_data, row_formatters=[style_positive_pnl, style_negative_pnl])


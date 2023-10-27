from requests import HTTPError
from py3pin.Pinterest import Pinterest
from datetime import datetime
import math
import commons.credentials as cred
import commons.excel_reader as excel
import commons.persistence_utils as db

default_board = '1050957331733068645' # Board: Bebês
default_pin = '1050957263028824748' # Pin: Pega correta na amamentação - como fazer

remove_char = '_'


def get_or_default(item, default_value):
    if (isinstance(item, str)):
        return default_value if (len(item) == 0 or item == 'nan') else item
    else:
        return default_value if (math.isnan(item)) else item

print('####################')
start = datetime.now()
print(f'Repin - {start}')
print('####################')

pinterest = Pinterest(
    email=cred.email, 
    password=cred.password, 
    username=cred.username, 
    cred_root=cred.cred_root
)
#pinterest.login()

# load previously processed lines
processed = db.get_processed_repin()

# read today's lines from Excel
todo_list = excel.get_repin_lines_from_today(start.time())
for item in todo_list:
    print(f'Processing line: {item}')
    id = int(item[excel.col_id])
    board_id = get_or_default(str(item[excel.repin_col_board_id]).removeprefix(remove_char), default_board)
    pin_id = get_or_default(item[excel.repin_col_pin_id], default_pin)

    print(f'Using:')
    print(f'   - id: {id};')
    print(f'   - board_id: {board_id};')
    print(f'   - pin_id: {pin_id};')

    if (str(id) in processed):
        print(f'Item [{id}] previously processed.')
    else:
        try:
            pin = pinterest.repin(board_id=board_id, section_id=None, pin_id=pin_id)
            print(f'Response code: {pin.status_code}')
            processed.add(str(id))
            db.update_processed_repin(processed)
        except HTTPError as error:
            print(f'Failed to process request: {error}')
    print()

#pinterest.logout()
elapsed = datetime.now()-start
print('####################')
print(f'Repin finished - Took: {elapsed}')
print('####################')

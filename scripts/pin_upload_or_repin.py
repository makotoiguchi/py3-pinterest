from requests import HTTPError
from py3pin.Pinterest import Pinterest
from datetime import datetime
import json
import math
import os
import commons.credentials as cred
import commons.excel_reader as excel
import commons.persistence_utils as db

default_board = '1050957331733068645' # Board: Bebês
default_image = 'data/default/pinterest-default-image.png'
default_desc = 'default description'
default_title = 'default title'
default_alt_text = 'default alt text'
default_link = 'https://sosmamae.com.br'

remove_char = '_'


def get_or_default(item, default_value):
    if (isinstance(item, str)):
        return default_value if (len(item) == 0 or item == 'nan') else item
    else:
        return default_value if (math.isnan(item)) else item


def build_image_path(folder, filename):
    if ((not isinstance(folder, str) and math.isnan(folder)) or
        (not isinstance(filename, str) and math.isnan(filename))):
        return default_image
    
    image_file = 'data/POSTS/' + folder + '/Pinterest/' + filename
    if (os.path.isfile(image_file)):
        return image_file
    
    return default_image


print('####################')
start = datetime.now()
print(f'Pin - {start}')
print('####################')

pinterest = Pinterest(
    email=cred.email, 
    password=cred.password, 
    username=cred.username, 
    cred_root=cred.cred_root
)
#pinterest.login()

# load previously processed lines
processed = db.get_processed_pin()
original_pins = db.get_original_pins()

pins_created = 0
pins_ignored = 0

# read today's lines from Excel
todo_list = excel.get_pin_lines_from_today(start.time())
for item in todo_list:
    print(f'Processing line: {item}')
    id = int(item[excel.col_id])
    board_id = get_or_default(str(item[excel.pin_col_board_id]).removeprefix(remove_char), default_board)
    image_file = build_image_path(item[excel.pin_col_folder], item[excel.pin_col_image])
    description = get_or_default(item[excel.pin_col_description], default_desc)
    link = get_or_default(item[excel.pin_col_link], default_link)
    title = get_or_default(item[excel.pin_col_title], default_title)
    alt_text = get_or_default(item[excel.pin_col_alt_text], default_alt_text)
    original_pin = f'{title}-{image_file}'

    print(f'Using:')
    print(f'   - id: {id};')
    print(f'   - board_id: {board_id};')
    print(f'   - image_file: {image_file};')
    print(f'   - description: {description};')
    print(f'   - link: {link}')
    print(f'   - title: {title}')
    print(f'   - alt_text: {alt_text}')
    print(f'   - original_pin: {original_pin};')

    if (str(id) in processed):
        print(f'Item [{id}] previously processed.')
        pins_ignored += 1
    else:
        try:
            if (original_pin in original_pins):
                # if current request has an original_pin, we should only repin it
                original_pin_id = original_pins[original_pin]
                print(f'Repinning the original pin {original_pin_id}')
                pin = pinterest.repin(board_id=board_id, section_id=None, pin_id=original_pin_id)
                print(f'Response code: {pin.status_code}')
                pins_created += 1
            else:
                # if current request has no original_pin, we should upload a new one
                print('Uploading a new pin')
                pin = pinterest.upload_pin(board_id, image_file, description, link, title, alt_text)
                print(f'Response code: {pin.status_code}')
                response = json.loads(pin.text)
                try: 
                    pin_id = response['resource_response']['data']['id']
                    db.add_new_pin(original_pin, pin_id)
                    pins_created += 1
                except KeyError as error:
                    print(f'New Pin Id not present in response.')

            # add to processed list, whether it is an original pin or not
            processed.add(str(id))
            db.update_processed_pin(processed)
        except HTTPError as error:
            print(f'Failed to process request: {error}')
    print()

#pinterest.logout()
elapsed = datetime.now()-start
print(f'Pins ignored: {pins_ignored}')
print(f'Pins created: {pins_created}')
print('####################')
print(f'Repin finished - Took: {elapsed}')
print('####################')

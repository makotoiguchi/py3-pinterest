import os

repin_file = 'data/processed/repinned.txt'
pin_file = 'data/processed/pinned.txt'
original_pins_file = 'data/processed/original_pins.txt'
kv_separator = ':'

def get_processed_items(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            items = set(file.read().split())
            print(f'Opening file [{filename}] with [{len(items)}] processed items.\n')
            return items
    except FileNotFoundError:
        print(f'Persistence file [{filename}] not found. Returning empty set.\n')
        return set()


def get_processed_repin():
    return get_processed_items(repin_file)


def get_processed_pin():
    return get_processed_items(pin_file)

##

def update_processed_items(filename, updated_set):
    print(f'Updating file [{filename}]')
    with open(filename, 'w', encoding='utf-8') as file:
        for item in updated_set:
            file.write(f'{item}\n')


def update_processed_repin(updated_set):
    return update_processed_items(repin_file, updated_set)


def update_processed_pin(updated_set):
    return update_processed_items(pin_file, updated_set)

##

def get_original_pins():
    print(f'Load original pins')
    pins = {}
    try:
        with open(original_pins_file, 'r', encoding='utf-8') as lines:
            print(f'Opening file [{original_pins_file}].\n')
            for line in lines:
                kv = line.split(kv_separator)
                pins[kv[0]] = kv[1]
    except FileNotFoundError:
        print(f'Persistence file [{original_pins_file}] not found. Returning empty dictionary.\n')
    return pins

def add_new_pin(original_pin, pin_id):
    print(f'Adding new pin for Request ID [{original_pin}]: [{pin_id}]')
    with open(original_pins_file, 'w', encoding='utf-8') as file:
        file.write(f'{original_pin}{kv_separator}{pin_id}\n')


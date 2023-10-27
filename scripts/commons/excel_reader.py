import pandas as pd
from datetime import datetime

excel_file = 'data/Pinterest/Pinterest.xlsx'

col_id = 'Id'
col_date = 'Data'
col_hour = 'Hora'

repin_name = 'Repin'
repin_col_board_id = 'Board id'
repin_col_pin_id = 'Pin id'

pin_name = 'Pin'
pin_col_board_id = 'Board Id'
pin_col_folder = 'Folder'
pin_col_image = 'Image file'
pin_col_description = 'Description'
pin_col_title = 'Title'
pin_col_alt_text = 'Alt Text'
pin_col_link = 'Link'


def get_lines_from_today(sheet_name, time_threshold):
    print(f'Opening source file to read and filter by until today at {time_threshold}')
    today = datetime.today().date()

    sheet = pd.read_excel(io=excel_file, sheet_name=sheet_name)
    sheet[col_date] = pd.to_datetime(sheet[col_date])
    print(f'Original lines: {sheet.shape[0]}')

    filtered_sheet = sheet[(sheet[col_id] > 0) & 
                           (sheet[col_date].dt.date == today) & 
                           (sheet[col_hour] < time_threshold)]
    print(f'Filtered lines: {filtered_sheet.shape[0]}')

    print('First lines:')
    print(filtered_sheet.head())
    print()
    return [row.to_dict() for _, row in filtered_sheet.iterrows()]


def get_repin_lines_from_today(time_threshold):
    return get_lines_from_today(repin_name, time_threshold)


def get_pin_lines_from_today(time_threshold):
    return get_lines_from_today(pin_name, time_threshold)
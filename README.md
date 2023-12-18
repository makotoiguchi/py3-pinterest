# SOS Mamãe

## Source files

We copy the Pinterest.xlsx file to mitigate open files concurrency in Windows.
If copy fails, we will use the previous copy of the file.

Copy file from:
   
    _____SOURCE_FOLDER_____/Pinterest.xlsx

to:

    _____PROJECT_FOLDER_____/data/Pinterest/Pinterest.xlsx

## Update Credentials

Update Pinterest credentials on:

    script/commons/credentials.py

## Running scripts

### Activate venv

Before all, we need to activate venv

    venv/Scripts/Activate.ps1

### Get Boards

Get boards name and ID

    python scripts/boards_get.py

Source file:

    data/Pinterest/Pinterest.xlsx
        sheet: Pin

Output file:

    data/boards.txt

### Create new Pin or repin it

Create a new Pin or repin a previously created pin.
Filter pins from source by date (today) and time.
Checks if Pin line was previously processed.
Checks if there is an original pin previously pinned and, if so, repin it to a new board.

    python scripts/pin_upload_or_repin.py

Source file:

    data/Pinterest/Pinterest.xlsx
        sheet: Repin
        columns:
            - Id
            - Data
            - Hora
            - Title
                note: also used as 'Original Pin'
            - Description
            - Board Id
            - Image file
            - Folder
            - Link
            - Alt Text

Based on the values specified on the columns of Pinterest.xlsx, we will read files from:

    data/POSTS/<FOLDER>/Pinterest/<FILENAME>
        - <FOLDER> is column "Folder"
        - <FILENAME> is column "Image file"

The path above may be adjusted as needed by modifying the script.

Output files:

    data/processed/pinned.txt
        - one processed Id per line 
    data/processed/original_pins.txt
        - one pair original_pin:pin_id per line

### Repin from another account

Repin an existing Pin from another account.
Filter pins from source by date (today) and time.
Checks if Pin line was previously processed.

    python scripts/pin_repin.py

Source file:

    data/Pinterest/Pinterest.xlsx
        sheet: Repin
        columns:
            - Id
            - Data
            - Hora
            - Board id
            - Pin id

Output files:

    data/processed/repinned.txt
        - one processed Id per line


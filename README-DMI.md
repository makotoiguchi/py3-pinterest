# SOS Mamãe

## Source files

Copy folders from:

    OneDrive > Meus arquivos > Documents > blog - sos mamae >
        POSTS:     https://onedrive.live.com/?id=15E3CBA5E00A9257%21160750&cid=15E3CBA5E00A9257
        Pinterest: https://onedrive.live.com/?id=15E3CBA5E00A9257%21162007&cid=15E3CBA5E00A9257

to:

    data/

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

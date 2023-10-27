from py3pin.Pinterest import Pinterest
import commons.credentials as cred
from datetime import datetime

print('####################')
start = datetime.now()
print(f'Get Boards - {start}')
print('####################')

pinterest = Pinterest(
    email=cred.email, 
    password=cred.password, 
    username=cred.username, 
    cred_root=cred.cred_root
)
#pinterest.login()

boards = pinterest.boards_all(username=cred.username)
print(f'Boards retrieved: {len(boards)}')

with open('data/boards.txt', 'w', encoding='utf-8') as f:
    print('BOARDS:')
    f.write('BOARDS:\n')
    for board in boards:
        print(f"   name: {board['name']} --> id: {board['id']}")
        f.write(f"   name: {board['name']} --> id: {board['id']}\n")

#pinterest.logout()
elapsed = datetime.now()-start
print('####################')
print(f'Get Boards finished - Took: {elapsed}')
print('####################')
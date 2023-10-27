from py3pin.Pinterest import Pinterest
import credentials

pinterest = Pinterest(
    email=credentials.email, 
    password=credentials.password, 
    username=credentials.username, 
    cred_root=credentials.cred_root
)
#pinterest.login()

pin = pinterest.load_pin('1050957263028824748')
#print(pin)
print(f"ID: {pin['id']} - TITLE: {pin['title']}")

#pinterest.logout()
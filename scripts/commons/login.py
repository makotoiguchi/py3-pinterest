from py3pin.Pinterest import Pinterest
import credentials

pinterest = Pinterest(
    email=credentials.email, 
    password=credentials.password, 
    username=credentials.username, 
    cred_root=credentials.cred_root
)
pinterest.login()
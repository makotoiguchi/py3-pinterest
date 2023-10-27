from py3pin.Pinterest import Pinterest
import commons.credentials as cred

feed_url='https://br.pinterest.com/sosmamaeblog/feed.rss'

pinterest = Pinterest(
    email=cred.email, 
    password=cred.password, 
    username=cred.username, 
    cred_root=cred.cred_root
)
#pinterest.login()

pins = pinterest.get(feed_url)

print(pins.text)

#pinterest.logout()
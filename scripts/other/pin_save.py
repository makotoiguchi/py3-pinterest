from py3pin.Pinterest import Pinterest
import credentials

pinterest = Pinterest(
    email=credentials.email, 
    password=credentials.password, 
    username=credentials.username, 
    cred_root=credentials.cred_root
)
#pinterest.login()

pin = pinterest.pin(
    board_id='1050957331733068645',
    section_id=None,
    image_url='https://sosmamae.com.br/wp-content/uploads/2023/10/nomes-japoneses-masculinos-conteudo.jpg',
    description='Pesquisando nomes japoneses masculinos? Aqui você encontra 52 ideias de nome masculinos elegantes, com significados fortes, raros, antigos e da moda.',
    title='Nomes japoneses masculinos e seus significados',
    alt_text='Nomes japoneses masculinos e seus significados',
    link='https://sosmamae.com.br/bebe/nomes-japoneses-masculinos-e-seus-significados/'
)
print(pin)

#pinterest.logout()
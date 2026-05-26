import time
import random
import requests
import requests
from bs4 import BeautifulSoup
import sys

#dominio do site/endereço 
page_title = ''
url = 'https://httpbin.org/ip'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


 #REDE TOR
proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}



def bpk(username, password):
    credencial = {'username' :username, 'password' :password}
    try:
        r = requests.get(
            url, # Site
            proxies=proxies,
            headers=headers,
            timeout=10
        )

        print("IP atual:")
        print(r.text)

    except Exception as erro:
        print("Erro no proxy:")
        print(erro)

    soup = BeautifulSoup(r, 'html.parser')
    if soup.title.text == page_title: #compara resposta esprada
        print('|===========================================================================|')
        print(f"        [+] Combinação encontrada com sucesso {username} : {password} [+]")
        print('|===========================================================================|')
        print('\n')
        sys.exit()
    else:
        pass
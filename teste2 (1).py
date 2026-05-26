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

#REDE TESTE
try:
    r = requests.get(
        "https://httpbin.org/ip", # Site
        proxies=proxies,
        headers=headers,
        timeout=10
    )

    print("IP atual:")
    print(r.text)

except Exception as erro:
    print("Erro no proxy:")
    print(erro)


# SEGUNDA ALTERNATIVA/ADAPTAVEL

# def brute(username, password):
#     data = {'username' : username, 'password' : password}      
    
#     r = requests.post(url, data=data, headers=headers).text
    
#     soup = BeautifulSoup(r, 'html.parser')
#     if soup.title.text == page_title:
#         print('|===========================================================================|')
#         print(f"          [+] A match was found with {username} : {password} [+]")
#         print('|===========================================================================|')
#         print('\n')
#         sys.exit()
#     else:
#         pass

#WORDLIST_USER
usuarios = "./users.txt"

#WORDLIST_PASS
senhas = "./pass.txt" 

# Usuários ainda pendentes
usuarios_pendentes = usuarios.copy()

# =========================
# SIMULAÇÃO
# =========================

def testar_login(usuario, senha):

    print(f"[{usuario}] -> TESTANDO")
    print(f"Senha: {senha}")

    # Simulação aleatória apenas para estudo
    return random.choice([True, False])

# =========================
# LOOP PRINCIPAL
# =========================

print("""
    ██████╗ ██╗  ██╗██████╗ 
    ██╔══██╗██║ ██╔╝██╔══██╗
    ██████╔╝█████╔╝ ██████╔╝
    ██╔══██╗██╔═██╗ ██╔═══╝ 
    ██████╔╝██║  ██╗██║     
    ╚═════╝ ╚═╝  ╚═╝╚═╝     

            BY GABRIEL
    """)
    

for senha in senhas:
   

    print("\n======================")
    print(f"TESTANDO SENHA: {senha}")
    print("======================\n")

    falharam = []
    #Brincadeira_começa xd
    for usuario in usuarios_pendentes:

        print(f"[*] TESTANDO | Usuário: {usuario:<15} | Senha: {senha}")

        try:
            resultado = testar_login(usuario, senha)

            if resultado:
                print(f"[+] SUCESSO  | Usuário: {usuario:<15} | Senha: {senha}")

            else:
                print(f"[-] FALHOU  | Usuário: {usuario:<15}")
                falharam.append(usuario)

        except Exception as erro:
            print(f"Erro: {erro}")
            falharam.append(usuario)

        # Delay pequeno
        time.sleep(2)

    # Atualiza apenas quem falhou
    usuarios_pendentes = falharam

    # Relatório
    print("\n===== RELATÓRIO =====")

    print(f"Usuários restantes: {len(usuarios_pendentes)}")

    for user in usuarios_pendentes:
        print(f"- {user}")

    # Se todos passarem
    if not usuarios_pendentes:
        print("\nTodos finalizaram.")
        break

    print("\nAguardando próxima rodada...\n")

    # Para testes rápidos:
    time.sleep(10)

    # Produção/laboratório:
    # time.sleep(3600)

print("\nExecução encerrada.")
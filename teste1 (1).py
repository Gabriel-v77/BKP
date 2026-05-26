import time
import random
import requests



 #REDE TOR
proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}

#REDE TESTE

try:
    r = requests.get(
        "https://httpbin.org/ip",
        proxies=proxies,
        timeout=10
    )

    print("IP atual:")
    print(r.text)

except Exception as erro:
    print("Erro no proxy:")
    print(erro)

#WORDLIST_USER
usuarios = [
    "usuario1",
    "usuario2",
    "usuario3"
]

#WORDLIST_PASS
senhas = [
    "senha123",
    "admin123",
    "teste2025"
]

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
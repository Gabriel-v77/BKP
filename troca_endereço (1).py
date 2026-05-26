import time
import requests
from stem.control import Controller
from stem import Signal

# Configuração do proxy Tor (SOCKS5)
# Tudo que o requests fizer vai passar pelo Tor Browser na porta 9150
proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}

# Função responsável por pegar o IP atual que está saindo pelo Tor
def get_ip():
    # Faz requisição passando pelo Tor para descobrir o IP de saída
    r = requests.get(
        "https://check.torproject.org/api/ip",
        proxies=proxies,
        timeout=10
    )
    
    # Converte resposta JSON em dicionário Python
    data = r.json()
    
    # Retorna apenas o IP
    return data["IP"]

# Mostra o IP atual antes da troca de circuito
print("IP atual:", get_ip())

# Conecta no ControlPort do Tor (porta 9051)
# Isso permite enviar comandos internos ao Tor
with Controller.from_port(port=9051) as controller:
    
    # Autentica para poder enviar comandos
    controller.authenticate()

    # Solicita um novo circuito (novo IP de saída)
    controller.signal(Signal.NEWNYM)

# Mensagem informando que está aguardando a troca
print("Aguardando novo circuito...")

# dalay para que o tor consiga trocar o ip, leva um tempo..
# Sem isso, pode retornar o mesmo IP antigo
time.sleep(5)

# Mostra o novo IP após a troca de circuito
print("Novo IP:", get_ip())
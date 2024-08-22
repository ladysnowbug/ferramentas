import requests

def verificar_subdominios():
    subdominios = []

    # Lê o arquivo e armazena os 20 primeiros subdomínios
    try:
        with open('subdomains-top30.txt', 'r') as file:
            for i, linha in enumerate(file):
                if i >= 20:
                    break
                subdominios.append(linha.strip())
    except FileNotFoundError:
        print("Erro: Arquivo 'subdomains-top30.txt' não encontrado.")
        return
    
    # Realiza as requisições GET nos subdomínios e exibe os status codes
    for subdominio in subdominios:
        url = f"http://{subdominio}"
        try:
            response = requests.get(url)
            print(f"{url}: {response.status_code}\n")
        except requests.exceptions.ConnectionError as e:
            print(f"{url}: Falha ao conectar ({e})\n")



# uso
verificar_subdominios()

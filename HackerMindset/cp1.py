import requests

print('1TDCPG-Giovanna Santos')
alvo = input('Alvo:')

def verificar_subdominios():
    subdominios = []

    # Lê o arquivo e armazena os 5 primeiros subdomínios
    try:
        with open('subdomains-top30.txt', 'r') as file:
            for i, linha in enumerate(file):
                if i >= 5:
                    break
                subdominios.append(linha.strip())
    except FileNotFoundError:
        print("Erro: Arquivo 'subdomains-top30.txt' não encontrado.")
        return
    
    # Verifica paths para cada subdomínio
    for subdominio in subdominios:
        url_base = f"http://{subdominio}.{alvo}"
        verificar_paths(url_base, subdominio)

def verificar_paths(url_base, subdominio):
    paths = []

    # Lê o arquivo e armazena os caminhos
    try:
        with open('paths.txt', 'r') as file:
            for linha in file:
                paths.append(linha.strip())
    except FileNotFoundError:
        print("Erro: Arquivo 'paths.txt' não encontrado.")
        return

    subdominio_com_resultados = False
    # Realiza as requisições GET nos paths e exibe apenas os status codes 200
    for path in paths:
        url = f"{url_base}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if not subdominio_com_resultados:
                    print(f"Subdomínio: {subdominio}.{alvo}")
                    subdominio_com_resultados = True
                print(f"  Path: {url}")
        except requests.exceptions.RequestException:
            # Ignora todos os erros e continua
            pass

# Exemplo de uso
verificar_subdominios()

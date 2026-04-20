#--------------------- meu codigo -------------------------------------------
import requests


def buscar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao buscar dados da API")
        return []
    

def filtrar_usuarios(usuarios):
    lista = []
    for usuario in usuarios:
        email = usuario["email"].lower()
        nome = usuario["name"]
        if "biz" in email:
            json = {
              "title": "Contato importante",
              "body": "Usuário com email corporativo",
              "userId": usuario["id"]
            }
            print(nome)
            publicar_usuarios(json)

        

def publicar_usuarios(json):
    url = "https://jsonplaceholder.typicode.com/posts"
    resposta = requests.post(url, json)
    print(resposta.status_code)


usuarios = buscar_usuarios()
filtrar_usuarios(usuarios)

# ------------------------ codigo chat --------------------------------------------------

import requests


# Busca usuários da API
def buscar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao buscar dados da API")
        return []


# Filtra usuários com "biz" no email
def filtrar_usuarios_biz(usuarios):
    filtrados = []

    for usuario in usuarios:
        email = usuario["email"].lower()

        if "biz" in email:
            filtrados.append(usuario)

    return filtrados


# Envia POST para cada usuário
def publicar_usuarios(usuarios):
    url = "https://jsonplaceholder.typicode.com/posts"

    for usuario in usuarios:
        payload = {
            "title": "Contato importante",
            "body": "Usuário com email corporativo",
            "userId": usuario["id"]
        }

        resposta = requests.post(url, json=payload)

        print(f'{usuario["name"]} -> {resposta.status_code}')


# Fluxo principal
if __name__ == "__main__":
    usuarios = buscar_usuarios()
    usuarios_filtrados = filtrar_usuarios_biz(usuarios)
    publicar_usuarios(usuarios_filtrados)
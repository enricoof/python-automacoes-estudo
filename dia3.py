# import requests

# url = "https://jsonplaceholder.typicode.com/users"
# json_string = requests.get(url)
# dados = json_string.json()

# def filtro(dados):
#     lista = []
#     for dado in dados:
#         email = dado["email"]
#         nome = dado["name"]
#         if "biz" in email:
#             lista.append(nome)
        
#     return lista


# if __name__ == "__main__":
#     resultado = filtro(dados)
#     print(resultado)

#------------------------------------------------------------------------------------------

import requests

# Função responsável por buscar dados da API
def buscar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    
    resposta = requests.get(url)

    # Verifica se a requisição deu certo (status 200)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao buscar dados da API")
        return []


# Função responsável por filtrar emails com "biz"
def filtrar_emails_biz(usuarios):
    lista = []

    for usuario in usuarios:
        email = usuario["email"]
        nome = usuario["name"]

        if "biz" in email:
            lista.append(nome)
    
    return lista


# Ponto de entrada do programa
if __name__ == "__main__":
    usuarios = buscar_usuarios()
    resultado = filtrar_emails_biz(usuarios)

    print(resultado)
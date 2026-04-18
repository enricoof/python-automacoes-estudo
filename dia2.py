# Como usar isso pra estudar

# Quando você bater o olho nesse código, tenta sempre pensar:

# “o que essa função recebe?”
# “o que ela retorna?”
# “eu conseguiria reaproveitar isso em outro projeto?”


usuarios = [
    {"nome": "Enrico", "idade": 17},
    {"nome": "João", "idade": 22},
    {"nome": "Maria", "idade": 19}
]

# Função responsável por filtrar apenas usuários maiores de idade
# Boa prática: usar nomes descritivos deixa o código mais fácil de entender
def filtrar_maiores_de_idade(usuarios):
    maiores = []

    # Percorre cada usuário da lista
    for usuario in usuarios:

        # Verifica se a idade é maior ou igual a 18
        if usuario["idade"] >= 18:

            # Adiciona apenas o nome na lista de resultado
            # append é usado para adicionar o elemeto do parametro dentro do valor antes do append
            maiores.append(usuario["nome"])
        
    # Retorna a lista final (melhor que usar print dentro da função)
    return maiores


# Esse bloco garante que o código só será executado quando rodarmos esse arquivo diretamente
# (e não quando ele for importado em outro arquivo)
if __name__ == "__main__":
    resultado = filtrar_maiores_de_idade(usuarios)
    print(resultado)


# -----------------------------
# Versão mais avançada (Pythonica)
# -----------------------------
# Essa versão faz a mesma coisa, mas de forma mais compacta usando list comprehension
# Você ainda não precisa dominar isso, mas é bom começar a reconhecer
def filtrar_maiores_de_idade_v2(usuarios):
    return [u["nome"] for u in usuarios if u["idade"] >= 18]
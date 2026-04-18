# nome = "Enrico"
# idade = 25
# ativo = True

# usuarios = ["João", "Maria", "Pedro"]
# print(usuarios[0])  # João

# usuario = {
#     "nome": "Enrico",
#     "idade": 25,
#     "ativo": True
# }

# print(usuario["nome"])

# for nome in usuarios:
#     print(nome)

# idade = 18

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

# usuarios = [
#     {"nome": "João", "idade": 17},
#     {"nome": "Maria", "idade": 22},
#     {"nome": "Pedro", "idade": 19}
# ]

# for usuario in usuarios:
#     if usuario["idade"] >= 18:
#         print(usuario["nome"])

# --------------------------------------------------------------------------------------


usuarios = [
    {"nome": "Enrico", "ativo": True},
    {"nome": "João", "ativo": False},
    {"nome": "Maria", "ativo": True}
]

for usuario in usuarios:
    if usuario["ativo"]:
        print(usuario["nome"])

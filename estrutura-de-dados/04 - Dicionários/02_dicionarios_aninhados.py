contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

emails = {
    "adailton.junior@ucsal.edu.br": {"nome": "jr", "matricula": 200512, "nascimento": "29/06/2004"},
    "adailtonpenga2019@gmail.com": {"assinatura": "disney+", "jogo": "fifa", "apelido": "jota"}
}

brasileirao = {
    "times": [
    {"nome": "Corinthians", "posicao": 10, "cor": "P&B"},
    {"nome": "Flamengo", "posicao": 1, "cor": "Rubro-Negro"},
    ]
}

print(brasileirao["times"][0]["nome"])

for dados in contatos.values():
    print(dados["nome"])
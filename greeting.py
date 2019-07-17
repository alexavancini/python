name_for_userid = {
    1: "Alex",
    2: "Joao",
    3: "Pedro",
}

def greeting(userid):
    return "Ola %s!" % name_for_userid.get(userid, "Cadastro nao encontrado")

print ("O que deseja fazer?")
print ("1 - Checar os dados de um usuario ja cadastrado")
print ("2 - Registrar um novo usuario")
print ("3 - Sair")
acao =  input("O que deseja?")

if acao  == 1:
    jacadastrado = greeting(input("Digite o codigo do usuario"))
    print(jacadastrado)

elif acao == 2:
    codigo = input ("Digite o codigo do novo usuario: ")
    nome   = raw_input ("Digite o nome do novo usuario:")
    name_for_userid[codigo] = nome
    print("Novo usuario inserido!")

elif acao == 3:
    print ("Saindo!")
    exit

else:
    print ("Acao Invalida")

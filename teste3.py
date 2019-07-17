import numpy as np

NOME_DO_ARQUIVO = "pessoas.npy"

name_for_userid = {}

def input_codigo():
    while True:
        cod_user = input("Digite o codigo do usuario: ")
        try:
        	return int(cod_user)
        except:
            resposta = input("Gostaria de tentar novamente, ou encerrar execucao? [S = Tentar novamente / N = Encerrar a secao]")
            if resposta.upper() != "S":
                exit()

try:
  name_for_userid = np.load(NOME_DO_ARQUIVO).item()
except: pass

#def greeting(userid):
#    return "Ola %s!" % name_for_userid.get(userid, "Cadastro nao encontrado")

print ("O que deseja fazer?")
print ("1 - Checar os dados de um usuario ja cadastrado")
print ("2 - Registrar um novo usuario")
print ("3 - Sair")

acao = input ("O que deseja? ")

if acao == "1":
    codigo = input_codigo()
    print(name_for_userid.get(codigo, "Não encontrado!"))

elif acao == "2":
    codigo = input_codigo()
    nome   = input ("Digite o nome do novo usuario:")
    name_for_userid[codigo] = nome
    print("Novo usuario inserido!")
# A cada insercao ele salva no arquivo o ultimo estado
    np.save(NOME_DO_ARQUIVO, name_for_userid)

elif acao == 3:
    print ("Saindo!")
    exit

else:
    print ("Acao Invalida")

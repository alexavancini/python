import numpy as np

NOME_DO_ARQUIVO = "pessoas.npy"

name_for_userid = {}

try:
  name_for_userid = np.load(NOME_DO_ARQUIVO)
except: pass

def greeting(userid):
    return "Ola %s!" % name_for_userid.get(userid, "Cadastro nao encontrado")

print ("O que deseja fazer?")
print ("1 - Checar os dados de um usuario ja cadastrado")
print ("2 - Registrar um novo usuario")
print ("3 - Sair")
acao =  input("O que deseja?")

if acao  == 1:
    print ('digite o codigo do usuario que deseja consultar')
    print(name_for_userid)

elif acao == 2:
    codigo = input ("Digite o codigo do novo usuario: ")
    nome   = raw_input ("Digite o nome do novo usuario:")
    name_for_userid[codigo] = nome
    print("Novo usuario inserido!")
# A cada insercao ele salva no arquivo o ultimo estado
    np.save(NOME_DO_ARQUIVO, name_for_userid)

elif acao == 3:
    print ("Saindo!")
    exit

else:
    print ("Acao Invalida")

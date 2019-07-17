import time
import timeit


def alguma_funcao():
    for i in range(1, 10):
        time.sleep(1)

inicio = timeit.default_timer()
alguma_funcao()
fim = timeit.default_timer()
print('prolongando a duracao do codigo')
#a=10
#b=20
#resultado=a+b
print ('duracao: %f' % (fim - inicio))

import collections as col

Empregado = col.namedtuple('Empregado', ['name', 'city', 'salary'])

e1 = Empregado('Alex', 'Itapira', '2000')
e2 = Empregado('Alex', 'Mogi Mirim', '900')

print('O nome e salario do e1 e: ' + e1[0] + ' e seu salario: ' + e1[2])
print('A cidade de e2 e: ' + e2[1])

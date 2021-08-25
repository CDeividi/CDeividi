x=0
nota =0
soma=0
while(x < 5 ):
    nota = float(input('Insira a nota {} no sistema:  '.format(x+1)))
    nota += nota
    x += 1
print('Média das notas é de {}'.format(nota/x))

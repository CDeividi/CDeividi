

mochila = ['cama','mesa','televisão','sofa']
print(mochila)
mochila[0] = 'teste'  #modifica um item indice 0
print(mochila)

#metodo adiciona valor metodo .append no final
mochila.append('cadeira')
print(mochila)

mochila.insert(1,'geladeita')
print(mochila)

del mochila[1]
print(mochila)

mochila.remove('sofa')
print(mochila)



x=[5,7,9,11]
y=x
print(x)
print('\n\n\n\n\n\n'.format(y))  #referência de memória reflexo de lista X

#cópia da lista
x=[5,7,11,9]
y = x[:]
print(x)
print(y)

print(mochila[3][5])

#imprimir caracter por caracter

for item in mochila:
    for letra in item:
        print(letra,end='')
    print()

#impressão usando o range
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j] , end='')
    print()

#lista dentro de listas
sacola = [['celola',0.39],['tomate',2.5],['maça',0.89]]
print(sacola[0])

print('-'*50,'Seja bem vindo!','-'*50)
print('-'*50,'Ao nosso supermercado','-'*50)
print('******   selecione sua lista de compras  *********')


carrinho=[]
pedido=[]


for p in range(0,5,1):
      carrinho[p][p][p].append =input('teste')

print(carrinho)


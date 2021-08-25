

carrinho = []
pedido = []

for i in range(1,3,1):
    carrinho.append(input('Produto:\n '))
    carrinho.append(float(input('Valor produto:\n ')))
    carrinho.append(int(input('QTDE:\n ')))

pedido = carrinho[:]
carrinho.clear()
print(pedido)


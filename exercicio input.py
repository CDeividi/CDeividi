preco = float(input('Informe o preço do produto:'))
desc = float(input('Informe o percentual de desconto:'))
perc = desc/100
desctotal = preco * perc
precodesc = preco-desctotal
print('Preço original R${} , desconto {}% , Preço liquido: R${}'.format(preco,desc,precodesc))

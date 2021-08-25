maca = 2.30
laranja = 3.60
banana = 1.85
qtde =0

print('Menu de opções de compra:')
print('Digite o número da opção :')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

opcao = int(input())

if(opcao == 1):
     print('Sua opção foi maças')
     qtde = float(input('Informe a quantidade desejada :'))
     print('A quantidade  total de maças é de {} , e valor  total é R$: {}'.format(qtde,maca * qtde))

elif(opcao == 2):
     print('Sua opção foi laranjas')
     qtde = float(input('Informe a quantidade desejada :'))
     print('A quantidade  total de Laranjas é de {} , e valor  total é R$: {}'.format(qtde, laranja * qtde))

elif(opcao == 3):
     print('Sua opção foi bananas')
     qtde = float(input('Informe a quantidade desejada :'))
     print('A quantidade  total de maças é de {} , e valor  total é R$: {}'.format(qtde, banana * qtde))


else:
  # (opcao != 1 and opcao != 2 and opcao != 3 ):
     print('Sua opção foi inválida')
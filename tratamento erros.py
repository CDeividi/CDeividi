

while(True):
    try:
        x=int(input('Digite um numero inteiro:  '))
        break
    except ValueError:
        print('Numero invalido ,tente novamente!')


while(True):
        try:
                codigo=int(input('Insira o código que deseja emitir digito verificador: \n'))

        except ValueError:
                print('São válidos somente números inteiros !')
                continue
        if(codigo < 10000 or codigo > 30000):
            print('Suportado apenas valores inteiros menores de 10000 e maiores de 30000')
            continue




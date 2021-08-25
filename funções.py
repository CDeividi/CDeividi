

def validacao(n, min, max):
    comp = len( n )
    if (comp <= min or comp >= max):
        valida = False
    else:
        valida = True
    return(valida)


st= input('Insira a string:  ')
valida =validacao(st,5,10)
print('String válida {} '.format(valida))



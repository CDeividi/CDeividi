
def soma(*num):
    soma=0
    print('Trupla: {} '.format(num))
    for i in num:
        soma += i
    return soma

    #programa principal
print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,4,7,10,)))

def validacaoInteiro(codigo): #Função para validação de número inteiro
    try:                      #tratamento do erro em caso de valores reais ou flutiantes
        codNum = int(codigo)   # tenta inserir e converter de uma string em uma variável inteira
        validacao = True        #se possivel valida a operação através da variável validação = True
    except ValueError:          # Em caso de erro
        print( 'Sómento são aceitos códigos com números naturais .' )  #Envia a mensagen descrita
        validacao = False       #e a variável validacao fica en estado falso

    return validacao   #retorno do resultado da validação se é número inteiro para o programa principal


def validacaoRange(codigo):   #função para validar o intervalo do código inserido
    cod_Int = int(codigo)     #insere e converte a string código para variável cod_Int

    if(cod_Int >= 10000 and cod_Int <= 30000):#Compara se o intervalo está entre 10000 e 30000
        validacao = True  #se intevalo está ok a variável validacao = True
    else:
        validacao = False #se não ok a variável validacao = False

    return validacao   #retorno do resultado da validação para o programa principal

def processamento(digito,codigo):  #Função de formatação do processamento para saída
    print('O segue o código com dígito: {} - {}\n\n'.format(codigo,digito)) #sai com os resultados processados formatados
    print('#'* 50)
############### main program ###############

while(True): # loop do programa principal

    #iniciando as variáveis usadas
    val_range = False
    val_inteiro = False
    z = 2
    digito = 0

    #####Interface usuário onde solicita a inserção do código para o usuário
    codigo = input('Por favor insira o código para geração do dígito:\n')

     #chama a função para validação se código  é número inteiro
    val_inteiro = validacaoInteiro(codigo)

     ####condicional se código é inteiro avança para proxima validação
    if(val_inteiro == True):
        ## se código é inteiro válido chama função par validar o range de 10000 à 30000
        val_range = validacaoRange(codigo)

        ##condicional que verifica se o range é válido
        if(val_range ==True):
            ##inicio da extração dos dados
            for i in range(0,len(codigo),1): #separa indice a indice da string codigo
                x = int(codigo[i]) #converte os indices da string codigo em inteiros e insere o valor em x
                digito += x * z #multiplica cada valor da mantissa x por z que inicia em igual a 2 e insere em digito
                z += 1          #incrementa valor de z para incrementar o peso do multiplicador da mantissa
                digito =(digito % 7) #extrai o resto da divisão por 7 o somatório do digito

            #ao final do processamento da extração do dígito chama a função para saida dos dados formatados
            processamento(digito,codigo)

        #caso o range não se enquadre nos limites informa aos usuários que o código não tem valor válido
        else:
            print('Insira valores entre 10000 e 30000:\n')
            print('Código inválido')

    else:
        print('Código invalido') #Reforço mensagem para codigo invalido




























def numAlunos():                               #função para tratamento de erros na inserção do numero de alunos
    global nAlunos                             #variavel global para retorno do número de alunos
    try:                                       #tenta inserir entrada de númeri inteiro
        nAlunos = int(input('Insira a quantidade de alunos que deseja avaliar:\n'))  #insere entrada de numero de alunos na variável nAlunos
        if(nAlunos == '' or nAlunos <= 0):       #se usuário iserir valor nulo ou menor que zero, chama novamente a função para repetilção da operação
            numAlunos()                           #chamamento da função
        else:                                    #se valor estiver ok
            return nAlunos                       #retorna o numero de alunos para programa principal

    except ValueError:                            #em caso de nçao ser um número , ou não for inteiro o numero inserido
        print('Somente serão aceitos números naturais!')   #avisa usuário quais são os critérios para inserir o dado
        nAlunos = numAlunos()



def valN1():                        # função para tratamento de erros da nota N1
    global n1                       # variável global de n1

    try:                            #tenta inserir valor float em n1

            n1=float(input ('Insira a nota 1 do aluno:\n'))     # inserção aguardo dado usuário
            if(n1 == '' or  n1 < 0 or n1 > 10):                 # verifica se dado digitado pelo usuário está nulo ou menor que 0 ou maior que 10
               valN1()                                          # se estiver cham a função novamente pois os dados estão inválidos
            else:                                               # se dados ok
                return n1                                       # segue para retorno de n1 para programa principal
    except ValueError:                                          # em caso erro na inserção do dado na memória
            print ('Insira somente números neste campo')        # avisa os critérios para usuário
            n1=valN1()                                          # chama a função novamente

def valN2():                                                   # função para tratamento de erros da nota N2
    global n2                                                  # variável global de n2
    try:                                                       # tenta inserir valor float em n2
            n2=float (input ('Insira a nota 2 do aluno:\n'))   # inserção aguardo dado usuário
            if(n2 == '' or  n1 < 0 or n1 > 10):                # verifica se dado digitado pelo usuário está nulo ou menor que 0 ou maior que 10
                valN2()                                        # chama a função novamente
            else:                                              # se dados ok
               return n2                                       # segue para retorno de n2 para programa principal
    except ValueError:                                         # em caso erro na inserção do dado na memória
            print ('Insira somente números neste campo')       # avisa os critérios para usuário
            n2=valN2 ()                                        # chama a função novamente

def valN3():                                                   # função para tratamento de erros da nota N3
    global n3                                                  # variável global de n3
    try:                                                       # tenta inserir valor float em n3

            n3=float (input ('Insira a nota 3 do aluno:\n'))   # inserção aguardo dado usuário
            if(n3 == '' or  n1 < 0 or n1 > 10):                # verifica se dado digitado pelo usuário está nulo ou menor que 0 ou maior que 10
                valN3()                                        # chama a função novamente
            else:                                              # se dados ok
                return n3                                      # segue para retorno de n3 para programa principal
    except ValueError:                                         # em caso erro na inserção do dado na memória
            print ('Insira somente números neste campo')       # avisa os critérios para usuário
            n3=valN3()                                         # chama a função novamente

def valN4():                                                     # função para tratamento de erros da nota N4
    global n4                                                    # variável global de n4
    try:                                                         # tenta inserir valor float em n4

            n4=float (input ('Insira a nota 4 do aluno:\n'))    # inserção aguardo dado usuário
            if(n4 == '' or  n1 < 0 or n1 > 10):                 # verifica se dado digitado pelo usuário está nulo ou menor que 0 ou maior que 10
                valN4()                                         # chama a função novamente
            else:                                               # se dados ok
                return n4                                       # segue para retorno de n4 para programa principal
    except ValueError:                                          # em caso erro na inserção do dado na memória
            print ('Insira somente números neste campo')        # avisa os critérios para usuário
            n4=valN4()                                          # chama a função novamente





alunoList = []         #cria uma lista vazia
aluno= {'Nome Aluno':'','n1':'','n2':'','n3':'','n4':'','med':'','Resultado':''} #cria dicionario e suas chaves

global nAlunos         #cria variável global nAlunos
nAlunos = 0            #inicia a variável em zero

nome = ''              #inicia variável nome vazia
global n1              #cria variável global n1
n1=-1                  #inicia a variavel em -1 para futura condicional para forçar usuário a inserir valor
global n2              #cria global n2
n2=-1                  #inicia a variavel em -1 para futura condicional para forçar usuário a inserir valor
global n3               #cria global n3
n3=-1                  #inicia a variavel em -1 para futura condicional para forçar usuário a inserir valor
global n4               #cria global n4
n4=-1                  #inicia a variavel em -1 para futura condicional para forçar usuário a inserir valor

numAlunos()  #chama função para tratamento da entrada do número de alunos

if(nAlunos == None):        # garantia se o retorno falhar chama a função de tratamento de entrada de alunos novamente
    nAlunos = numAlunos()



for i in range(0,nAlunos,1):   # com a variável nAlunos ok feito um for que terá um loop conforme quantidade de alunos

    while(nome == ''):         # força usuário a inserir algo na variável
        nome = input('Insira o nome do alunos {}:\n'.format(i+1))    #insere na variável os dados digitados

    n1=valN1()                    #chama função de tratamento para inserção da nota 1
    if(n1 == None):            #se o retorno do tratamento for nulo ou vazio , chama a função novamente
        n1=valN1 ()            #chamamento da função de tratamento

    n2 = valN2()                #chama função de tratamento para inserção da nota 2
    if(n2== None):              #se o retorno do tratamento for nulo ou vazio , chama a função novamente
        n2 = valN2()            #chamamento da função de tratamento

    n3=valN3 ()                 # chama função de tratamento para inserção da nota 3
    if (n3 == None):            # se o retorno do tratamento for nulo ou vazio , chama a função novamente
        n3=valN3 ()             # chamamento da função de tratamento

    n4=valN4 ()                  # chama função de tratamento para inserção da nota 4
    if (n4 == None):             # se o retorno do tratamento for nulo ou vazio , chama a função novamente
        n4=valN4 ()              # chamamento da função de tratamento

    media = (n1 + n2 + n3 + n4) / 4 # calcula e inseri a média da 4 notas na variável média

    if(media >= 7.0 ):             #condicional se média maior ou igual a 7
          result = 'Aprovado'      #atualiza variável result com 'Aprovado'
    else:                          # se não
          result = 'Reprovado'     # a tualiza a variável result com Reprovado


    aluno['Nome Aluno'] = nome    #Insere a variável nome na chave nome aluno do dicionario aluno
    aluno['n1'] = n1              # insere a variável n1 na chave n1  no dicionário aluno
    aluno['n2'] = n2              # insere a variável n2 na chave n1  no dicionário aluno
    aluno['n3'] = n3              # insere a variável n3 na chave n1  no dicionário aluno
    aluno['n4'] = n4              # insere a variável n4 na chave n1  no dicionário aluno
    aluno['med'] = media          # insere a variável media na chave media  no dicionário aluno
    aluno['Resultado'] = result   # insere a variável result na chave resultado  no dicionário aluno

    alunoList.extend (aluno.items ())  #adiciona o dicionario aluno na lista alunoList

    nome = ''                     #esvazia variável nome para impedir usuário de inserir nome vazio do aluno
print('Notas Alunos:\n')           #imprime 'Notas dos alunos na tela

z = 100                           #variável z inicia com 100 , variável para captar o menor comprimento de nome aluno la lista
y = 0                             # variável criada para captar o maior nome de aluno da lista para alinhamento cabeçario

for a in range(0,(nAlunos * 7) - 6,7): #loop for para varrer nome de alunos da lista aluinolist
        x = len(alunoList[a][1])       #vai inserindo em 'x' o comprimento dos nomes alunos
        if (x > y):                    # se o nome do prximo for maior que o ultimo
                y=x                    # armazena o maior comprimento em 'y'

for a in range (0, (nAlunos * 7) - 6, 7): # loop for para varrer os dados da alunoList
        x=len (alunoList[a][1])           #detecta comprimento dos nomes alunos para alinhamento dos dados com cabeçario
        if (x < z):                       #se comprimento do proximo for maior que o ultimo
                z=x                       #então armazena comprimento
        k = y - x + 3                     #formula para determinar o comprimento do campo nome aluno cabeçario relatório
                                          #comprimento do maior menos o menor + 3 espaõs vazios

        if(a == 0 ):                      #condicional para imprimir cabeçario soimente uma vez
                k = y - 4 + 5             #formula para alinhamento  do cabeçario
                print('Relatório')        #Imprime na tela 'Relatórios'
                print ('Nome', ' ' * k, '| NOTA 1 | NOTA 2 | NOTA 3 | NOTA 4 | MÉDIA | RESULTADO') #imprime o cabeçario#

        k=y - x + 3                        #desfaz a fórmula que foi usada para alinhamento do cabeçario
        print(alunoList[a][1], ' '  *  k ,'  | ',alunoList[a+1][1],                         ########## imprime os dados da lista.
        '  | ',alunoList[a+2][1],'  | ',alunoList[a+3][1],'  | ',alunoList[a+4][1],
        '  | ',alunoList[a+5][1],' | ',alunoList[a+6][1])








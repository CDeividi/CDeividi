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



def valN():                        # função para tratamento de erros da nota N
    global n                       # variável global de n

    try:                            #tenta inserir valor float em n

            n=float(input ('Insira a nota 1 do aluno:\n'))     # inserção aguardo dado usuário
            if(n == '' or  n < 0 or n > 10):                 # verifica se dado digitado pelo usuário está nulo ou menor que 0 ou maior que 10
               valN()                                          # se estiver cham a função novamente pois os dados estão inválidos
            else:                                               # se dados ok
                return n                                       # segue para retorno de n1 para programa principal
    except ValueError:                                          # em caso erro na inserção do dado na memória
            print ('Insira somente números neste campo')        # avisa os critérios para usuário
            n=valN()                                          # chama a função novamente


alunoList = []         #cria uma lista vazia
aluno= {'Nome Aluno':'','n1':'','n2':'','n3':'','n4':'','med':'','Resultado':''} #cria dicionario e suas chaves

global nAlunos         #cria variável global nAlunos
nAlunos = 0            #inicia a variável em zero
global n
n=0
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

    n1 =valN()                    #chama função de tratamento para inserção da nota 1
    if(n == None):            #se o retorno do tratamento for nulo ou vazio , chama a função novamente
        n1=valN ()            #chamamento da função de tratamento

    n2=valN()
    if(n== None):
        n2 = valN()
    n3=valN3()
    if(n == None):
        n3 = valN()
    n4=valN4()
    if(n==None):
        n4 = valN()


    media = (n1 + n2 + n3 + n4) / 4

    if(media >= 7.0 ):
          result = 'Aprovado'
    else:
          result = 'Reprovado'


    aluno['Nome Aluno'] = nome
    aluno['n1'] = n1
    aluno['n2'] = n2
    aluno['n3'] = n3
    aluno['n4'] = n4
    aluno['med'] = media
    aluno['Resultado'] = result

    alunoList.extend (aluno.items ())

    nome = ''
print('Notas Alunos:\n')

z = 100
y = 0

for a in range(0,(nAlunos * 7) - 6,7):
        x = len(alunoList[a][1])
        if (x > y):
                y=x
        if (x < z):
                z = x
        k = ((y - x) * 3)-2



for a in range (0, (nAlunos * 7) - 6, 7):
        x=len (alunoList[a][1])
        if (x < z):
                z=x
        k = y - x + 3

        if(a == 0 ):
                k = y - 4 + 5
                print('Relatório')
                print ('Nome', ' ' * k, '| NOTA 1 | NOTA 2 | NOTA 3 | NOTA 4 | MÉDIA | RESULTADO')

        k=y - x + 3
        print(alunoList[a][1], ' '  *  k ,'  | ',alunoList[a+1][1],
        '  | ',alunoList[a+2][1],'  | ',alunoList[a+3][1],'  | ',alunoList[a+4][1],
        '  | ',alunoList[a+5][1],' | ',alunoList[a+6][1])




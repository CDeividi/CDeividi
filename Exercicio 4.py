from pprint import pprint  #importa biblioteca pprint que fatia um dicionario ou lista na impressão
def valIdade():                                                      #função de validação da idade
    try:                                                             #tratamento erro para entrada válida numérica inteira
        idade = int(input('Insira a idade do contato:\n'))           #aguarda entrada da idade pelo usuário
        if(idade == '' or idade < 0 or idade > 100):                 #verifica se a idade está vazia , ou maior que 100 ou menor que zero
           idade= valIdade()                                         #se qualquer uma das opção acima chama a função novamente
        else:                                                        #se o dado idade estiver dentro dos critérios retorna a idade
            return idade

    except ValueError:                                               #se houver um erro de valor inválido
        print('Insira uma idade válida')                             #avisa usuário e chama função de validação novamente
        idade = valIdade()



contato = {'nome':'','idade':'','telefone':'' }                      #cria dicionário chamado contato
auxNome=[]                                                           #cria uma lista auxiliar para nomes alfabéticos
agendaAlf={}                                                         #cria dicionário para acumolo agenda alfabética
agenda = []                                                          #cria uma lista de agenda vazia
agenda_Alf = []                                                      #cria uma lista agenda_Alf vazia
contatoMenores={}                                                    #cria um dicionário para contatoMenores
agendaMenores=[]                                                     #Cria uma lista agenda para menores
contatoMaiores={}                                                    # Cria um dicionário para os maiores
agendaMaiores=[]                                                     #cria uma lista para os maiores

#****************************** programa principal

while(True):                                                         #loop para a seguència do programa
    nome = input('Insira  o nome do contato:\n')                     #Aguara a entrada do nome do contato pelo usuário
    if (nome == ''):                                                 #verifica se a string está vazia
        print('Programa encerrado!')                                 #se estiver avisa , programa encerrado e encerra o loop e termina a execução
        break                                                        #parada do loop principal
    else:                                                            #se os dados do nome estã valido segue
        contato['nome'] = nome                                       #transfere o nome digitado  e variável(nome) ,para a chave nome no dicionário contato
        auxNome.append(nome)                                         #transfere a variável nome para lista auxLista
        auxNome.sort()                                               #Organiza os nomes da lista auxNome em ordem alfabética
        idade = valIdade()                                           #chama a função para validação idade
        if(idade == None):                                           #Garantia para se a idade retornar vazia
            idade = valIdade()                                       #chama novamente a validação idade
        contato['idade']=idade                                       #uma vez a idade validada , insere data no dicionário contato na chave (idade)


    contato['telefone'] = input('Insira o número do telefone:\n')    #solicita o numero de telefone do contato ao usuário
    agenda.extend(contato.items())                                   #adiciona o dicionário contato em agenda

    for auxnome in auxNome:                                          #navega na lista auxNome para copiar a seguência alfabética
        for i in range(len(agenda)):                                 #percorre o comprimento da lista agenda na na chave dos campos
            for j in range(0,2,1):                                   #percorre a lista nos valores dos campos
                if(auxnome == agenda[i][j]):                         #procura dentro da lista agenda o nome seguencial da lista auxNome alfabeticamente
                    agendaAlf['nome']=agenda[i][j]                   #uma vez encontrado o nome insere o conjunto de danos no dicionário agendaAlf (nome)
                    agendaAlf['idade']=agenda[i+1][j]                #uma vez encontrado o nome insere o conjunto de danos no dicionário agendaAlf (idade)
                    agendaAlf['telefone']=agenda[i+2][j]             #uma vez encontrado o nome insere o conjunto de danos no dicionário agendaAlf (telefone)
                    agenda_Alf.extend(agendaAlf.items())             #Insere os itens do dicionario agendaAlf na lista agenda_Alf
                    agendaAlf.clear()                                #apara os itens do dicionário agendaAlf para não replicar dados
    print('Agenda em ordem alfabética:\n')                           #mensagem dos contatos em ordem alfabétiva
    pprint (agenda_Alf)                                              #imprime na tela os dados dos contatos em ordem alfabética
                #Código para dividir os contatos maiores de 18 anos e menores de 18 anos****************************
    for k in range(1,len(agenda),3):                                 #Percorre somente o campo idade na lista agenda
        auxIdade = int(agenda[k][1])                                 #insere e converte a inteiro na variável auxIdade o valor da idade
        if(auxIdade < 18):                                           #se a idade for menor que 18
              for m in range(0,2,1):                                 #percorre pels valores dos campos
                    contatoMenores['nome']=agenda[k-1][j]            #insere o nome percorrido no dicionário contatoMenores os dados
                    contatoMenores['idade']=agenda[k][j]             #estão com os indices relacionados ao indice da idade
                    contatoMenores['telefone']=agenda[k + 1][j]      #Insere o valor do campo telefone no dicionário agendaMenores
                    agendaMenores.extend(contatoMenores.items ())    #Adiciona os itens do dicionário contatoMenores na lista agendaMenores
                    contatoMenores.clear()                           #Apaga os dados do dicionário contatoMenores para não replicar
                    break                                            #uma vez inserido conclui-se este loop para evitar replica de dados
        else:
            for m in range (0, 2, 1):                                #se o contato for maior de 18 anos cai neste bloco
                contatoMaiores['nome']=agenda[k - 1][j]              #insere o nome da agenda percorrida no dicionário contatoMaiores na chave (nome)
                contatoMaiores['idade']=agenda[k][j]                 #insere o nome da agenda percorrida no dicionário contatoMaiores na chave (idade)
                contatoMaiores['telefone']=agenda[k + 1][j]          #insere o nome da agenda percorrida no dicionário contatoMaiores na chave (telefone)
                agendaMaiores.extend(contatoMaiores.items ())        #adiciona na lista agendaMaiores o dicionário contatoMaiores
                contatoMaiores.clear ()                              #apaga limpa dicionário contatoMaiores para evitar replicalção dedados
                break                                                #encerra o loop para evitar replicação de dados

    print('Menores de 18 anos:\n***************************')        #informa ao usuário a impressão dos contatos menores de 18 anos
    pprint(agendaMenores)                                            #imprimi na tela os contatos manores de 18 anos
    print ('************************************************')
    print('Maiores de 18 anos:\n***************************')        #informa ao usuário que será impresso a lista de usuário maiores de 18 anos
    pprint(agendaMaiores)                                            #imprime na tela a lista dos contatos maiores de 18 anos
    print('************************************************')        #print para separar os dados impressos
    agendaMaiores.clear()                                            #limpa a lista  agendaMaiores
    agendaMenores.clear()                                            #limpa a lista agendaMenores
    agenda_Alf.clear ()                                              #limpa a lista agenda_Alf , para iniciar a seguència novamente de inserção de novos dados














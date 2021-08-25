from pprint import pprint
contato={}
agenda=[]
nomeLista = []
iD = 1
while(True):

    nome =  input('Insira o nome do do contato:\n ')
    nomeLista.append(nome)
    nomeLista.sort()
    idade = int(input('Insira a idade do contato:\n'))
    telefone = input('Insira o telefone:\n')
    contato['nome'] = nome
    contato['idade']= idade
    contato['telefone'] = telefone


    k=nomeLista.index(nome)

    iD += 1

    agenda.insert(k,contato)
    contato.clear()
    pprint(agenda)
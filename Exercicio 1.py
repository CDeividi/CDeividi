
cadastro = [['Nome fornecido',''],['Peso Fornecido','']]  #lista para armazenamento dos dados Nome e peso

def avaliacao(peso): #função para para enquadramento da categoria com parâmetro float peso
    if(peso <= 65):     #caso menos ou igual a 65 kg
        return 'Pena'   #retorna categoria PENA

    elif(peso >= 65 and peso <72): #caso menor ou igual a 65 kg ou menor que 72 kg
        return 'Leve' #retorna categoria LEVE

    elif(peso >= 72 and peso < 79):  #caso menor ou igual a 72 kg ou menor que 79 kg
        return 'Ligeiro'  #retorna categoria Ligeiro

    elif(peso >= 79 and peso < 86): #caso menor ou igual a 79 kg ou menor que 86 kg
        return 'Meio-médio' #retorna categoria Meio-Médio
    elif(peso >= 86 and peso < 93): #caso menor ou igual a 86 kg ou menor que 93 kg
        return 'Médio' #retorna categoria Médio

    elif(peso >= 93 and peso < 100): #caso menor ou igual a 93 kg ou menor que 100 kg
        return 'Meio-pesado'  #retorna categoria Meio-pesado
    elif(peso >= 100):  #caso maior que 100 kg
        return 'Pesado'  #retorna categoria Pesado

#------------------------------PROGRAMA PRINCIPAL

while(True): #loop ativo
    print('#'*50,'Software para avaliação de categorias dos lutadores','#'*50) #apresentação do software
    print('#'*153) # imprime cerquilha 153 vezes para destacar apresentação
    cadastro[0][1] = input('Nome do Lutador:\n') #solicita e Insere na lista da lista o nome fornecido

    if(cadastro[0][1] == 'sair'): #condicional que monitora se é digitada a palavra sair
        break  #para o loop ao digitar sair

    peso = float(input('Informe o peso do lutador:\n')) #solicita e insere o peso na variável peso
    categoria =    avaliacao(peso) #chama a função avaliacao com parâmetro do float peso e insere retorno
    # na variável categoria
    cadastro[1][1] = categoria #insere categoria na lista da lista cadastro
    #imprime o nome peso e categoria
    print('O lutador {} pesa : {} kg , e se enquadra na categoria : {}'.format((cadastro[0][1]),peso,cadastro[1][1]))
    print('#'*153) #imprime cerquilha 80 vezes para destacar o resultado

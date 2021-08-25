game={'nome':'Super Mario','Desenvolvedora':'Nintendo','ano':1900}
print(game)

print(game['nome'])
print(game['Desenvolvedora'])
print(game['ano'])
print('-'*20)
for i in (game.values()):
        print (i)
print('-'*20)
for i in (game.keys()):
    print(i)
print('-'*20)
for i in (game.items()):
    print(i)

print('-'*20)

for i,j in (game.items()):
    print('{} = {} '.format(i,j))
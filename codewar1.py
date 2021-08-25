multiplos = []
soma =0

def solution(number):
    soma = 0
    for i in range (0, number, 1):
        if (i % 3 == 0 or i % 5 == 0 or i % 9 == 0):
            multiplos.append (i)
            soma += i
    return soma


nun = int(input("Numero:\n"))

print(solution(nun))




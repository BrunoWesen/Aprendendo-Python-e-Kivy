i = int(input("De um número de 2 até 99, qual o número que o algoritmo deve parar? \n"))
for k in range(2, 100):
    print(k)
    if (k == i):
        break

print(list(range(9, 1, -1)))

somapar = 0  # Variável que representa a soma de todos os pares de 0 a 100
for par in range(0, 101, 2):
    somapar += par

else:
    print(somapar)

for primos in range(1, 100):
    if ((
        primos % 2 != 0 and primos % 3 != 0 and primos % 5 != 0 and primos % 7 != 0 and primos % 11 != 0)
        or primos == 2 or primos == 3 or primos == 5 or primos == 7 or primos == 11):
        print(primos)

ui = int(input("Me forneça o número inicial: \n"))
uf = int(input("Me forneça o número final: \n"))
for primos in range (ui, uf, 1):
    if ((
    primos % 2 != 0 and primos % 3 != 0 and primos % 5 != 0 and primos % 7 != 0 and primos % 11 != 0)
    or primos == 2 or primos == 3 or primos == 5 or primos == 7 or primos == 11):
        print(primos)
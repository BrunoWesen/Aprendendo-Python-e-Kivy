
ui = int(input("Me forneça o número inicial: \n"))
uf = int(input("Me forneça o número final: \n"))
ug1 = int(input("Me forneça o primeiro número a ser ignorado \n"))
ug2 = int(input("Me forneça o segundo número a ser ignorado \n"))
ug3 = int(input("Me forneça o terceiro número a ser ignorado \n"))
for primos in range(ui, uf, 1):
    if (((
             primos % 2 != 0 and primos % 3 != 0 and primos % 5 != 0 and primos % 7 != 0 and primos % 11 != 0)
         or primos == 2 or primos == 3 or primos == 5 or primos == 7 or primos == 11) and primos != ug1 and primos != ug2 and primos != ug3):
        print(primos)

""""
x = "f"
while (x != "q"):  # A letra q é a única capaz de finalizar o algoritmo
    print("Estou em looping!")
    x = input("Digite uma letra: \n")
"""
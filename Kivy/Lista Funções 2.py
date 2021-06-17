def inverta(*lista):  # Inverte Listas
    i = (len(lista) * 1) - 1
    invert = []
    while i >= 0:
        invert += lista[i]
        i -= 1
    return invert


lista = ["a", "b", "c", "k"]
print(inverta(*lista))


def fatorial(i):  # Faz o fatorial de um número inteiro não negativo
    if i != int(i):
        print("O número deve ser inteiro e maior que 0")

    else:
        k = i - 1
        while k > 0:
            i *= k
            k -= 1
            if k == 0:
                print(i)
                break
        else:
            print("O número deve ser inteiro e maior que 0")


fatorial(2)

n = float(input("Forneça o número a ser verficado: \n"))

if n > 14 and n < 21:
    print("Está entre o intervalo(de 14 e 21)")

else:
    print("Não está entre o intervalo(de 14 e 21)")


def analisador_de_strings(s):  # Calcula a quantidade de letras em mauisculas e minúsculas que a String possui.
    s = "".join(s.split(" "))
    i = len(s) * -1
    m = 0  # Variável que conta quantas letras maiúsculas existem em uma String
    while i != 0:
        if s[i].isupper():
            m += 1
        i += 1

    print("A quantidade de letras maiúsculas é %i, portanto a quantidade de letras minúsculas é" % m, len(s) - m,
          "\n")


String = input("Digite uma String \n")
analisador_de_strings(String)


def non_repeate_list(lista):  # Retornar a lista sem elementos repetidos
    i = len(lista) * -1
    lista.sort()
    while i < 0:
        ea = lista[i]  # Elemento Atual
        while lista.count(ea) > 1:
            lista.pop(ea)
        i += 1
    return lista


Lista = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 7, 9, 9, 5, 5, 4, 18]

print(non_repeate_list(Lista))

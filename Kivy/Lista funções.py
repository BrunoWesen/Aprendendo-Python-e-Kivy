def estudo(x):
    print("Estamos estudando funções \n")
    print("Função invocada com sucesso!\nO valor passado pelo argumento de x é:", x, "\n")


estudo(322)


def soma(x, y):
    vSoma = x + y  # v antes serve pra diferenciar uma variável de outros objetos.
    print(vSoma)


soma(21, 267)


def media(x=0, y=0, z=0):
    vmedia = (x + y + z) / 3
    lista = [x, y, z]
    lista.sort()
    print("\nNúmeros fornecidos em ordem crescente:\n", lista[0], ",", lista[1], ",", lista[2])
    print("A média entre eles: %.5f\n" % (vmedia))


media(14.7, 2, 36.44)


def func1(x, y):  # f antes serve pra diferenciar uma função de outros objetos.
    def func2(x, y):
        vsoma = x + y
        print(vsoma)

    func2(x, y)


func1(21, 36)


def funcl(lista):
    i = len(lista) * -1
    while (i < 0):
        print(lista[i])
        i += 1


print()

lista = ["A", "B", "C", "d", "e", "f"]
funcl(lista)

print()


def funcdic(A, B, C, d, e, f):
    print("Chave, Valor")
    print("A    ", A)
    print("B    ", B)
    print("C    ", C)
    print("d    ", d)
    print("e    ", e)
    print("f    ", f)


funcdic(**dict(zip((lista), (1, 2, 3, 4, 5, 6))))  # * serve para listas e ** para dicionários

print()


def func(a, b, c, d):
    print(a + b + c + d, "\n")


lista = 1, 2, 3, 4
func(*lista)


def maior(a, b, c):
    lista = [a, b, c]
    lista.sort()
    print(lista[-1])


maior(21, 56, 44)

print()

lsoma = [5, 21, 10, 100, 210, 2341, 31, 5, 61, 4]
lmult = [8, 10]


def soma2(*llista):
    i = len(llista) * -1
    fsoma = 0
    while (i < 0):
        fsoma += llista[i]
        i += 1
    print(fsoma)


soma2(*lsoma)

print()


def mult(*llista):
    i = len(llista) * -1
    mult = 1
    while (i < 0):
        mult *= llista[i]
        i += 1
    print(mult)


mult(*lmult)
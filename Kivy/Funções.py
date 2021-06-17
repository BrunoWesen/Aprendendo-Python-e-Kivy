""""
def minha_func():  # def para definir funções
    print("Fala galera!")

minha_func()
"""

""""
# def soma(x, y):
def soma(x=21, y=15):
    total = x + y
    print("A soma de %i e %i é:" % (x, y), total)

soma()  # Vai puxar o default
soma(20, 14)
soma(y=36)
"""

""""
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {} "
          .format(nome, sobrenome, idade, sexo))

nome = input("Qual o seu nome? \n")
sobrenome = input("E qual o seu sobrenome? \n")
idade = int(input("Qual sua idade? \n"))
sexo = input("E qual o seu sexo? \n")

dados_pessoais(nome,sobrenome,idade,sexo)
"""

""""
def func():
    return 1, 2


a, b = func()
t = (10, 20)  # Tupla
a, b = t  # A quantidade de variáveis a receber os valores de uma tupla/lista
          # devem ser exatamente igual a quantidade de valores da tupla/lista

print(a)
print(b)
"""

""""
def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo

q,c = potencia(10)

print(q)
print(c)
"""


def lista_de_argumentos(*lista):  # * recebe tupla
    print(lista)


def lista_de_argumentos_associativos(**dicionario):  # ** recebe dicionario
    print(dicionario)


lista_de_argumentos(1, 2, 3, 4, 5, 6, 7)
lista_de_argumentos("um", "dois", "três", "quatro")

lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativos(um=1, dois=2, tres=3, quatro=4)

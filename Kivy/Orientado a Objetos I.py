# código: utf-8

# __author__ = Bruno Sevalho Wesen

""""
nomeclatura de classes em python usa-se a camel case
Sem caracteres especias,espaços, primeira "letra com simbolos"
O primeiro caractere precisa estar em Uppercase(letra maiúscula)
exemplos: MinhaCasa(), Sorvete2(),MacacoAmarelo
"""


# class Estudo1():
#     pass
#
# # Criação de instância
# e1 = Estudo1()
# e2 = Estudo1()
#
# print(id(e1))
# print(id(e2))

class A:
    def __init__(self):
        print(id(self))


a = A()
print(id(a))


class Retangulo:
    def __init__(self):
        self.a = 0
        self.l = 0

    def area(self):
        return self.a * self.l


r1 = Retangulo()
r1.l = 10
r1.a = 5

print(r1.area())

""""
ou
class Retangulo:

    def area(self):
        return self.a * self.l

def membros_retangulo(r):
    r.a = 0
    r.l = 0

r1 = Retangulo()
membros_retangulo(r1)
r1.l = 10
r1.a = 5

print(r1.area())
"""


class Retangulo:

    def __init__(self, largura, altura):
        self.a = largura
        self.l = altura

    def area(self):
        return self.a * self.l


r = Retangulo(7, 5)

print(r.area())
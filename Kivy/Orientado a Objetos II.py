# coding: utf-8

__author__ = "Bruno Sevalho Wesen"

""""
class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.set_altura(altura)  # isintance é uma função de comparação
        self.set_largura(largura)  # de uma instância

    def set_altura(self, num):
        try:
            if not (isinstance(num, int) and (num > 0)):
                raise ValueError
        except ValueError:
            print("Altura inválida: {}".format(num))
        finally:
            self._altura = num

    def set_largura(self, num):
        try:
            if not (isinstance(num, int) and (num > 0)):
                raise ValueError
        except ValueError:
            print("Largura inválida: {}".format(num))
        finally:
            self._largura = num

    def get_area(self):
        return self._altura * self._largura


r = Retangulo(largura=100,altura=-4)
print(r.get_area())

"""

# publico=0, _restrito=0 por convenção no python nomes precedidos por underline(_), não
# feitas para uso irrestrito, as próprias IDEs de python reconhece isso
# e nomes com DOIS underlines(__), são conhecidos como nome privados
# Para evitar a colisão de superclasses e subclasses usa se os dois underlines exemplo __colisão=0
# Nomes exclusivos da linguagem exemplo __linguagem__

""""
class Retangulo:
    def __init__(self):
        self._largura = 0
        self._altura = 0

    def _set_altura(self, num):
        try:
            if not (isinstance(num, int) and (num > 0)):
                raise ValueError
        except ValueError:
            print("Altura inválida: {}".format(num))
        finally:
            self._altura = num

    def _set_largura(self, num):
        try:
            if not (isinstance(num, int) and (num > 0)):
                raise ValueError
        except ValueError:
            print("Largura inválida: {}".format(num))

        finally:
            self._largura = num


    # def _get_altura(self):
    #     return self._altura
    #
    # def _get_largura(self):
    #     return self._altura

    def get_area(self):
        return self._altura * self._largura

    VarAluta = property(fset=_set_altura)
    VarLargura = property(fset=_set_largura)


r = Retangulo()
r.VarAluta= int(input("Me forneça a altura\n"))
r.VarLargura = int(input("Me forneça a largura\n"))

print(r.get_area())
"""


# Por convenção não usamos o property do builtins, ultilizamos os Decorators
#
# class A:
#     def __init__(self):
#         self._var = 0
#
#     @property  # Método Get
#     def var(self):
#         print("valor está sendo lido")
#         return self._var
#
#     @var.setter  # Método Set
#     def var(self, x):
#         print("o valor está sendo escrito")
#         self._var = x
#
#
# a = A()
# a.var = 20
# print(a.var)

# Ctrl + R para usar o replace do PyCharm

class Bichos:
    qnt_bichos = 0

    def __init__(self):
        self.add_bicho()

    def __del__(self):
        self.del_bicho()
        if self.qnt_bichos == 0:
            print("Todos os bichos foram mortos!")

    @classmethod
    def add_bicho(cls):
        cls.qnt_bichos += 1

    @classmethod
    def del_bicho(cls):
        cls.qnt_bichos -= 1

    # add_bicho() = classmethod(add_bicho)
    # del_bicho() = classmethod(del_bicho)

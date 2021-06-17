# EXCEÇÕES

# uma exceção com um tratamento
# try :
#     código
# except Erroclass:
#     tratamento

# Múltiplas exceções diferentes tratamentos
# try :
#     código
# except Erroclass1:
#     tratamento
# except Errorclass2:
#     tratamento

# Múltiplas exceções mesmo tratamento
# try:
#     a = 10 / 0
#     print(a)
# except (ZeroDivisionError, NameError):
#     a = "infinito"
#     print("a =",a)

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    a = "infinito"
    print("a =", a)

b = int(input())

try:
    a = 10 / b
    print(a)
except (ZeroDivisionError, ValueError) as e:
    print(type(e))  # Instância da Exceção
    print(e.args)  # Argumentos as mensagens
    print(e)  # __str__ mensagem
else: # else será executado se não houver exeções
    print("Não houve exceção!")

"""
Bloco finally
finally será executado independente das exceções
mesmo quando não houver um except para uma exceção,
antes do programa finalizar com a exceção,
ele rodará o finally
"""

try:
    b = int(input("Segunda aplicação do b\n"))
    a = 10 / b
    print(a)
except (ZeroDivisionError) as e:
    print(type(e))  # Instância da Exceção
    print(e.args)  # Argumentos as mensagens
    print(e)  # __str__ mensagem
else: # else será executado se não houver exeções
    print("Não houve exceção!")
finally:
    print("Sempre será executado")
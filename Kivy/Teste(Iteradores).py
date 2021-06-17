"""""
for c in "Bruno gostoso":   # for com string
    print (c)
"""
""""
range(0, 10, 1)             # (start, stop, step)
x = list(range(0, 10, 1))   # Função range retorna em range, por isso converti em list
print(x)                    # range é parecido com Progressão Aritmética
"""
""""
for i in range(10, 100, 5):
    print(i)
"""
""""
for k in range(100):
    print(k)
    if(k == 54):
        break               # Função break interrompe um laço e economiza memória
"""
""""
print()
print("início da rodada")
f = 0
while(f<10):
    f += 1
    if(f%2==0):
        continue
    if(f>5):
        break
    print(f)
else:
    print("else")
print("fim")
print()
"""
for j in range(100, 2):
    print(j)
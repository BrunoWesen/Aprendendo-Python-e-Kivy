Metros = float(input("Me forneça em metros, o que você deseja converter para centímetros \n"))
print("%.2f metros em centímetros é:" % (Metros), Metros * 100, "centímetros")
print("O quadrado de 7, e o cubo de 9 são respectivamente: \n", 7 ** 2, "e", 9 ** 3)
Numerox = float(input("Me forneça um número: \n"))
Numeroy = float(input("Agora me forneça outro número: \n"))
xy = Numerox / Numeroy
xyy = Numerox // Numeroy
print(
    "A divisão entre o primeiro número e o segundo é: %.3f, e em forma de número inteiro(sem arredondamento) fica: %i" % (
        xy, xyy))
print(
    "Considerando que os dois números foram dado em métros, se fizessem parte da altura e largura, o retângulo possuiria",
    Numeroy * Numerox, "m²")
Dias = int(input("Me forneça a quantidade de dias a ser convertida em segundos \n"))
Horas = int(input("Me forneça a quantidade de horas a ser convertida em segundos \n"))
Minutos = int(input("Me forneça a quantidade de minutos a ser convertida em segundos \n"))
Segundos = int(input("Me forneça a quantidade de segundos \n"))
Diass = Dias * 86400  # Variáveis com ss no final são convertidas em segundos
Horass = Horas * 3600
Minutoss = Minutos * 60
Totalss = Diass + Horass + Minutoss + Segundos  # Variáveis com ss estão em segundos
print("%i dia(s), %i hora(s), %i minuto(s) e %i segundos totalizam %i segundos." % (
    Dias, Horas, Minutos, Segundos, Totalss))
Valor = float(input("Qual o valor da compra? \n R$ "))
print("Valor sem desconto: R$ %.2f , Valor com desconto: R$" % (Valor), Valor - (Valor * 0.1))
numero1 = 0
operacao = " "
numero2 = 0
resultado = 0

numero1 = int(input ("Digite o numero1: "))
operacao = input ("Digite a operacao: ")
numero2 = int(input ("Digite o numero2:"))

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "/":
    resultado = numero1 / numero2
elif operacao == "*":
    resultado = numero1 * numero2
else:
    resultado = "Operação Invalida"

print(str(numero1) + " " + str(operacao) + " " + str(numero2) + " = " + str(resultado))
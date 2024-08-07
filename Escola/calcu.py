print("=" * 15, "Bem-vindo a calculadora", "=" * 15)
print("Por favor selecione sua operação \n"
      "[1] Soma \n"
      "[2] Subtração \n"
      "[3] Multiplica \n"
      "[4] Divisão")
print("=" * 55)

escolha = int(input("--> "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = 0

if escolha == 1:
    print("=" * 55)
    resultado = num1 + num2
    print("{} + {} = {}".format(num1, num2, resultado))
elif escolha == 2:
    print("=" * 55)
    resultado = num1 - num2
    print("{} - {} = {}".format(num1, num2, resultado))
elif escolha == 3:
    print("=" * 55)
    resultado = num1 * num2
    print("{} * {} = {}".format(num1, num2, resultado))
elif escolha == 4:
    print("=" * 55)
    resultado = num1 / num2
    print("{} / {} = {}".format(num1, num2, resultado))
else:
    print("=" * 55)
    print("Operação invalida")

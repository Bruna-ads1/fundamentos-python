# Mini Projeto: Calculadora Simples

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {a + b}")
elif op == "-":
    print(f"Resultado: {a - b}")
elif op == "*":
    print(f"Resultado: {a * b}")
elif op == "/":
    print(f"Resultado: {a / b}")
else:
    print("Operação inválida")

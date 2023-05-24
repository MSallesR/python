numero1 = float(input("coloque o numero---> "))

op = input("operação---> ")

numero2 = float(input("coloque o numero---> "))

if op == "+":
    print(f"O calculo: {numero1} + {numero2} = {numero1 + numero2}")

elif op == "-":
    print(f"O calculo: {numero1} - {numero2} = {numero1 - numero2}")

elif op == "/":
    print(f"O calculo: {numero1} / {numero2} = {numero1 / numero2}")

elif op == "*":
    print(f"O calculo: {numero1} * {numero2} = {numero1 * numero2}")

elif op == "**":
    print(f"O calculo: {numero1} ** {numero2} = {numero1 ** numero2}")

elif op == "%":
    print(f"O calculo: {numero1} % {numero2} = {numero1 % numero2}")

elif op == "//":
    print(f"O calculo: {numero1} // {numero2} = {numero1 // numero2}")
else:
    print("Favor inserir uma operação válida.")
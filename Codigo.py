import Calculadora

def esnumero(candidato):
    valido = True
    for caracter in candidato:
        if caracter in '0123456789':
            continue
        else:
            valido = False
            break
    return valido


print("Bienvenido a la calculadora")
operacion = input("Indique la operación (+, -, *, /): ")
oper1 = input("Indique el primer número: ")
oper2 = input("Indique el segundo número: ")
if esnumero(oper1) and esnumero(oper2):
    oper1 = int(oper1)
    oper2 = int(oper2)
    if operacion == "+":
        print(Calculadora.suma(oper1, oper2))
    elif operacion == "-":
        print(Calculadora.resta(oper1, oper2))
    elif operacion == "*":
        print(Calculadora.multiplicacion(oper1, oper2))
    elif operacion == "/":
        print(Calculadora.division(oper1, oper2))
    else:
        print("Error! Eso no es una operación válida!")
else:
    print("Error! Ambos números deben tener formato numérico.")

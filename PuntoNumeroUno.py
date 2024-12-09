while True:
    numero = float(input("Digite un número: ")) #Se le pide al usaurio que digite el número
    if numero >= 0:
        print(f"El cuadrado del número ingresado es: {numero * numero}")
        break
    else:
        print("El valor digitado no es válido")


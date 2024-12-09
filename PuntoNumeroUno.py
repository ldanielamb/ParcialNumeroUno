while True:#Para repetir el código indefinidamente
    numero = float(input("Digite un número: ")) #Se le pide al usaurio que digite el número
    if numero >= 0: #Si el numero es mayor a cero
        print(f"El cuadrado del número ingresado es: {numero * numero}") #Realizar la operación del caudado
        break #Romper el bucle
    else: #Si no
        print("El valor digitado no es válido") #Mostar el mensaje y repetir el bucle


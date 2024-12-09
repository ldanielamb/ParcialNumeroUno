def impares(a): #La funcion permite hacer la operación de impares
    imp = 3 * a + 1
def pares(a):#La operación permite hacer la operación de pares
    par = a / 2
def esparoimp(valor):#La función permite identificar si es o no par
    while valor != 1:#Mientras que el valor sea distinto a uno
        print(int(valor))#Se va a imprimir el valor digitado
        if valor % 2 == 0:#Si el valor es par, elmodulo es 0
            valor = pares(valor)#La variable ahora va a valer la operación que indica pares
        else:#Si es impar
            valor = impares(valor)#La variable ahora va a valer la operación que indica impares
valor = int(input("Digite un número: ")) #Se imprime el mensaje para que digite el valor
esparoimp(valor)#Se llama la función que ejecuta




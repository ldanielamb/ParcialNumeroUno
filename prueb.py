def impares(a):
    imp = 3 * a + 1
    return print(" ",imp)
def pares(a):
    par = a / 2
    return print(" ",par)
def esparoimp():
    if (valor % 2 == 0):
        pares(valor)
    else:
        impares(valor)
valor = int(input("Digite un número: "))
esparoimp()
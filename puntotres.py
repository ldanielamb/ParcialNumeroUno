k1 = 25000000 #Valor de A
k2 = 18900000 #Valor de B
tasa1 = 0.20 #Tasa de A
tasa2 = 0.30 #Tasa de B
def simple1(): #Función que permite evidenciar el crecimiento de la población A
    intsimp = k1 * tasa1 * 360 #La variable es igual a A * tasa de A * 360 días
    interes_simple = k1 + intsimp #La variable suma A y el crecimiento anual
    return interes_simple #Se devuelve el valor
def simple2(): #La función permite evidenciar el crecimiento de la población B
    intsimp = k2 * tasa2 * 360 #La variable es igual a B * tasa de B * 360 días
    interes_simple = k2 + intsimp #La variable suma B y el crecimiento anual
    return interes_simple #Se devuelve el valor
contador = 2022 #Se establece un contador en el año de inicio
if simple2()>simple1():#Condición de que si B pasa a A
    contador += 1#Se suma un año
    print("El año en que lo supera es:",contador)#Mostrar el mensaje
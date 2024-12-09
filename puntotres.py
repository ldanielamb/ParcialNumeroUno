k1 = 25000000
k2 = 18900000
tasa1 = 0.20
tasa2 = 0.30
def simple1():
    intsimp = k1 * tasa1 * 360
    interes_simple = k1 + intsimp
    return interes_simple
def simple2():
    intsimp = k2 * tasa2 * 360
    interes_simple = k2 + intsimp
    return interes_simple

contador=2022
while simple1()>simple2():
    contador +=1
print("El año en el que la población A supera a la población B es:",contador)
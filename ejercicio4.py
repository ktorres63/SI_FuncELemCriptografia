#Elimine los espacios en blanco y los signos de puntuación Indique cuál sería el alfabeto resultante y cuál su
#longitud
#GUARDE EL RESULTADO EN EL ARCHIVO “POEMA_PRE.TXT” (el que deberá ser adjuntado)

file = open("poema.txt")
file2 = open("POEMA_PRE.txt", "w")

cont = file.read()
nPoem = []

for letra in cont:
    if letra == ' ' or letra == '.' or letra == ',':
        continue
    nPoem.append(letra)

NuevoPoema = ''.join(nPoem)

print("tamaño: ",len(NuevoPoema))
file2.write(NuevoPoema)

file.close()
file2.close()
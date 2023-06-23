'''Volver a preprocesar el archivo insertando la cadena EPIS cada 17 caracteres, el texto resultante deberá
contener un número de caracteres que sea múltiplo de 4, si es necesario rellenar (padding) al final con
caracteres Z según se necesite'''

file = open("POEMA_PRE.txt")
file2 = open("POEMA_PRE2.txt","w+")
content = file.read()
nPoem = []
cont = 0
tamFin = len(content)

for letra in content:
    if cont == 17:
        nPoem.append("EPIS")
        cont = 0
    else:
        nPoem.append(letra)
        cont+=1


while(len(nPoem) % 4 != 0):
    nPoem.append("Z")


NuevoPoema = ''.join(nPoem)

file2.write(NuevoPoema)
print(NuevoPoema)

print("tamaño", len(nPoem))
    
file.close()
file2.close()
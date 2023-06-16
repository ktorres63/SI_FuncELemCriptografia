#Volver a preprocesar el archivo insertando la cadena UNSA cada 26 caracteres, el texto resultante deberá
#contener un número de caracteres que sea múltiplo de 5, si es necesario rellenar (padding) al final con
#caracteres # según se necesite
file = open("poema.txt")
content = file.read()
nPoem = []
cont = 0
tamFin = len(content)

for letra in content:
    if cont == 26:
        nPoem.append("UNSA")
        cont = 0
    else:
        nPoem.append(letra)
        cont+=1


while(len(nPoem) % 5 != 0):
    nPoem.append("#")


NuevoPoema = ''.join(nPoem)
print(NuevoPoema)

print("tamaño", len(nPoem))
    
file.close()
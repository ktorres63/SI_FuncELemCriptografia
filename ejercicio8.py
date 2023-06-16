#Volver a preprocesar el archivo cambiando cada carácter según alfabeto de su elección
file = open("poema.txt")
cont = file.read()
nPoem = []


for letra in cont:
    if letra == 'a' or letra =='A':
        nPoem.append('o')
    elif letra =='u' or letra == 'U':
        nPoem.append('v')
    elif letra =='e' or letra == 'E':
        nPoem.append('m')
    elif letra =='k' or letra == 'K':
        nPoem.append('p')
    elif letra =='\n' :
        nPoem.append('_')
    else:
        nPoem.append(letra)

NuevoPoema = ''.join(nPoem)
print(NuevoPoema)
file.close()
#Elimine las tildes
file = open("poema.txt")
cont = file.read()
nPoem = []

for letra in cont:
    if letra == 'á':
        nPoem.append('a')
    elif letra =='é':
        nPoem.append('e')
    elif letra =='í':
        nPoem.append('i')
    elif letra =='ó':
        nPoem.append('o')
    elif letra =='ú':
        nPoem.append('u')
    
    else:
        nPoem.append(letra)

NuevoPoema = ''.join(nPoem)
print(NuevoPoema)
file.close()
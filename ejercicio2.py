#Elimine las tildes
file = open("poem_2.txt")
file2 = open("poem_3.txt","w")
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
file2.write(NuevoPoema)
file.close()
file2.close()
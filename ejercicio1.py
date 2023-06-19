# Realizar las siguientes sustituciones: axi, hxj, ñxn, kxl, vxu, wxv, zxy, rxf (tanto mayúsculas como minúsculas).

file = open("poema.txt")
file2 = open("poem_2.txt", "w")

cont = file.read()
nPoem = []


for letra in cont:
    if letra == 'a' or letra =='A':
        nPoem.append('i')
    elif letra =='h' or letra == 'H':
        nPoem.append('j')
    elif letra =='ñ' or letra == 'Ñ':
        nPoem.append('n')
    elif letra =='k' or letra == 'K':
        nPoem.append('L')
    elif letra =='v' or letra == 'V':
        nPoem.append('u')
    elif letra =='w' or letra == 'W':
        nPoem.append('v')
    elif letra =='z' or letra == 'Z':
        nPoem.append('y')
    elif letra =='r' or letra == 'R':
        nPoem.append('f')
    else:
        nPoem.append(letra)

NuevoPoema = ''.join(nPoem)
file2.write(NuevoPoema)
file.close()
file2.close()
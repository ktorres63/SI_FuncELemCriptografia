#Convierta todas las letras a mayúsculas
file = open("poema.txt")
cont = file.read()
nPoem = []

for letra in cont:
    nPoem.append(letra.capitalize())

NuevoPoema = ''.join(nPoem)
print(NuevoPoema)
file.close()
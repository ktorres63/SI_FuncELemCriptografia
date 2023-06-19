#Convierta todas las letras a mayúsculas
file = open("poem_3.txt")
file2 = open("poem_4.txt","w")
cont = file.read()
nPoem = []

for letra in cont:
    nPoem.append(letra.capitalize())

NuevoPoema = ''.join(nPoem)
file2.write(NuevoPoema)
print(NuevoPoema)
file.close()
file2.close()
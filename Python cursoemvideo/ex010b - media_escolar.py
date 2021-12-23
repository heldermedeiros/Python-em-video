import math
n1 = float(input("Digite a nota 1:"))
n2 = float(input("Digite a nota 2:"))
media = ((n1+n2)/2)
#Forma 1:
print("Aprovado" if media>=7 else "Em recuperacao" if media>=5 else "Reprovado")

#Forma 2:
if media>=7:
    print("A média foi {:.1f}. Estude mais!".format(media))
elif media>=5:
    print("A média foi {:.1f}. Tá de recuperação. Estude mais!".format(media))
elif media<5:
    print("A média foi {:.1f}. Se fudeu, parça.".format(media))
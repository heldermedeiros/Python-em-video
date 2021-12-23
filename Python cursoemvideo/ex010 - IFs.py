tempo = int(input("Quanto anos tem seu carro?"))

########### #Opção A: If separado.
if tempo <=3:
    print("carro novo!")
else:
    print("Já tá na hora de trocar, hein?")

#######   #Opção B (no próprio IF:
print("carro novo" if tempo<=3 else "carro velho")

print ("--------- Fim ---------")
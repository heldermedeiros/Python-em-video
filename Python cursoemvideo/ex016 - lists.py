valores = list()
for count in range(0,5):
    valores.append(int(input("Digite um valor:")))

for c, v in enumerate(valores):
    print(f"Na posição {c} tem o número {v}")
print("Cheguei ao fim da lista")


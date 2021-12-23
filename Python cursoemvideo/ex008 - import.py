from math import sqrt, floor, ceil
from random import randint
num = int(input("Digite o numero 1:"))
raiz = sqrt (num)
print("a raiz de {} é igual a {}.".format(num, floor(raiz)))
num2 = randint (1,10)
print ("numero aleatório gerado: {}".format(num2))
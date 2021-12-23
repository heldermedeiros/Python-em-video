t = int(input("Digite o número que você deseja consultar a tabuada:"))
n = 0
for n in range (1,11,1):
    print("Soma: {:2} + {:2} = {:2} // Subtração: {:2} - {:2} = {:2} // Multiplicação: {:2} x {:2} = {:2} // Divisão: {:2} / {:2} = {:2.2f}".format(t,n,t+n,t,n,t-n,t,n,t*n,t,n,t/n))

x = 80
numeri = list (range(2,x+1))
def crivello(x) :
    for i in range(x**1/2):
        multipli = [x * i for x in range (2, x)]
        numeri.difference(multipli)

print(numeri)
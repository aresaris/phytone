x = 100

def crivello(x) :
    numeri = set(range(2,x+1))
    for i in range(2, int(x**0.5) + 1):
        numeri = numeri.difference({x * i for x in range (2, x+1)})
    return numeri

numeri = crivello(x)
print(numeri)
import math
primeNum = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

def gcd(m,n): 
    primeM = list()
    primeN = list()
    for i in primeNum:
        if m > i or n > i:
            while True:
                if m % i == 0:
                    primeM.append(i)
                    m = m / i
                else:
                    break

                if n % i == 0:
                    primeN.append(i)
                    n = n / i
                else:
                    break
    CPF = [x for x in primeM if x in primeN]
    GCD = math.prod(CPF)
    return GCD

print(gcd(60, 24))  # test case
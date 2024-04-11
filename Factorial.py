# Factorial Numbers

def fact(n):
    fact =1
    for i in range(n,0,-1):
        fact *= i
        print(i,fact)
    return

print(fact(5))

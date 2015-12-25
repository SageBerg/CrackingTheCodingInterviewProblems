def factorial(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

def zeros(n):
    zeros = 0
    i = 1
    while i <= n:
        i *= 5
        zeros += n / i
    return zeros 

def main():
    for i in range(51):
        print factorial(i)
    print zeros(5)
    print zeros(25)
    print zeros(50)
    print zeros(125)

main()

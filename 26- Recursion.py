print(" ")
def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

Factorial = factorial(5)
print("The result = ", Factorial)
print(" ")
def square (x):
    return x*x

number = [2, 4, 5, 8, 10]
result = list(map(square, number))

print("The square value of number = ", result)
#Filter Function:

marks = [62, 72, 75, 73, 84]
result = list(filter(lambda x : x%2==0, marks))

print("The result = ", result)
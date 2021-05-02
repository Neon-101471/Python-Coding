print(" ")
number = [10, 0, 20]
try:
    result = number[0]/number[5]
    print("The result = ", result)
except ZeroDivisionError:
    print("Found Zero Division Error.", end = "\n\n")
except IndexError:
    print("Found Index Error.", end = "\n\n")
finally:
    x = 10
    if x%2==0:
        print("This is even number.")
    else:
        print("This is odd number.")
print("Your program is done successfully.")

print(" ")
example = [10, 20, 25]
number = [10, 12, 15, 17, 24, 27]

result = [x*5 for x in example]
even = [x for x in number if x%2 == 0]

print("The result = ", result)
print("Even numbers are = ", even)

#Even number is finding using as filter function.
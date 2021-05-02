print(" ")
def result (marks):
    if marks < 33:
        raise ValueError ("Status: FAIL. Better luck next time.")
    return ("Congratulations! You are PASS.")

try:
    print(result(32))

except ValueError as Error:
    print(Error)
print(" ")
class zero:
    def cobalt (self):
        print("Cobalt-60")

    def neon (self):
        print("Neon-10")

class one (zero):

    def italy (self):
        print("My first choice is Italy.")

    def spain (self):
        print("My second choice is Spain.")

ict = one ()
ict.neon ()
ict.italy ()
ict.spain ()

print (" ")
print(issubclass(one, zero))
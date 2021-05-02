print(" ")
class phone:
    def __init__(self):
        print("Warning! This is phone class.")

class laptop (phone):
    def __init__(self):
        #super().__init__()
        print("Warning! This is laptop class.")

pc = laptop ()

#If line 8 is using, than phone class is working also. Without this method overriding is working.
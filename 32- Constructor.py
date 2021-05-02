print(" ")
class student:

    def __init__(self, name, roll, area):
        self.name = name
        self.roll = roll
        self.area = area

    def display(self):
        print(f"Name = {self.name}, Roll = {self.roll}, Area = {self.area}")

nowshin = student ("Homaira Nowshin", 101, "Rangamati")
nowshin.display()

saif = student ("Saif Uddin Ahmed", 102, "Moulvibazar")
saif.display()
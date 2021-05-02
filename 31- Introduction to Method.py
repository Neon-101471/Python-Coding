print(" ")
class student:

    def setValue(self, name, roll, area):
        self.name = name
        self.roll = roll
        self.area = area

    def display(self):
        print(f"Name = {self.name}, Roll = {self.roll}, Area = {self.area}")

nowshin = student ()
nowshin.setValue("Homaira Nowshin", 101, "Rangamati")
nowshin.display()

saif = student ()
saif.setValue("Saif Uddin Ahmed", 102, "Moulvibazar")
saif.display()
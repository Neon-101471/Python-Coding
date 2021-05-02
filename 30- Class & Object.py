print(" ")
class student:
    name = " "
    roll = " "
    area = " "

nowshin = student ()
#print(isinstance(nowshin, student))
nowshin.name = "Homaira Nowshin"
nowshin.roll = 101
nowshin.area = "Rangamati"

saif = student ()
saif.name = "Saif Uddin Ahmed"
saif.roll = 102
saif.area = "Moulvibazar"

print(f"Name: {nowshin.name}, Roll: {nowshin.roll}, Area: {nowshin.area}")
print(f"Name: {saif.name}, Roll: {saif.roll}, Area: {saif.area}")
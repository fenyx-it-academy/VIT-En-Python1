""" VIT-En-Python1
    First Exercise of Python lessen
    This project is producted by Hojjatollah Saeedi"""

# first exercise
# Area of a Circle

pi = 3.14159

print("This is first exercise that calculate the Area of a Circle")

radius = float(input("Please enter a radius of a CIRCLE: "))

area = pi * radius * radius

print("The Area of a Circle with radius ", radius, "is: ", area, "cm\u00b2")

#End of the Area of Circle

# second exercise
# This is Greeting address

print("This is second exercise that swap the names then Greeting")

fname = input("Please enter your firstname: ")
lname = input("Please enter your lastname: ")

swap = lname + "   " + fname
print("Hello dear ", swap, " :) ")

#End of Second exercise

# Third exercise
# Name and address

print("This is third exercise that show your name & address")

fname = input("Please enter your firstname: ")
lname = input("Please enter your lastname: ")
address = input("Please enter your address: ")

x = 0
n = len(address) - 1
star = '*'

while x < n :
    star = star + '*'
    x += 1

print("Your specifications is")
print('\n',fname, '\n', lname, '\n', address, '\n', star)

#End of third exercise

# Fourth exercise
# Fourth exercise is Second conversion to Days, Hours, Minutes and second

print("This is fourth exercise that convert the seconds to the days, hours ...")

seconds = int(input("Please enter seconds: "))

days = int(seconds / 86400)
hours = int((seconds - (days * 86400)) / 3600)
minutes = int((seconds - (days * 86400 + hours * 3600)) / 60)
second = int(seconds - (days * 86400 + hours * 3600 + minutes * 60))

print(seconds, "Seconds is\n", days, "Days\n", hours, "Hours\n", minutes, "Minutes\n", second, "Seconds\n")

#End of fourth exercise






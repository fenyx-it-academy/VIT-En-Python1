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

# Fifth exercise
# Print name  in a rectangle

fname = input("Enter your first name, please: ")
lname = input("Enter your last name, please: ")

fnum = len(fname)
lnum = len(lname)
star = '**'

x = fnum + lnum
i = 0

while i <= x :
    star = star + '*'
    i += 1


i = 1
space = ''
while i <= len(star) :
    space = space + ' '
    i += 1

i = 0
outputstr = ''
while i <= 4 :
    if i == 0 or i == 4 :
        outputstr += '\nI' + star + 'I'
    elif i == 2 :
        outputstr += '\nI ' + fname + ' ' + lname + ' I'
    else:  outputstr += '\nI' + space + 'I'
    i += 1

print(outputstr)

#End of fifth exercise

# Sixth exercise
# A short chat

print("This is the sixth exercise that have a short conversation with you")
print(" Come to have a short conversation together")

yourname = input("What is your name:")
print("Hello ", yourname)

yourage = int(input("Please, enter your age: "))

if yourage < 13 :
    print("You are very young")
elif yourage >= 13 or yourage <= 19 :
    print("You are a teenager")
elif yourage >= 20 or yourage <= 39 :
    print("You are a young person")
elif yourage >= 40 or yourage <= 55 :
    print("You are a middelage person")
elif yourage >= 56 :
    print("You are a old person")

yourcountry = input("Where are you from ?")
yourplace = input("Wich country do you live now ? ")

if yourcountry == yourplace :
    print("So you live fortunately in your country")
else :
    print("Unfortunately you are a emigrant")

marriagestatus = bool(input("Are you married ? (if NO, please enter 0, other Numbers is yes)!"))

if marriagestatus == True :
     childnum = int(input("How many childeren do you have ? "))
     if childnum <= 2 :
         print("You have a small family")
     else :
         print("you have a big family")
else :
    print("I hope that you find a good partner")


#End of sixth exercise

#End of the all of exercises

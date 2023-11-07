# Question 1: Ask the user for the radius of a circle and calculate the area of the circle. Write a program that adds enough "-" to underline the area of the circle.
### Example:
# The Area of the Circle is 232 cm².
# ---------------------------
 
import math
radius = float(input("Enter the radius of the circle: "))
area = round(math.pi * (radius ** 2))
print(f"The area of the circle is {area} cm²." )
print("-------------------------------")

## Question 2: Take the person's first and last name and write a greeting address. While writing, swap the first and last name and add three spaces between them.
# ---------------------------

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
first_name, last_name = last_name, first_name

print("Dear", first_name, last_name, sep="   ")

## Question 3: Take the person's first name, last name, and address and print them on separate lines. Under the address, add as many "*" as the length of the address.

First_name = input('Please enter your first name: ')
Last_name = input('Please enter your last name: ')
Adress = input('Please enter your adress: ')
print(First_name)
print(Last_name)
print(Adress)
adress_length = len(Adress)
ask_adress = '*' * adress_length
print(ask_adress)

## Question 4: Take seconds as input from the user and convert it to days, hours, minutes, and seconds.
#----------------------------

seconds = int(input('Please enter the number of seconds: '))
days = seconds // (24 * 3600)
hours = (seconds % (24 * 3600)) // 3600
minutes = ((seconds % (24 * 3600)) % 3600) // 60
remaining_seconds = ((seconds % (24 * 3600)) % 3600) % 60
print(f"{seconds} seconds is equal to:")
print(f"{days} days, {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")

## Question 5: Write a program that takes a person's first name and last name and places it in the center of a rectangle. The rectangle should expand or shrink according to the length of the first and last name.
### Example: 

name_first = input('Enter your first name: ')
name_last = input('Enter your last name: ')
full_name = name_first + last_name
length_full = len(full_name)
rectangle_width = length_full * 2 + 6
rectangle = '*' * rectangle_width + '\n'
rectangle += '* ' + full_name.center(rectangle_width - 4) + "*\n"
rectangle += '*' * rectangle_width
print(rectangle)


## Question 6: Ask the user at least 6 questions and write a simple chat program that gives answers based on their responses.

name = input("Could you write your name? ")
print("Lovely to see you", name, "!")
age = int(input('Could you write your age? '))
print("You are " + str(age) + "years old. Wow you have so much wishdom and experience to share! ")
country = input('Where do you live? ')
print("To live in",  country, "is amazing!")
book = input("What is your favorite book? ")
print("I really enjoyed reading", + book)
food = input("what is your favorite food? ")
print("Yummy! I can eat", + food, + "all the time.", )
hobby = input("What is your hobby? ")
print("Your favorite hobby is", hobby, + "it sounds a tad insane!")
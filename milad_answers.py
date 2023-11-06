"""Question 1: Ask the user for the radius
 of a circle and calculate
 the area of the circle.
 Write a program that adds enough "-" to
 underline the area of the circle."""

radius = float(input("Enter the radius of the circle: "))
area = 232 * (radius ** 2)
formatted_area = f"{area} cm2"
line_length = len(formatted_area)
underline = "-" * line_length
print(f"The Area of the Circle is {formatted_area}")
print(underline)


'''Question 2: Take the person's first and last name and write a greeting address.
 While writing, swap the first and last name and add three spaces between them.'''

first_name = input('what is your firstname? ')
last_name = input('what is your lastname? ')
print(f"hello dear {first_name}\t{last_name}")

'''Question 3: Take the person's first name, last name, and address
 and print them on separate lines.
 Under the address, add as many "*" as the length of the address.'''

first_name = input('what is your firstname? ')
last_name = input('what is your lastname? ')
address = '2491 db\n125 Hoofdstraat(amsterdam)'
separate = "*" * len(address)
print(f'{first_name}\n{last_name}')
print(address)
print(separate)

'''Question 4: Take seconds as input from the user
 and convert it to days, hours, minutes, and seconds.'''

your_second = int(input('enter your second '))
day = your_second // (24 * 3600)
your_second = your_second % (24 * 3600)
hour = your_second // 3600
your_second %= 3600
minute = your_second // 60
your_second %= 60
second = your_second
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minute, second))

"""Question 5: Write a program that takes a person's first name and 
last name and places it in the center of a rectangle.
The rectangle should expand or shrink according to the length of the first and last name."""

your_name = input('what is your firstname, lastname? ')
print("*" * len(your_name))
print("\t\t\t\t\t" + your_name)
print("*" * len(your_name))
Q1 = input('what is your favorite programming language? ')
print('i really like python')
Q2 = input('how old are you? ')
print('i think you look younger!')
Q3 = input('how was the first exercise? ')
print('i think was a little bit hard for me!')
Q4 = input('what is your favorite color? ')
print('its a nice color')
Q5 = input('what is your name? ')
print('nice to meet you ')
Q6 = input('where are you from? ')
print("it's a beautiful country! ")










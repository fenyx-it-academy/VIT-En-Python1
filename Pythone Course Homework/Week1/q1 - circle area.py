import math
circle_radius = float(input('Enter the radius (in cm) of the circle to calculate Area: '))
circle_area = math.pi * circle_radius ** 2
print("The area of the circle is: \n" + str(circle_area) + " cm2")
print('-' * len(str(circle_area)))

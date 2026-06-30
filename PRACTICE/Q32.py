# Circle Area FinderWrite a script that asks the user to input the radius of a circle as an integer or float. Calculate and print the area of the circle using the formula $\text{Area} = 3.14159 \times \text{radius} \times \text{radius}$.
# Concept: Working with floats, expressions, and variable reuse.

radius = int(input("Enter the radius : "))

area_of_circle = float(3.14159*radius*radius)

print(f"The area of circle is {area_of_circle}")
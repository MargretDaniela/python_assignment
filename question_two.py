# Create a program to calculate the area of a triangle (1/2 *base * height).
# Base and height should be entered using the key board and provide the nswer in 2 decimal places.  
base = float(input("Enter the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
area = 1/2 * base * height
print(f"The area of the triangle :{area:.2f}")
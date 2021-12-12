import math

z = int(input("Input height of trapezoid: "))
print("Input bases of trapezoid: ")
a, b = input().split()
if a > b:
    c = (math.sqrt((int(a) - int(b)) ** 2 / 4 + z ** 2)) * 2 + int(a) + int(b)
else:
    c = (math.sqrt((int(b) - int(a)) ** 2 / 4 + z ** 2)) * 2 + int(a) + int(b)
print("Perimeter of a trapezoid is ", c)


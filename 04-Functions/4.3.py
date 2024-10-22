###
# Calculates the area of a triangle based on the lengths
# 3, 4, 5 (result is 6)
# 5, 12, 13 (result is 30)
# 7, 24, 25 (result is 84)
# of the triangle's sides
# P=√p(p−a)(p−b)(p−c)−
#
import math

def triangle_area(a,b,c):
    p = (a + b + c)/2
    result = math.sqrt(p*(p - a)*( p - b)*(p - c ))
    return result
area1 = triangle_area(3,4,5)
area2 = triangle_area(5,12,13) 
area3 = triangle_area(7,24,25)
print(f'The area of  ​a triangle with sides 3, 4, 5 is {area1}')
print(f'The area of  ​a triangle with sides 5, 12, 13 is {area2}')
print(f'The area of ​a triangle with sides 7, 24, 25 is {area3}')
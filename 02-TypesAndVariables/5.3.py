###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
volume = int(a)*int(b)*int(c)
surface = int(a)*int(b)*2+int(a)*int(c)*2+int(b)*int(c)*2
print(f"the volume is {volume} and the surface is {surface}")

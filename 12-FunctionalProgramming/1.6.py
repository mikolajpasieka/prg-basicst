
avg_speed = lambda x,y,z: x/(y+(z*(1/60)))


km = int(input("Enter distance in km"))
h = int(input("Enter number of travel hours"))
m = int(input("Enter number of travel minutes"))


result = avg_speed(km,h,m)
print(f"Average speed: {result}")
def avg_speed(distance,hours,minutes):
    speed = distance/(hours + minutes*(1/60))
    return speed 


km = int(input("Enter distance in km"))
h = int(input("Enter number of travel hours"))
m = int(input("Enter number of travel minutes"))


result = avg_speed(km,h,m)
print(f"Average speed: {result}")

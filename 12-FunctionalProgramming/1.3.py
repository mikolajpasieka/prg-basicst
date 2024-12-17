
def ms_to_kmh(ms):
    kmh = ms*3,6
    return kmh 

x = int(input("give speed in m/s"))

result = ms_to_kmh(x)
print(result)
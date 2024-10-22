def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return round(0.393700787*n, 2)
def feet_and_inch_to_cm(m, n):
    return round(2.54*n, 2) + round(m*30.48,2)
  
if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'16 cm = {cm_to_inch(16)}inch')
    print(f'5 feet 9 inches = {feet_and_inch_to_cm(5,9)}cm')

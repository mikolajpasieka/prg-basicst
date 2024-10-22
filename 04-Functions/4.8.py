hours = 0 
minutes = 0 

def time_string(hours, minutes, time_format):
    if time_format == 12:
        if hours > 0 and hours <12:
           hours = hours 
           result = (f"{hours},{minutes}am ")
        else:
            hours -=12 
            result = str(f"{hours},{minutes}pm ")
    else:
        result = str(f"{hours}:{minutes}")
    return result 
time_string(15, 38, '24') 
time_string(8, 3, '24') 
time_string(0, 5, '24') 
time_string(11, 15, '12') 
time_string(0, 7, '12') 
time_string(7, 30, '12')
time_string(12, 46, '12') 
time_string(13, 10, '12') 
time_string(19, 2, '12') 
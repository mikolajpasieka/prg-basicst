###
# Functions to read any data type from the keyboard
#
message = ''
def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    real = (input(message))
    return real

def input_boolean(message):
    boolean = input(message)
    return boolean


if __name__ == "__main__":
    print(f"{input_string(message)}")
    print(f"{input_integer(message)}")
    print(f"{input_real(message)}")
    print(f"{input_boolean(message)}")
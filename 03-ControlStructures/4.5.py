###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    caesar_code =  ord(char)
    # add one to the character's code
    leter = caesar_code + 1  
    # replace new character code with its
    # corresponding character (use chr())
    new_leter = chr(leter)
    # add encrypted character to encrypted text
    

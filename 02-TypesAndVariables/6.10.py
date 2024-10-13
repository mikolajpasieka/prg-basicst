###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print("Title in capital letters: ", movie.upper() )

# print title in small letters
print('Title in small letters:', movie.lower())

# print how many times the vowel "e" appears in the title
print(f' "e" appears in the title: {movie.count("e")} times')

# print where in the text is the word "Lord"
print(f'The word "Lord" begins at the {movie.find("Lord")}th position in the sequence')

# print where in the text is the word "dragon"
print(f'The word "dragon" begins at the {movie.find("dragon")}th position in the sequence')
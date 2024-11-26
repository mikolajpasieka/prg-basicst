#Create a dictionary as in the example below. 
# Do you know what type of value was used in each of the six key-value pairs?
#Then, create a program that:
person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
# Displays name
print(person['name'])

# Displays hobby
print(person['hobby'])

# Displays the entire contents of the dictionary
for key,value in person.items():
   print(f"{key} : {value}")

#Changes surname to 'Nowak'
person["surname"] = "Nowak"

# Adds gender: 'male'
person["gender"] = "male"

# Changes person's marriage status
person["married"] = False

# Adds a new hobby: 'bicycle'
person["hobby"].append('bicycle')

# Adds work phone to existing phones: '313131444'
person["phone"]["work phone"] = '313131444'

#Displays the entire contents of the dictionary (iterate over dictionary items)
for key,value in person.items():
   print(f"{key} : {value}")
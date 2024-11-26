#Create an array with 5 dictionaries, 
# each containing a country and its population. 
# Then, print the array contents. 

# Sample result:
# COUNTRY  POPULATION
# Poland   38000000


countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":84480000},
{"name":"France", "population":68170000},
{"name":"Spain", "population":48000000},
{"name":"Italy", "population":58000000}
]

print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country["name"]}  {country["population"]}")

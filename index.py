import random

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

otherRandomNumbers = list()
for i in range(10):
    otherRandomNumbers.append(random.randrange(1, 10, 1))

# Generate a list of numbers 1..10
randomNumbers = range(1, 10)

# Iterate from 1 to 10
for number in randomNumbers:
    if number in otherRandomNumbers:
        print(f'{number} is in the random list')
    else:
        print(f'{number} aint in there')

    # Iterate your random number list here

    # Do the two numbers match? Change the boolean.

 #-------PLANETS ----------    
planet_list = ["Mercury", "Mars"]
planet_list.extend(["Jupiter", "Saturn"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
cold_planets = ["Uranus", "Neptune"]
planet_list.extend(cold_planets)
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
planet_list.remove("Pluto")
for planet in planet_list:
    print(planet)

#--------WORDS AND DEFINITIONS--------
word_definitions = dict()
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Coffee"] = "Awesome drink that wakes you up"
word_definitions["Potato"] = "The most beautiful vegetable in the world"





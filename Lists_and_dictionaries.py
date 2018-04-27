# lists and Dictionaries

#Picking a specific number from a lists

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

#Modifying a list

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

zoo_animals[2] = "hyena"

zoo_animals[3] = "cheetah"

# Adding items to a lists

suitcase = []
suitcase.append("sunglasses")

suitcase.append("pants")
suitcase.append("underwear")
suitcase.append("socks")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# Making a slice list_length

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:] # Slice  does not include the end of the range

# Slicing a string

animals = "catdogfrog"

cat = animals[:3]

dog = animals[3:6]

frog = animals[6:]

# Finding the index of a certain item and inserting into that index

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

animals.insert(duck_index, "cobra")

print animals

# Using a for loop to print a modified list based on your variable.

my_list = [1,9,3,8,5,7]

for number in my_list:
  print 2 * number

  # Making a modified list from an existing list using a for loop.

  start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number**2)

square_list.sort()

print square_list

# Printing items from a dictionary based on the values of the key

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents['Sloth']
print residents['Burmese Python']

# Adding new entries in a dictionary

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu["Pizza"] = 7.50
menu["winga"] = 10
menu["Mozz sticks"] = 3.50

print "There are " + str(len(menu)) + " items on the menu."
print menu

# Deleting entries and replacing key value with new info

zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}

del zoo_animals['Unicorn']

del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]

zoo_animals["Rockhopper Penguin"] = "Rock exhibit"

print zoo_animals

# Removing an item from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove("dagger")

# Review

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()


inventory["pocket"] = ["seashell", "strange berry", "lint"]

inventory["backpack"].sort()

inventory["backpack"].remove("dagger")

inventory["gold"] = inventory["gold"] + 50

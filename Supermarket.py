# Supermarket Example: For loops with lists and dictionaries

names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print name            # Outputs every name in the lists

# Printing out the key values in a dictionary

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print webster[key]

# Printing even numbers only using a loop with a condition

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for numbers in a:
  if numbers % 2 == 0:
    print numbers

# For loop to see how many items in a list match a string

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

# Printing out a string by line or choosing a certain letter to Printing
for letter in "Codecademy":
  print letter

print       # blank prints can be used to put space in the output
print

word = "Programming is fun!"

for letter in word:
  if letter == "i":
    print letter

# Supermarket project

# Start by creating a dictionary

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3,

}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

# Iterating through two lists with the same keys

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3,

}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]

# Mulipying price X stock to get total inventory is worth

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0
for x in prices:
  total_per_key = prices[x] * stock[x]
  total = total + total_per_key
print total

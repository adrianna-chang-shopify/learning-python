# Learning about tuples, lists, and dictionaries

# A tuple - an immutable collection of objects
months = 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'

print months[0] # Note that tuples are 0-indexed

# Can also wrap a tuple in parentheses if splitting over multiple lines like this
months_db_line = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

# Lists - mutable version of tuple (like an array)
cats = ['Bobby', 'Jimmy', 'Larry', 'Sal']

print cats[2]

cats.append("Susan") # Append item to list
del cats[2] # Remove item from list

# Dictionary - set of key/val pairs, like a hash

phonebook = { 'Peter Parker': 8771234, 'John Doe': 4551890, 'Susan Smith': 5551010 }

print phonebook['Peter Parker'] # print value in phonebook based on key

# Add value to phonebook using key as well:
phonebook['Penny Potts'] = 1234567

# delete: 
# del phonebook['Penny Potts']

#Some useful dictionary functions:

print "Testing out the .has_key function for dicts"

if phonebook.has_key('John Doe'):
    print "John is in the phonebook!"
else:
    print "John is not in the phonebooks!"

print "Here are the phonebook keys: "
print phonebook.keys()

print "Here are the phonebook values: "
print phonebook.values()

# Sort a list
keys = phonebook.keys()
print keys
keys.sort()
print keys

# Use len function to get the number of entries:
print "The phonebook has this many entries: ", len(phonebook)

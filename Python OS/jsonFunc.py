import json

#dumps : from any data type tp string
#loads : from string to any datatype, structured

# dump and load : work with files
# dumps and loads : work with strings

filename = 'userName.json'
name = ''

# Check for a history file 
try:
    with open(filename, 'r') as r: # Load the user's name from the history file 
        name = json.load(r)
except IOError: 
    print("First-time login")
    
# If the user was found in the history file, welcome them back 
if name != "": 
    print("Welcome back, " + name + "!")
else: # If the history file doesn't exist, ask the user for their name
    name = input("Hello! What's your name? \n ") 
    print("Welcome, " + name + "!")
    
# Save the user's name to the history file 
try:
    with open(filename, 'w') as f: 
        json.dump(name, f)
except IOError: 
    print("There was a problem writing to the history file.")
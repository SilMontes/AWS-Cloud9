''' 1) Define a list and tuple in Python. Provide some examples. '''

# list
elements = ["Hello", {'a':1.0}, 89, ['A','E'],
            {':)':'😊', ':(':'😕', ':D':'😁'}]
            
letters = ['A','B','C','D']
numbers = [21.3,34,56.76,45.6]

# tuple
userNames = ('Ani23','Lily45','John09')
objects = (
    {'Apple': {'price':1.21, 'stock':50},
    'Mango' : {'price':2.99, 'stock':20}},
    'bicycle',
    '234'
)
ages = (23,56,87,30)


''' 2) What is a name space in Python? 
        R/: Indentation 
'''


''' 3) What is the difference between a local variable and a global variable? 
        R/:  Global variables can be accessed globally in the entire program, 
        whereas local variables can be accessed only within the function or block in which they are defined.
'''

''' 4) What is an IDE? Mention some common IDEs that could be used with Python. 
        R/: Visual Studio Code, Atom, PyCharm, Sublime Text...
'''

''' 5) What are modules in Python? Provide some examples.
        R/: We can say that a module is a file containing a set of functions and variables that can be used or imported 
        inside another Python program. Using modules results in having code logically organized by being grouped into 
        one Python file which makes development easier and less error-prone. Another advantage is that code is easier to understand and use.
        
        *** Check module_example.py and import_modules.py files. ***
'''


''' 6) What is the difference between an array and a list? 
        R/: Differences between an array and a list:
            * A list can consist of elements belonging to different data types, but an array only consists of elements belonging to the same data type
            * A list can be printed without any explicit looping, yet a loop has to be formed to print or access the components of an array
            * An array's elements are allocated with contiguous memory locations allowing easy modification, that is, addition, deletion, accessing of elements. 
            * In Python, we have to use the array module to declare arrays, but no module is needed to declare a list.
'''

''' 7) What are operators? Provide some examples.
        R/: Python Operators in general are used to perform operations on values and variables.
        * Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division.
            (+, -, *, /, //)
        
        * Comparison operators compares the values. (>, >=, <, <=, !=, ==)
        
        *Logical operators: (and, or, not)
        
        * Assignment operators are used to assigning values to the variables. (+=, -=, *=)
'''

# Operators
num1 = 5
num2 = 4

if num1 > num2:
    print(str(num1)+" is greater than "+str(num2))
elif (num1 < num2):
    print(str(num2)+" is greater than "+str(num1))
else:
    print(str(num1)+" is equal to "+str(num2))

counter = 0
for i in ages:
    counter += i
average = counter / len(ages)    
print(average)


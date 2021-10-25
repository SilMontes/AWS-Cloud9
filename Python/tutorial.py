numbers = [5,7,8,20]
numbers.append(29)
numbers.insert(0,32) # the first number defines the position
numbers.pop() # delete the last one
numbers.sort()
numbers.reverse()
print(numbers)

numbers= [3,3,5,6,8,9,10,4,5,6]
uniqueNumbers=[]
for num in numbers:
    if num not in uniqueNumbers:
        uniqueNumbers.append(num)
uniqueNumbers.sort()
print(uniqueNumbers)

numTuple=(1,2,3,4)
print(numTuple[0])


coordinates = (1,2,3,4)
x, y, z, y = coordinates # asigning a value to each letter
print(x,y,z)

# [] list
# () tuple
# {} dictionary

numbers = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}
phone = "3466"
for item in phone:
    for key, value in numbers.items():
        if item == key:
            print(value)
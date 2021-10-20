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
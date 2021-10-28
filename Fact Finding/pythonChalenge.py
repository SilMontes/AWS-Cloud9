fileResults = open('results.txt','w')
count = 0
for x in range(1,251):
    for i in range(1,251):
        if(x % i == 0):
            count += 1
    if (count == 2):
        fileResults.write(str(x)+'\n')
    count = 0
    
fileResults.close()
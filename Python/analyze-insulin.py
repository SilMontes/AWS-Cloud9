file=open("Python/preproinsulin-seq.txt", "r")
lines=file.readlines()
print(lines)
file.close()

file=open("Python/preproinsulin-seq-clean.txt", "w")
for line in lines:
    if line == "ORIGIN      \n" or  line == "//":
        line = ""
        file.write(line)
    else:
        line = line.replace("1","")
        line = line.replace("\n","")
        line = line.replace(" ","")
        line = line.replace("6","")
        file.write(line)
file.close()

file=open("Python/preproinsulin-seq-clean.txt", "r")
lines = file.readlines()
line24 = ""
line54 = ""
line89 = ""
line110 = ""
for line in lines:
    print(len(line))
    
    file24=open("Python/lsinsulin-seq-clean.txt","w")
    for char in range(0,24):
        line24 += line[char]
    file24.write(line24)
    file24.close()
    
    file54 = open("Python/binsulin-seq-clean.txt","w")
    for char in range(24,54):
        line54 += line[char]
    file54.write(line54)
    file54.close()
    
    file89 = open("Python/cinsulin-seq-clean.txt","w")
    for char in range(54,89):
        line89 += line[char]
    file89.write(line89)
    file89.close()
    
    file110 = open("Python/ainsulin-seq-clean.txt","w")
    for char in range(89,110):
        line110 += line[char]
    file110.write(line110)
    file110.close()

print(len(line24),len(line54),len(line89),len(line110))
file.close()
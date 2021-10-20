import copy
import csv

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

myInventoryList = []

with open('/home/ec2-user/environment/Python/car_fleet.csv') as csvFile: # keeps a file open while you read data, it will be open as a varibale name csvFile
    csvReader = csv.reader(csvFile, delimiter=',')  # reads a column one by one taking the comma a delimeter and the value will be assigned to csvReader
    lineCount = 0  # lines counter
    for row in csvReader: # for each line in csvReader
        if lineCount == 0: #
            print(f'Column names are: {", ".join(row)}')  # f replaces .format()
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
print(f'Processed {lineCount} lines.')
print(currentVehicle)
import logging # loging library

logging.basicConfig(filename="demoLog.log",level=logging.DEBUG) # DEBUG INFO WARNING


#Assertions are conditions that check the values in the application

def chekValue(valueToCheck):
    try:
        assert(type(valueToCheck) is int), "You must enter a number"
        assert (valueToCheck > 0), "The number must be greater than 0"
    except AssertionError as msg:
        logging.debug(msg)
        print(msg)
    
    if valueToCheck > 0:
        print("Value greater than 4")
        logging.debug(f'{valueToCheck} is greater than 4')
        
num = int(input("Enter a number\n"))
chekValue(num)
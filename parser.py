import re
#TYPES OF MIR
OPERATOR = 'OPERATOR'
INT = 'INT'
FLOAT = 'FLOAT'
STRING = 'STRING'

def notEmpty(char):
    return char != ' ' and char != '\b' and char != '\n'

def run(arguments):
    totalLen = len(arguments)
    tokens = []
    charIndex = 0
    
    while charIndex < totalLen and arguments[charIndex] != None and notEmpty(arguments[charIndex]):
        if re.match("[A-Za-z]", arguments[charIndex]):
            print("single alphabet character")
        elif re.match("^[0-9]", arguments[charIndex]):
            print("single digit")
        else:
            print("ERROR")
        charIndex += 1
        
while True:
    arguments = input("MIR $ ")
    run(arguments)



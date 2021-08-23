import re
#TYPES OF MIR
OPERATOR = 'OPERATOR'
PLUS = 'PLUS'
INT = 'INT'
FLOAT = 'FLOAT'
STRING = 'STRING'

class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value
    def __repr__(self):
        return "Type: %s, Value: %s" % (self.type, self.value)

class Mir:
    def __init(self, text, currentPos):
        self.text = text
        self.currentPos = currentPos
    
def spaceOrNewLine(char):
    return char == ' ' or char == '\t' or char == '\n'

def run(arguments):
    totalLen = len(arguments)
    tokens = []
    charIndex = 0
    
    number_str = ''
    new_str = ''
    
    while charIndex < totalLen and arguments[charIndex] != None:
        c = arguments[charIndex]
        if re.match("[A-Za-z]", c):
            print("single alphabet character")
        elif re.match("^[0-9]", c):
            number_str += arguments[charIndex]
            
            print("single digit ", c)
        elif spaceOrNewLine(c):
            if number_str != '':
                tokens.append(Token(INT, number_str))
                number_str = ''
        
        elif c == '+':
            print("plus")
            tokens.append(Token(PLUS))
        else:
            print("ERROR")
        charIndex += 1
    if number_str != '':
        tokens.append(Token(INT, number_str))
    print(tokens)



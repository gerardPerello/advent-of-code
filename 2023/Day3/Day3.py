import re
import numpy as np
from functools import reduce
import operator

def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input

def whatIsThisSymbol(symbol):
    if symbol == '.': #Es un punto
        return 0
    elif re.search("\d", symbol):
        return 1 #Es un numero
    elif symbol == '*':
        return 3
    else:
        return 2 #Es un simbolo distinto
    

def endNumber(line, position):
    endNumberPosition = position
    while(whatIsThisSymbol(line[endNumberPosition]) == 1):
        endNumberPosition += 1
        if endNumberPosition == len(line):
            break
    """ 
    print("Position and endNumberPosition")
    print(position)
    print(endNumberPosition - 1) """
    return endNumberPosition - 1


def checkMask(mask):
    for i in mask:
        for j in i:
            if whatIsThisSymbol(j) in (2,3):
                return True
    return False

def checkGearInMask(mask):
    print("mask shape")
    print(mask.shape)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            print(i,j)
            print(mask[i,j])
            if whatIsThisSymbol(mask[i,j]) == 3:
                return True, j , i
    return False, 0, 0

def analizeLine(topLine, line, botLine, position, endNumberPosition, validNumbers, gearRatios, lineIndex):
    
    x_l,y_l = endNumberPosition-position + 3, 3

    x_i, y_i = position - 1, 0

    
    try:
        
      matrix = np.array([list(topLine), list(line), list(botLine)])
    except:
        print(topLine)
        print(line)
        print(botLine)
        print("Exception")
    print(matrix)
    mask = matrix[y_i:y_i + y_l, x_i:x_i + x_l]

    print("mask")
    print(mask)
    isSymbolInMask = checkMask(mask)
    print(isSymbolInMask)
    print(line[position:endNumberPosition+1])
    if(isSymbolInMask):
      validNumbers.append(int(line[position:endNumberPosition+1]))
    isGearInMask, xGear, yGear = checkGearInMask(mask)
    
    if(isGearInMask):
      print("gearRatios")
      print(gearRatios)
      if((x_i+xGear,lineIndex+yGear) in gearRatios):
        gearRatios[(x_i+xGear,lineIndex+yGear)].append(int(line[position:endNumberPosition+1]))
      else:
        gearRatios[(x_i+xGear,lineIndex+yGear)] = [int(line[position:endNumberPosition+1])]
      print("After gearRatios")
      print(gearRatios)
      


def analizeLines(topLine, line, botLine, validNumbers, gearRatios, lineIndex):
    print("line")
    print(line)
    lineLen = len(line)
    if not topLine: #CASE WHEN WE ARE DOING THE FIRST LINE
        topLine = "."*lineLen
    if not botLine: #Case when we are doing the LAST line
        botLine = "."*lineLen

    position = 0
    while position < len(line):
        if(whatIsThisSymbol(line[position]) == 1):
            endNumberPosition = endNumber(line, position)
            analizeLine(topLine, line, botLine, position, endNumberPosition, validNumbers, gearRatios, lineIndex)
            position = endNumberPosition + 1
        else:
            position += 1

def modify_input(input_list):
    # Add a '.' at the beginning and end of each row
    modified_list = ['.' + row + '.' for row in input_list]

    # Length of each row (including the added '.')
    row_length = len(modified_list[0])

    # Add a row of '.' at the beginning and the end of the list
    modified_list.insert(0, '.' * row_length)
    modified_list.append('.' * row_length)

    return modified_list

def main():
  data = modify_input(readInput("Day3\input2.txt")[:-1])
  validNumbers = [] #Lista para el Part1  (que tienen un simbolo alrededor)
  gearRatios = dict() #Lista con todos los numeros que tienen un gear, ademas, apuntamos la posicion del gear.
  for lineIndex in range(1,len(data)-1):
    analizeLines(data[lineIndex-1],data[lineIndex],data[lineIndex+1], validNumbers, gearRatios, lineIndex)
          
  totalGear = 0
  for key in gearRatios.keys():
      if(len(gearRatios[key]) > 1):
          print(gearRatios[key])
          totalGear += reduce(operator.mul, gearRatios[key], 1)
  return sum(validNumbers), totalGear
  
  
  
  
     

print(main())
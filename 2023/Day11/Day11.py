import math
def readInput(path):
    input = "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, part):
    """ instructions = input_list[0]

    dictio = {}
    for pair in input_list[2:]:
        todo = pair.split()
        keynode = todo[0]
        left = todo[2][1:-1]
        right = todo[-1][:-1]

        if todo[0][-1] == 'A':
            tipo = 1 #Starter
        elif todo[0][-1] == 'Z':
            tipo = 2 #End
        else:
            tipo = 3 #Normal


        dictio[keynode] = {"L": left, "R": right, "T": tipo} """

    return input_list



def main():
    data = modify_input(readInput("Day9/input2.txt"), 1)
    

    return data

print(main())
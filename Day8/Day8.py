import math
def readInput(path):
    input = "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, part):
    instructions = input_list[0]

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


        dictio[keynode] = {"L": left, "R": right, "T": tipo}

    return dictio, instructions

def terminado(nodo):
    if nodo[-1]=='Z':
        return True

def moverse(arbol, instrucciones, nodoactual, visto, paso):
    while nodoactual != "ZZZ":
        if nodoactual in visto:
            visto[nodoactual] += 1
        else:
            visto[nodoactual] = 1

        current_instruction = instrucciones[paso % len(instrucciones)]
        siguientenodo = arbol[nodoactual][current_instruction]

        # Improved print statement
        print(f"Step: {paso}, Instruction: {current_instruction}, Current Node: {nodoactual}, Next Node: {siguientenodo}")

        nodoactual = siguientenodo
        paso += 1

    return paso

def moverse2(arbol, instrucciones, starters):
    pasos = {}
    for starter in starters:
        nodoactual = starter
        print(nodoactual)
        paso=0
        while arbol[nodoactual]['T'] != 2:
            
            current_instruction = instrucciones[paso % len(instrucciones)]
            siguientenodo = arbol[nodoactual][current_instruction]

            # Improved print statement
            print(f"Step: {paso}, Instruction: {current_instruction}, Current Node: {nodoactual}, Next Node: {siguientenodo}")

            nodoactual = siguientenodo
            paso += 1
        pasos[nodoactual]=paso

    return pasos


def main():
    arbol, instrucciones = modify_input(readInput("Day8/input.txt"), 1)
    visto = {}
    print(arbol)
    #Parte 1
    #pasos = moverse(arbol, instrucciones, "AAA", visto, 0)
    # Parte 2
    starters = {k:v for (k,v) in arbol.items() if v['T'] == 1}
    print(starters)
    pasos = moverse2(arbol, instrucciones, starters)

    

    return math.lcm(*pasos.values())

print(main())



# 307
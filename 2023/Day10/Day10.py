import math
def readInput(path):
    input = "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, part):
    """
    Modify the input list into a dictionary with key-value pairs and set global variables for matrix dimensions.
    Key: Tuple (x, y) representing the position of the character.
    Value: The character at that position.
    """
    global MATRIX_X, MATRIX_Y, START_POSITION
    MATRIX_X = len(input_list[0])  # Width of the matrix
    MATRIX_Y = len(input_list)     # Height of the matrix

    result = {}
    for y, row in enumerate(input_list, start=1):
        for x, char in enumerate(row, start=1):
            if char == "S":
                START_POSITION = (x,y)
            result[(x, y)] = char
    return result

def get_around_positions(position):
    """
    Given a position, return all the positions around it, considering matrix boundaries.

    Args:
    position (tuple): A tuple (x, y) representing the position.

    Returns:
    list: A list of tuples representing the positions around the given position.
    """
    x, y = position
    around_positions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Skip the position itself
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            # Check boundaries
            if 1 <= new_x <= MATRIX_X and 1 <= new_y <= MATRIX_Y:
                around_positions.append((new_x, new_y))
    return around_positions

def get_next_position(node, data):
    """
    Determine the next position the animal goes to from the current node.

    Args:
    node (tuple): The current position of the animal (x, y).
    data (dict): The dictionary containing the matrix data.

    Returns:
    tuple: The next position (x, y) the animal moves to, or None if there is no valid move.
    """
    current_char = data[node]
    around_positions = get_around_positions(node)

    # Function to determine if the current piece can connect to the next one
    def can_connect(current, next_char):
        if current == 'L':
            return next_char in ['-', '7', 'J']
        elif current == 'J':
            return next_char in ['-', 'L', 'F']
        elif current == '7':
            return next_char in ['|', 'F', 'J']
        elif current == 'F':
            return next_char in ['|', '7', 'L']
        elif current == '|':
            return next_char in ['7', 'F', 'J', 'L']
        elif current == '-':
            return next_char in ['L', 'J', 'F', '7']
        else:
            return False

    for pos in around_positions:
        if pos in data and can_connect(current_char, data[pos]):
            return pos

    return None

def get_initial_directions(start_node, data):
    """
    Determine the possible initial directions from the start node.

    Args:
    start_node (tuple): The starting position of the animal (x, y), marked as 'S'.
    data (dict): The dictionary containing the matrix data.

    Returns:
    list: A list of tuples representing the possible initial direction positions.
    """
    x, y = start_node
    possible_directions = []
    adjacent_positions = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    # Connectivity rules for starting position 'S'
    valid_connectors = ['|', '-', 'L', 'J', 'F', '7']

    for pos in adjacent_positions:
        if data.get(pos) in valid_connectors:
            possible_directions.append(pos)

    return possible_directions


def recorrer_nodo(nodo, data, result, distancia):

    if data[nodo] == "S":
        result[nodo] = distancia
        print("jeje")
        print(get_initial_directions(nodo, data))

    
    alrededorPositions = get_around_positions(nodo)




    

def main():
    data = modify_input(readInput("Day10/input2.txt"), 1)
    
    result = {}

    recorrer_nodo(START_POSITION,data, result, 0)

    return data

print(main())
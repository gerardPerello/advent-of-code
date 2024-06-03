
from functools import reduce
import operator

def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input

def process_set(set_data):
  # Splitting the data by commas
  items = set_data.split(',')
  set_dict = {"red": 0, "green": 0, "blue": 0}
  for item in items:
      # Extracting color and number
      parts = item.strip().split()
      if len(parts) == 2:
          number, color = parts
          set_dict[color] = int(number)
  return set_dict

def process_game_data(game_data):
  # Splitting the data by ';'
  sets = game_data.split(';')

  # Removing the game number and colon from the first set
  game_number, sets[0] = sets[0].split(':')

  # Extracting the game number
  game_number = game_number.split()[-1]

  processed_sets = [process_set(set_data) for set_data in sets]

  return game_number, processed_sets


def is_set_possible(set):
  for key in set.keys():
      if(CONTAINED_CUBES[key] < set[key]):
         return False
  return True
  

def is_game_possible(game):
  
  for set in game:
    if not is_set_possible(set):
      return False
  return True

def minimum_cubes_per_set(set):
  minimum_cubes = dict()
  for key in set.keys():
    if key not in minimum_cubes or minimum_cubes[key] < set[key]:
        minimum_cubes[key] = set[key]
  return minimum_cubes

def minimum_cubes_per_game(game):
  minimum_cubes = dict()
  for set in game:
    minimum_cubes_set = minimum_cubes_per_set(set)
    print("minimum_cubes_set")
    print(minimum_cubes_set)
    for key in minimum_cubes_set.keys():
      if key not in minimum_cubes or minimum_cubes[key] < minimum_cubes_set[key]:
          minimum_cubes[key] = minimum_cubes_set[key]
  
  return minimum_cubes


CONTAINED_CUBES = {"red": 12, "green":13, "blue":14}


def main():
  data = readInput("Day2\input.txt")[:-1]
  possibleGames = dict()
  
  for game in data:
     number, game_data = process_game_data(game)
     possibleGames[number] = is_game_possible(game_data)
  
  sum_of_keys = sum(int(key) for key, value in possibleGames.items() if value)
  
  total = 0

  for game in data:
     number, game_data = process_game_data(game)
     print(game_data)
     print("hola")
     minimum_cubes = minimum_cubes_per_game(game_data)
     print(minimum_cubes)
     mult = reduce(operator.mul, minimum_cubes.values(), 1)
     print(mult)
     total += mult
  return (total, sum_of_keys)
     

print(main())
   

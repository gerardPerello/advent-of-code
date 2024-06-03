def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, part):
    dictio = {}
    for index, pair in enumerate(input_list):
        cards, bid = pair.split()

        # Counting the occurrences of each card
        cards_count = {}
        for card in cards:
            if card in cards_count:
                cards_count[card] += 1
            else:
                cards_count[card] = 1

        counts = {}
        for card, count in cards_count.items():
            if count in counts:
                counts[count].add(card)
            else:
                counts[count] = {card}

        # Adding the counts to the main dictionary
        dictio[index + 1] = {
            "cards_ordered": list(cards), 
            "bid": int(bid), 
            "cards_count": cards_count,
            "counts": counts
        }
    
    return dictio


def get_points_by_type(index, counts):
  contiene = set(counts.keys())

  #5 iguales
  if 5 in contiene:
      categories[1].add(index)
      return

  if 4 in contiene:
      categories[2].add(index)
      return
  
  if 3 in contiene:
      if 2 in contiene:
          categories[3].add(index)
          return
      else:
          categories[4].add(index)
          return
  
  if 2 in contiene:
      if(len(counts[2]) == 2):
          categories[5].add(index)
          return
      else:
          categories[6].add(index)
          return
  categories[7].add(index)
  return

def get_points_by_type_2(index, counts):
  contiene = set(counts.keys())

  #5 iguales
  if 5 in contiene:
      categories[1].add(index)
      return

  if 4 in contiene:
      if "J" in counts[1]:
        categories[1].add(index)
      else:
        categories[2].add(index)
      return
  
  if 3 in contiene:
      if 2 in contiene:
          if "J" in counts[2]:
            categories[1].add(index)
          else:
            categories[3].add(index)
          return
      else:
          if "J" in counts[1]:
            categories[2].add(index)
          else:
            categories[4].add(index)
          return
  
  if 2 in contiene:
      
      if(len(counts[2]) == 2):
          if "J" in counts[2]:
            categories[2].add(index)
          elif "J" in counts[1]:   
            categories[3].add(index)
          else:
            categories[5].add(index)
          return
      else:
          if "J" in counts[2]:
            categories[4].add(index)
          elif "J" in counts[1]:   
            categories[4].add(index)
          else:
            categories[6].add(index)
          return
  if "J" in counts[1]:
    categories[6].add(index)
  else:
    categories[7].add(index)
  return


def card_value(card, part=1):
    """Maps a card to its value according to the specified order."""
    order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
             'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if part == 2:
        order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
             'T': 10, 'J': 1, 'Q': 11, 'K': 12, 'A': 13}
    return order[card]



def sort_hands(hands,part):
    """Sorts a list of hands of cards."""
    return sorted(hands, key=lambda hand: [card_value(card,part) for card in hand], reverse=True)

def sort_hands_by_id(hands_dict,part):
    """Sorts the IDs of hands based on the hands they represent."""
    return sorted(hands_dict.keys(), key=lambda id: [card_value(card,part) for card in hands_dict[id]], reverse=True)


def order_hands(data,part):
    for category in categories.keys():
         categoryData = {item:data[item]['cards_ordered'] for item in categories[category]}
         print(categoryData)
         categoriesOrdered[category] = sort_hands_by_id(categoryData,part)

def join_categories():

    finalList = []

    for category in categoriesOrdered.keys():
        finalList += categoriesOrdered[category]
    
    return finalList

def calculate(data, finalList):
    maximum = len(finalList)
    finalCalculation = 0
    for i in range(len(finalList)):
        finalCalculation += (maximum - i) * data[finalList[i]]["bid"]

    return finalCalculation
def main():
  global categories
  global categoriesOrdered
  categories = {i:set() for i in range(1,8)}
  categoriesOrdered = {i:[] for i in range(1,8)}
  data = modify_input(readInput("Day7\input2.txt"), 1)
  print(data)
  for index in data.keys():
      hand = data[index]
      get_points_by_type_2(index, hand["counts"])
  
  order_hands(data,2)
  finalList = join_categories()
  finalCalculation = calculate(data, finalList)
  print(categories)
  print(categoriesOrdered)
  print(finalList)
  return finalCalculation

print(main())
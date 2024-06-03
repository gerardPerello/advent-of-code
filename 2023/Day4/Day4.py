def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list):
    modified_list = input_list

    return modified_list


def extract_card_data(cards):
    card_dict = {}
    
    for card in cards:
        
        parts = card.split('|')
        if len(parts) == 2:
            
            card_number = parts[0].split(':')[0].split()[-1]
            
            winning_list = [int(num) for num in parts[0].split(':')[1].split() if num.isdigit()]
            my_numbers = [int(num) for num in parts[1].split() if num.isdigit()]
            
            card_dict[int(card_number)] = {"winningList": winning_list, "myNumbers": my_numbers}
    
    return card_dict 

def calculate_card_punct(card_number, card_dict, card_punctuations, card_copies):
    
    winningNumbersSet, myNumbers = set(card_dict['winningList']), card_dict['myNumbers']

    card_score = 0
    n_winning_cards = 0

    for number in myNumbers:
        
        if number in winningNumbersSet:
            
            n_winning_cards += 1
            
            if card_score == 0:
                card_score = 1
            
            else:
                card_score = card_score * 2

    card_punctuations[card_number] = card_score

    print("next")
    print(f"card_number: {card_number}")
    print(f"Winning: {n_winning_cards}")
    if card_number not in card_copies:
        card_copies[card_number] = 1
    else:
        card_copies[card_number] += 1

    print(f"card_copies: {card_copies}")
    
    
    
    for i in range(1, n_winning_cards + 1):
        
        if card_number + i not in card_copies:
            
            card_copies[card_number + i] = card_copies[card_number]
        
        else:
            
            card_copies[card_number + i] += card_copies[card_number]

    print(f"card_copies after: {card_copies}")
    
      

def main():

  data = modify_input(readInput("Day4\input.txt"))
  #15429487
  #15429487
  print(data)
  
  card_punctuations = {}
  card_copies = {}

  card_dict = extract_card_data(data)

  for card_number in card_dict:
      calculate_card_punct(card_number, card_dict[card_number], card_punctuations, card_copies)

  
  print(f"Puntuactions: {card_punctuations}")
  print(f"Card copies: {card_copies}")


  total_score_part1 = sum(card_punctuations.values())
  total_score_part2 = sum(card_copies.values())
  return total_score_part1, total_score_part2

print(main())
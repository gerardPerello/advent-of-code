def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, combine=False):
    time_data = input_list[0].split()[1:]  # Skip the first element 'Time:'
    distance_data = input_list[1].split()[1:]  # Skip the first element 'Distance:'

    if combine:
    # Combine all time and distance values into single entries
        combined_time = ''.join(time_data)
        combined_distance = ''.join(distance_data)

        # Convert combined string data to integers
        time_data = [int(combined_time)]
        distance_data = [int(combined_distance)]
    else:
        # Convert string data to integers
        time_data = [int(time) for time in time_data]
        distance_data = [int(distance) for distance in distance_data]

    # Create a dictionary for each race
    races = {}
    for i, (time, distance) in enumerate(zip(time_data, distance_data)):
        races[i + 1] = {"t": time, "d": distance}

    return races




def distance(holdedButtonTime, raceTime):
    if holdedButtonTime == 0 or holdedButtonTime >= raceTime:
        return 0
    
    restantTime = raceTime - holdedButtonTime

    return restantTime * holdedButtonTime

def win(distance, distanceToBeat):

    return distance > distanceToBeat

def testRace(race_id, race):

    max_time , distance_to_beat = race.values()

    if race_id not in dists:
        dists[race_id] = list()
        wins[race_id] = list()

    """ print(dists[race_id]) """
    
    theRange = (max_time+1)//2
    if (max_time % 2 == 0):
        theRange += 1
    for i in range(theRange):

        my_d = distance(i, max_time)

        dists[race_id].append((my_d))

        wins[race_id].append(win(my_d, distance_to_beat))





def main():
  
  global wins
  global dists 

  wins = {}
  dists = {}

  data = modify_input(readInput("Day6\input.txt"), True)
  print(data)
  for id in data.keys():
      testRace(id, data[id])
  #15429487
  #15429487
  """ print(dists) """
  total = 1
  for id in wins.keys():
      """ print(dists[id])
      print(data[id]["t"]) """
      if data[id]["t"] % 2 != 0:
          newTot = sum(wins[id]*2)
      else:
          newTot = sum([wins[id][i] for i in range(len(wins[id])-1)]*2) + wins[id][-1]
      total *= newTot
  return total
  

print(main())
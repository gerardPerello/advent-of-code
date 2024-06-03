def readInput(path):
    input =  "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list):
    modified_list = input_list

    return modified_list

def extract_data_to_dict(data_list):
    result_dict = {}
    seeds = []
    temp_dict = {}
    key_name = ""
    for item in data_list:
        # Check for seeds
        if "seeds:" in item:
            seeds = item.replace("seeds: ", "").split()
            seeds = [int(seed) for seed in seeds]
        # Check for empty line
        elif item == "":
            if key_name:
                result_dict[key_name] = temp_dict
                temp_dict = {}
            key_name = ""
        else:
            # Check for map definition
            if "-to-" in item:
                parts = item.split("-to-")
                key_name = parts[0]
                temp_dict = {"to": parts[1].split(" ")[0], "maps": []}
            else:
                # Map data
                d, o, r = map(int, item.split())
                temp_dict["maps"].append({"d": d, "o": o, "r": r})

    # Add the last map to the result dictionary
    if key_name:
        result_dict[key_name] = temp_dict

    return seeds, result_dict

def from_to(initNumb, maps):
    
    for mapa in maps:
        
        """ print(f"o:{mapa['o']}, d:{mapa['d']}, r:{mapa['r']}, init: {initNumb}") """
        
        if mapa['o'] <= initNumb <= mapa['o'] + mapa['r']:
            """ print("IM HERE")
            print(mapa['d'] + initNumb - mapa['o'] ) """
            return mapa['d'] + initNumb - mapa['o'] 
    
    else:
        
        return initNumb

def ending_location(seed, dict):
    
    location = seed
    """ print(f"Seed: {location}") """
    
    for key in dict.keys():
        
      location = from_to(location, dict[key]['maps'])

      """ print(f"{dict[key]['to']} : {location}") """
    
    return location

def from_to2(locations, maps):
    
    """ print(maps) """
    changes = []
    notChanged = locations

    for mapa in maps:
        
        
        """ print(f"d:{mapa['d']},o:{mapa['o']}, r:{mapa['r']}")
        print(f"init:{locations}") """

        # I can't do anything, no changes.
        if max(locations) < mapa['o']:
            locations = locations
        # Same
        elif min(locations) > mapa['o'] + mapa['r']:
            locations = locations
        
        else:
            
            init_ranges = set([mapa['o'] + i for i in range(mapa['r'])])

            intersect = locations & init_ranges

            if intersect:
              """ print("intersect") """
              change_dict = dict()

              for i in range(mapa['r']):
                  change_dict[mapa['o'] + i] = mapa['d'] + i

              notChanged = notChanged - intersect
              changedIntersect = {change_dict[key] for key in intersect}

              #location = changedIntersect | diff
              changes.append(changedIntersect)

              """ print(f"from:{intersect}")
              print(f"to:{changedIntersect}") """
    
    final = set()
    if changes:
      """ print(f"changes:{changes}")
      print(f"noChanges:{notChanged}") """
      for item in changes:
          final = final | item
      final = final | notChanged 
    else:
        final = locations
    
    
    """ print(f"final:{final}")
    print(f"Len:{len(final)}") """
    return final

def ending_location2(seedOrigin,seedRange, dict):
    
    locations = set([seedOrigin + i for i in range(seedRange)])
    print(f"Seed: {locations}")
    
    for key in dict.keys():
      print(dict[key]['to'])
      locations = from_to2(locations, dict[key]['maps'])

      print(f"{dict[key]['to']} : {locations}")
    
    return locations

def changeLocation(locations, mapa):
    newLocations = dict()
    rangesNow = sum([i[1] for i in locations.values()])
    for seedOrigin in locations.keys():
            

            seedRange = locations[seedOrigin][1]

            if seedOrigin == 54:
                print("ahora")

            if not locations[seedOrigin][0]:

                """ print(seedOrigin, seedRange) """
                
                # Cubrimos los casos donde el origen del map es mas grande que la semilla maxima
                # Cubrimos los casos donde la semilla mas minima es mas grande que el final del map.
                if seedOrigin + seedRange <= mapa['o'] or seedOrigin >= mapa['o'] + mapa['r']:

                    """ print("Se queda igual") """
                    newLocations[seedOrigin] = (False,seedRange)
                
                else:

                    # En caso de que el origen del map sea mas pequeño o igual que la semilla origen
                    if mapa['o'] <= seedOrigin: # ---------- o -------- seedOrigin  -------------
                    
                        # En caso de que el map maximo sea mayor que la semilla maxima (quiere decir que cambiamos todo) 
                        if mapa['o'] + mapa['r'] >= seedOrigin + seedRange: # ---------- o -------- seedOrigin ----------seedOrigin+SeedRange -------- o + r
                            
                            """ print("caso 1") """
                            # Por lo tanto cambiamos la semilla original y le ponemos el mismo range
                            newLocations[mapa['d'] + seedOrigin - mapa['o'] ] = (True,seedRange)

                            """ print(f"New locations:{newLocations}") """
                    
                        # En caso de que el map maximo sea mas pequeño que la semilla maxima
                        if mapa['o'] + mapa['r'] < seedOrigin + seedRange: # ---------- o -------- seedOrigin -------- o + r ----------seedOrigin+SeedRange 
                            
                            """ print("Caso 2") """
                            # Cojemos el range solapado:
                            changedRange = mapa['o'] + mapa['r'] - seedOrigin

                            # Mapeamos el location solapado
                            newLocations[mapa['d'] + seedOrigin - mapa['o']] = (True,changedRange)

                            # Dejamos igual el otro
                            newLocations[seedOrigin + changedRange] = (False,seedRange - changedRange )
 

                            """ print(f"New locations:{newLocations}") """
                        


                    # En caso de que el map sea mas grande que el origin.
                    elif mapa['o'] > seedOrigin: # ---------- seedOrigin -------- o -------------

                        # Caso de que el range del mapeo no llegue a la ultima semilla (3 grupos) 
                        if mapa['o'] + mapa['r'] < seedOrigin + seedRange: # ---------- seedOrigin -------- o -------- o + r -------so+sr
                            
                            """ print("Caso 3") """
                            # First number changed, also the range of the first group.
                            #changedOrigin = mapa['o'] - seedOrigin
                            firstNotChangedRange = mapa['o'] - seedOrigin
                            
                            # First not changed group
                            newLocations[seedOrigin] = (False,firstNotChangedRange)

                            #Changed group
                            newLocations[mapa['d']] = (True,mapa['r'])

                            # Second not changed group
                            newLocations[mapa['o'] + mapa['r']] = (False,seedRange - firstNotChangedRange - mapa['r'])

                            """ print(f"New locations:{newLocations}") """
                        # Caso de que el range del mapeo llegue a la ultima semilla (2 grupos)

                        if mapa['o'] + mapa['r'] >= seedOrigin + seedRange:
                            
                            """ print("Caso 4") """
                            notChangedRange = mapa['o'] - seedOrigin

                            # Not changed group
                            newLocations[seedOrigin] = (False,notChangedRange)

                            # Changed group
                            newLocations[mapa['d']] = (True,seedRange - notChangedRange)


                            """ print(f"New locations:{newLocations}") """

            else:
                newLocations[seedOrigin] = (False,seedRange)
    
    """ print(f"Nos vamos:{newLocations}") """
    rangesFinal = sum([i[1] for i in newLocations.values()])
    if(rangesNow != rangesFinal):
        cuenta.append(rangesFinal - rangesNow)
        print(f"DIFFERENT HERE!!!!! final:{rangesFinal} and now:{rangesNow}")
    return newLocations
def from_to3(locations, maps):
    
    print(maps)
    
    

    for mapa in maps:
        
        
        """ print(f"d:{mapa['d']},o:{mapa['o']}, r:{mapa['r']}")
        print(f"init:{locations}") """

        locations = changeLocation(locations, mapa)

    
    for key in locations.keys():
        locations[key] = (False,locations[key][1])

    """ print(f"Nos vamos DEL TODO:{locations}") """
    return locations
            



def ending_location3(seedOrigin,seedRange, dictio):

    
    
    
    print(f"Seed: {seedOrigin}, Range:{seedRange}")
    locations = dict()
    locations[seedOrigin] = (False, seedRange)

    print(locations)
    
    for key in dictio.keys():
      print(dictio[key]['to'])
      locations = from_to3(locations, dictio[key]['maps'])

      print(f"{dictio[key]['to']} : {locations}")
    
    return locations


def main():

  data = modify_input(readInput("Day5\input.txt"))

  seeds, dict = extract_data_to_dict(data)

  global cuenta 

  cuenta = []

  finalLocations = {}
  for seed in seeds:
      finalLocations[seed] = ending_location(seed, dict)

  seedsPairs = [(seeds[i],seeds[i+1]) for i in range(0,len(seeds),2)]
  finalLocations2 = {}
  print(seedsPairs)
  for (seedOrigin, seedRange) in seedsPairs:
        print("NEW")
        finalLocations2[seedOrigin] = ending_location3(seedOrigin, seedRange, dict)

  
  for dictioKey in finalLocations2.keys():
      print(f"Seed: {dictioKey}, and minimum locations => {min(finalLocations2[dictioKey].keys())}")

  returnpart2 = min([min(item) for item in finalLocations2.values()])
  print(cuenta)
  return min(finalLocations.values()), returnpart2


print(main())
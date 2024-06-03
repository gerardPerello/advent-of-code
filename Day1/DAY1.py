import re
fp = open("Day1\input.txt")
sum = 0
numbersDict = {
   "zero":0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# Add keys for numbers as strings with their integer values
for i in range(10):
    numbersDict[str(i)] = i

print(numbersDict)

for i, line in enumerate(fp):
  numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)

  reversed_line = line[::-1]
  reversed_numbers = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', reversed_line)

  reversed_numbers = [num[::-1] for num in reversed_numbers]
  
  if len(numbers) > 0:
    intNumbers = [numbersDict[number] for number in numbers]
    intNumbersRev = [numbersDict[number] for number in reversed_numbers]
    toSum = int(str(intNumbers[0])+str(intNumbersRev[0]))
    sum += toSum
    with open("Day1\data.txt","a") as myFile:
       
      myFile.write(str(toSum)+"\n")

print(sum)
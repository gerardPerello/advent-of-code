fp = open("Day1\data.txt").readlines()
fp2 = open("Day1\data2.txt").readlines()

for i in range(len(fp)):
  if(fp[i] != fp2[i]):
    print(i)
    print(fp[i])
    print(fp2[i])
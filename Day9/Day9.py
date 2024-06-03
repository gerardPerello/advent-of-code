import math
def readInput(path):
    input = "".join(open(path).readlines()).split('\n')
    return input


def modify_input(input_list, part):
    dictio = {}
    for index,seq in enumerate(input_list):
        seqList = [int(i) for i in seq.split()]
        dictio[index+1] = seqList

    return dictio

def is_zero_list(setList):
    if 0 in setList and len(setList) == 1:
        return True
    
def calculate_next_seq(seq):
    return [seq[i] - seq[i-1] for i in range(1, len(seq))]

def dec_to_0s(seq):
    print(seq)
    punct = seq[-1]
    punct2 = [seq[0]]
    nextSeq = calculate_next_seq(seq)
    print(f"1: {nextSeq}")
    while not is_zero_list(set(nextSeq)):
        punct += nextSeq[-1]
        punct2.append(nextSeq[0])
        nextSeq = calculate_next_seq(nextSeq)
        print(f"1: {nextSeq}")
    print(f"Total:{punct2}")
    punc2 = 0
    for i in range(len(punct2),0,-1):
        print(punc2)
        punc2 = punct2[i-1] - punc2
    print(f"Final:{punc2}")
    return punc2

def main():
    data = modify_input(readInput("Day9/input.txt"), 1)
    total = 0
    for index in data:
        seq = data[index]
        total += dec_to_0s(seq)

    return total

print(main())
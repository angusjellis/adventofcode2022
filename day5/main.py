from collections import deque

def transpose_string(string):
    return string[::-1]

with open("input.txt", "r") as input_file:
    stacks, instructions = input_file.read().split("\n\n")

    stacks = stacks.splitlines()
    stacks.reverse()
    stacks_object = {}
    for s in stacks:
        for l in s:
            if l.isdigit():
                stacks_object[s.index(l)] = deque(l)
                new = deque(l)
                
            elif s.index(l) % 4 == 1:
                stacks_object[s.index(l)].append(l)

    print(stacks_object)
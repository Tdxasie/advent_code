with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()


shit = [i for i in lines[0].split(" ") if i != ""]
operations = [[] for i in range(len(shit))]
for line in lines:
    shit = [i for i in line.split(" ") if i != ""]
    for i, op in enumerate(operations):
        op.append(shit[i])

from functools import reduce

tot = 0

for op in operations:
    numbers = [int(i) for i in op[:-1]]
    tot += reduce(lambda x, y: eval(f"{x}{op[-1]}{y}"), numbers)

print(tot)

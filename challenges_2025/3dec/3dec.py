with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

tot = 0

for line in lines:
    line = [int(i) for i in line]

    a = max(line[:-1])
    b = max(line[line.index(a) + 1 :])
    tot += int(f"{a}{b}")

print(tot)

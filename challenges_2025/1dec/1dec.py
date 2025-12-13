with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

dial = 50

count = 0

for line in lines:
    line = line.replace("L", "-")
    line = line.replace("R", "+")
    dial += eval(line)
    dial %= 100
    if dial == 0:
        count += 1

print(count)

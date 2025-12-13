with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()


ranges = []
shesfreshsofreshexcitingtinlinninin = 0
for line in lines:
    if "-" in line:
        a, b = line.split("-")
        ranges.append(range(int(a), int(b)))
    elif line == "":
        continue
    else:
        ingredient = int(line)
        for range in ranges:
            if ingredient in range:
                shesfreshsofreshexcitingtinlinninin += 1
                break

print(shesfreshsofreshexcitingtinlinninin)

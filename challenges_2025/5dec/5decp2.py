with open("ex.txt", "r") as infile:
    lines = infile.read().splitlines()


ranges = []
shesfreshsofreshexcitingtinlinninin = set()
for line in lines:
    if "-" in line:
        a, b = line.split("-")
        a, b = int(a), int(b)

        ranges.append((a, b))


def intersect(range1, range2):
    return (
        (range1[0] in range(range2[0], range2[1]))
        or (range1[1] in range(range2[0], range2[1]))
        or (range2[0] in range(range1[0], range1[1]))
        or (range2[1] in range(range1[0], range1[1]))
    )


# a = min(range1[0], range2[0])
# b = max(range1[1], range2[1])

sdf = set()

for range1 in ranges:
    for range2 in ranges:
        if intersect(range1, range2):
            a = min(range1[0], range2[0])
            b = max(range1[1], range2[1])
            sdf.add((a, b))
            print(sdf)

thoth = 0
for range in sdf:
    thoth += range[1] - range[0] + 1


print(thoth)

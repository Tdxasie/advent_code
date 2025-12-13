import re

with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()


nb_cols = len(lines[0])
nb_lines = len(lines)


buffer = "." * nb_cols

lines.insert(0, buffer)

lines.append(buffer)

new_lines = []
for line in lines:
    new_lines.append("." + line + ".")


tot = 0
is_valid = False
digits = ""
for x in range(nb_cols):
    for y in range(nb_lines):
        idxx = x + 1
        idxy = y + 1

        char = new_lines[idxx][idxy]

        if char.isdigit():
            digits += char
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    char = new_lines[idxx - a][idxy - b]
                    if not char.isdigit() and char != ".":
                        is_valid = True
        else:
            if is_valid:
                is_valid = False
                tot += int(digits)
            digits = ""

print(tot)

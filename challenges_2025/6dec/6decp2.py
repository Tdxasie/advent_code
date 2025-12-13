with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

new_line = ""
for char in lines[-1]:
    if char != " ":
        operator = char
        new_line += "="
    else:
        new_line += operator

lines[-1] = new_line

shit = [i for i in lines[0].split(" ")]
operations = [[] for i in range(len(lines[0]))]
for line in lines:
    shit = [i for i in line.split(" ")]
    for i, op in enumerate(operations):
        op.append(line[i])


tot = 0
temp_tot = 0
operator = ""
for op in operations[::-1]:
    if all(i == " " for i in op[:-1]):
        continue

    val = int("".join(op[:-1]))
    if temp_tot == 0:
        temp_tot = val
        operator = op[-1]
    else:
        temp_tot = eval(f"{temp_tot}{operator}{val}")
        if op[-1] == "=":
            operator = ""
            tot += temp_tot
            temp_tot = 0
print(tot)

with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()


nb_cols = len(lines[0])
nb_lines = len(lines)


buffer = "." * nb_cols

lines.insert(0, buffer)

lines.append(buffer)

new_lines = []
for line in lines:
    new_lines.append(list("." + line + "."))

a = ""
a.isnumeric

tot = 0
ratio = 0
count = 0
for x in range(nb_cols):
    for y in range(nb_lines):
        idxx = x + 1
        idxy = y + 1

        char = new_lines[idxx][idxy]
        if char == "*":
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    char = new_lines[idxx - a][idxy - b]
                    if char.isdigit():
                        # find full digits and replace them by .
                        # look for . left
                        print(char + "^")
                        digits = ""
                        q = 1
                        while True:
                            if not new_lines[idxx - a][idxy - b - q].isdigit():
                                break
                            q += 1
                            print(new_lines[idxx - a][idxy - b - q], idxy - b - q)
                        p = 1
                        while True:
                            if not new_lines[idxx - a][idxy - b - q + p].isdigit():
                                break
                            digits += new_lines[idxx - a][idxy - b - q + p]
                            new_lines[idxx - a][idxy - b - q + p] = "."
                            p += 1
                        if digits:
                            count += 1
                            ratio *= int(digits)
                print("####")
            print("-------")
        else:
            if count > 1:
                tot += ratio
            ratio = 1
            count = 0

print(tot)

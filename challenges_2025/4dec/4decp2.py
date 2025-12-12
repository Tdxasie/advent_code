with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

kernels = [
    [
        ["@", "@", "@"],
        ["@", "^", "@"],
        ["@", "@", "@"],
    ],
]

nb_cols = len(lines[0])
nb_lines = len(lines)

# padding

buffer = "X" * nb_cols

lines.insert(0, buffer)
lines.append(buffer)

new_lines = []
for line in lines:
    new_lines.append("X" + line + "X")


def mul(kernel, search_zone):
    tot = 0
    if search_zone[1][1] != "@":
        return 9
    for i in range(3):
        for j in range(3):
            tot += 1 if (kernel[i][j] == search_zone[i][j]) else 0
    return tot


def caca(new_lines, tot):
    valid = []
    for x in range(nb_cols):
        for y in range(nb_lines):
            idxx = x + 1
            idxy = y + 1

            search_zone = [
                new_lines[idxx - 1][idxy - 1 : idxy + 2],
                new_lines[idxx][idxy - 1 : idxy + 2],
                new_lines[idxx + 1][idxy - 1 : idxy + 2],
            ]

            # print(search_zone)

            for kernel in kernels:
                if mul(kernel, search_zone) < 4:
                    tot += 1
                    valid.append([idxx, idxy])
    return valid, tot


def cacarec(tot):
    valid, tot = caca(new_lines, tot)
    if len(valid) == 0:
        return tot

    for pedro in valid:
        a = list(new_lines[pedro[0]])
        a[pedro[1]] = "."
        new_lines[pedro[0]] = "".join(a)

    print(tot)
    cacarec(tot)


tot = cacarec(0)


print(tot)

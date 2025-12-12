with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

lines: list[str]
res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            for a in range(i - 1, -1, -1):
                if lines[a][j] == "S":
                    lines[i] = lines[i][: j - 1] + "S^S" + lines[i][j + 2 :]
                    res += 1
                    break
                if lines[a][j] == "^":
                    break


print(res)

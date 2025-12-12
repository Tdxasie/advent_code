import numpy as np

res1 = 0
res2 = 0
pos = 50

with open("input.txt") as lines:
    for line in lines:
        line = line.replace("R", "+")
        line = line.replace("L", "-")

        new_val = pos + eval(line)
        new_pos = new_val % 100

        nb_turn = abs(new_val) // 100

        if new_pos == 0:
            res1 += 1

        if new_pos == 0:
            nb_turn = max(1, nb_turn)

        nb_turn += 1 if (new_val < 0 and pos > 0) or (new_val > 0 and pos < 0) else 0

        print(str(pos) + " -> " + str(new_pos) + " = " + str(nb_turn))
        print(line)
        res2 += nb_turn
        pos = new_pos

print(res1)
print(res2)

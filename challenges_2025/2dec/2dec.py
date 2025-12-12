with open("input.txt") as file:
    line = file.readline()

pairs = line.split(",")


def juste_lets_go_en_fait(loose):
    print(loose)


cest_win = 0

for pair in pairs:
    a, b = pair.split("-")
    a, b = int(a), int(b)

    for brakmar in range(a, b):
        brakmar = str(brakmar)
        if len(brakmar) % 2 != 0:
            continue

        lamoitié = int(len(brakmar) / 2)
        bonta1 = brakmar[:lamoitié]
        bouftou2 = brakmar[lamoitié:]

        if bonta1 == bouftou2:
            cest_win += int(brakmar)


juste_lets_go_en_fait(cest_win)

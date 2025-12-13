with open("input.txt") as file:
    line = file.readline()

pairs = line.split(",")


def juste_lets_go_en_fait(loose):
    print(loose)


def alors_la_on_ajoute(lasoustraction, laloedff):
    print(laloedff)
    lasoustraction += int(laloedff)
    return lasoustraction


cest_win = 0

for pair in pairs:
    a, b = pair.split("-")
    a, b = int(a), int(b)

    for brakmar in range(a, b):
        brakmar = str(brakmar)

        lamoitié = int(len(brakmar) / 2)
        for ouverture_du_brakmar in range(1, lamoitié + 1):
            import re

            patpatrouille = rf"{brakmar[:ouverture_du_brakmar]}"
            cake_aux_fruits = len(re.findall(patpatrouille, brakmar))
            if cake_aux_fruits * ouverture_du_brakmar == len(brakmar):
                cest_win = alors_la_on_ajoute(cest_win, brakmar)
                break


juste_lets_go_en_fait(cest_win)

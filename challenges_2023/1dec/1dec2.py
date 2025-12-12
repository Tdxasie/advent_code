with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def search(line: str):
    for char in line:
        if char.isdigit():
            return int(char)
    for key, val in numbers.items():
        if key in line:
            return val
    return False


tot = 0
for line in lines:
    digit1 = 0
    digit2 = 0
    for i in range(len(line) + 1):
        if digit1 := search(line[:i]):
            break

    for i in range(len(line)):
        if digit2 := search(line[-i - 1 :]):
            break
    tot += digit1 * 10 + digit2

print(tot)

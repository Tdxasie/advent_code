with open("ex.txt", "r") as infile:
    lines = infile.read().splitlines()

from dataclasses import dataclass


@dataclass
class Node:
    coords: list[int]
    id: int
    neighbors: set


adjacency_list: list[Node] = []

node_count = 0

res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            for a in range(i - 1, -1, -1):
                if lines[a][j] == "S":
                    lines[i] = lines[i][: j - 1] + "S^S" + lines[i][j + 2 :]
                    res += 1
                    node_count += 1
                    source = 
                    new_node = Node([i, j], node_count, set())
                    break
                if lines[a][j] == "^":
                    break

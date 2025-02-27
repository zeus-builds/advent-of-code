lines = None

with open("input.txt", "r") as file:
    lines = file.readlines()

first, second = [], []
for line in lines:
    line = line[:-1]
    a, b = line.split("   ")
    first.append(int(a))
    second.append(int(b))

first.sort()
second.sort()

res = 0
for i in range(len(first)):
    res += abs(first[i] - second[i])

print(f"Part 1: {res}")
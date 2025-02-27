from collections import defaultdict

lines = None

with open("input.txt", "r") as file:
    lines = file.readlines()

first, count = [], defaultdict(int)
for line in lines:
    line = line[:-1]
    a, b = line.split("   ")
    first.append(int(a))
    count[int(b)] += 1

res = 0

for num in first:
    res += count[num] * num

print(f"Part 2: {res}")

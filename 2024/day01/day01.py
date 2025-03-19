class Day01:
    
    def parse_input(self, file_name: str) -> list[tuple[int, int]]:
        number_pairs = []
        lines = None

        with open(file_name, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            line = line[:-1]
            a, b = line.split("   ")
            number_pairs.append((int(a), int(b)))
        
        return number_pairs

    
    def part1(self, number_pairs: list[tuple[int, int]]) -> int:
        first_sorted = sorted(x[0] for x in number_pairs)
        second_sorted = sorted(x[1] for x in number_pairs)

        res = 0

        for i in range(len(first_sorted)):
            res += abs(first_sorted[i] - second_sorted[i])

        return res
    

    def part2(self, number_pairs: list[tuple[int, int]]) -> int:
        first, count = [], {}

        for a, b in number_pairs:
            first.append(a)
            count[b] = count.get(b, 0) + 1
        
        res = 0
        
        for a in first:
            res += a * count.get(a, 0)
        
        return res


if __name__ == "__main__":
    solver = Day01()
    
    number_pairs = solver.parse_input("input.txt")
    
    print(f"Part 1: {solver.part1(number_pairs)}")
    print(f"Part 2: {solver.part2(number_pairs)}")

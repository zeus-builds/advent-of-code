class Day02:

    def parse_input(self, file_name: str) -> list[list[int]]:
        reports = []
        lines = None

        with open(file_name, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            line = [int(x) for x in line.split(' ')]
            reports.append(line)
        
        return reports

    def part1(self, reports: list[list[int]]) -> int:
        count = 0

        for levels in reports:
            is_increasing = True
            is_decreasing = True
            is_in_range = True

            for i in range(1, len(levels)):
                # check if it is increasing
                if levels[i] < levels[i - 1]:
                    is_increasing = False
                
                # check if it is decreasing
                if levels[i] > levels[i - 1]:
                    is_decreasing = False
                
                # check if it is in the range of [1, 3]
                diff = abs(levels[i] - levels[i - 1])
                if not 1 <= diff <= 3:
                    is_in_range = False

            if (is_increasing or is_decreasing) and is_in_range:
                count += 1
        
        return count

    def part2(self, reports: list[list[int]]) -> int:
        pass

if __name__ == "__main__":
    solver = Day02()

    input_data = solver.parse_input("input.txt")

    print(f"Part 1: {solver.part1(input_data)}")
    print(f"Part 2: {solver.part2(input_data)}")

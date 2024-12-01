from coordinates import Symbol, EngineValue


# parse the data file to get only the lines
def parse(filename):
    lines = []
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            lines = map(lambda n: n.rstrip(), contents)
            file.close()
    except OSError:
        print("Error in reading the file.")

    return list(lines)


def to_objects(grid):
    numbers = []
    symbols = []

    for y in range(0, len(grid)):
        curr_num = ""
        num_s = float("inf")
        for x in range(0, len(grid[0])):
            char = grid[y][x]
            if char.isnumeric():
                curr_num += char
                num_s = min(x, num_s)
                if x == 139 or not grid[y][x + 1].isnumeric():
                    numbers.append(EngineValue(y, num_s, x, curr_num))
                    curr_num = ""
                    num_s = float("inf")
            elif char != ".":
                symbols.append(Symbol(y, x, char))
    return (numbers, symbols)


def engine_sum(symbols, numbers):
    sum = 0
    for n in numbers:
        if any(n.isAdjacent(s) for s in symbols):
            sum += n.value()
    return sum


def gear_ratios(symbols, numbers):
    gear_ratio = 0
    for symbol in list(filter(lambda s: s.symbol() == "*", symbols)):
        adjacent_values = list(filter(lambda n: n.isAdjacent(symbol), numbers))
        if len(adjacent_values) == 2:
            gear_ratio += adjacent_values[0].value() * adjacent_values[1].value()
    return gear_ratio


def main():
    lines = parse("day3/data.txt")
    grid = [list(w) for w in lines]
    engine_objects = to_objects(grid)

    symbols = engine_objects[1]
    numbers = engine_objects[0]
    adjacent_sum = engine_sum(symbols, numbers)
    print(f"Sum of valid engine numbers: {adjacent_sum}")
    gear_sum = gear_ratios(symbols, numbers)
    print(f"Sum of valid gear ratios: {gear_sum}")


main()

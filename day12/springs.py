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


def valid_combinations(symbols, broken_sets):
    # if there are not question marks, check if the number and sequence of broken springs is valid

    if "?" not in symbols:
        broken_symbols = list(filter(lambda n: n != "", symbols.split(".")))
        broken_counts = list(
            zip(broken_sets, list(map(lambda n: len(n), broken_symbols)))
        )
        if (
            any(not i[0] == i[1] for i in broken_counts)
            or not len(broken_counts) == len(broken_sets)
            or not len(broken_symbols) == len(broken_sets)
        ):
            return 0
        else:
            return 1

    # if there are still question marks, convert the first available ? into . and #, and do recursion
    else:
        question_index = symbols.index("?")
        first_option = symbols[:question_index] + "." + symbols[question_index + 1 :]
        second_option = symbols[:question_index] + "#" + symbols[question_index + 1 :]
        return valid_combinations(first_option, broken_sets) + valid_combinations(
            second_option, broken_sets
        )


def main():
    lines = parse("day12/data.txt")
    combinations = 0
    for line in lines:
        broken_sets = list(map(lambda n: int(n), line.split()[1].split(",")))
        symbols = line.split()[0]
        spring_combinations = valid_combinations(symbols, broken_sets)
        combinations += spring_combinations
    print(f"Sum of the possible combinations: {combinations}")


main()

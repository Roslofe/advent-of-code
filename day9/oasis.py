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


def extrapolate(numbers):
    extrapolations = 0
    for reading in numbers:
        values = [list(map(lambda n: int(n), reading))]
        # first, create the differences
        while not all(n == 0 for n in values[-1]):
            curr_values = values[-1]
            differences = []
            for i in range(0, len(curr_values) - 1):
                differences.append(curr_values[i + 1] - curr_values[i])
            values.append(differences)
        values[-1].append(0)
        # add the extrapolations to each row
        for i in range(len(values) - 2, -1, -1):
            values[i].append(values[i + 1][-1] + values[i][-1])
        extrapolations += values[0][-1]
    return extrapolations


def main():
    numbers = list(map(lambda m: m.split(), parse("day9/data.txt")))
    extrapolations = extrapolate(numbers)
    print(f"The sum of extrapolations: {extrapolations}")


main()

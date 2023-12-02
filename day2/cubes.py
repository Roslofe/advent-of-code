from cube import Cube
import re


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

    return lines


def main():
    lines = parse("day2/data.txt")
    sum = 0
    for line in lines:
        split_line = line.split(": ")
        id = int(split_line[0].split()[1])
        as_cubes = list(
            map(
                lambda n: Cube(n.split()[0], n.split()[1]),
                re.split(", |; ", split_line[1]),
            )
        )
        if not any(cube.too_many() for cube in as_cubes):
            sum += id
    print(f"Sum of IDs from valid games: {sum}")


main()

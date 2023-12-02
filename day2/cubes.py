from cube import Cube
import re
from functools import reduce


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


# turn the line of data into a list of Cube objects
def as_cubes(line):
    return list(
        map(
            lambda n: Cube(n.split()[0], n.split()[1]),
            re.split(", |; ", line),
        )
    )


# calculate sum of all game IDs where none of the cube amounts go over the limit
def id_sum(lines):
    sum = 0
    for line in lines:
        split_line = line.split(": ")
        id = int(split_line[0].split()[1])
        cubes = as_cubes(split_line[1])
        if not any(cube.too_many() for cube in cubes):
            sum += id
    return sum


# calculate the sum of the powers of the smallest possible cube amounts in each game
def smallest_power(lines):
    sum = 0
    for line in lines:
        cubes = as_cubes(line.split(": ")[1])
        r = -1
        g = -1
        b = -1
        cubes_sorted = sorted(cubes, key=lambda x: x.amount())
        while cubes_sorted and (r == -1 or g == -1 or b == -1):
            curr_cube = cubes_sorted.pop()
            match curr_cube:
                case red if red.color() == "r":
                    r = max(r, red.amount())
                case green if green.color() == "g":
                    g = max(g, green.amount())
                case blue if blue.color() == "b":
                    b = max(b, blue.amount())
        sum += reduce(lambda x, y: x * y, filter(lambda x: not x == -1, [r, g, b]))
    return sum


def main():
    lines = parse("day2/data.txt")
    sum_id = id_sum(lines)
    smallest = smallest_power(lines)
    print(f"Sum of IDs from valid games: {sum_id}")
    print(f"Sum of the smallest possible powers: {smallest}")


main()

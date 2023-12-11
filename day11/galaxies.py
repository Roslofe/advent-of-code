from itertools import combinations


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


def galaxy_array(lines, ncr):
    galaxy_lines = [list(line) for line in lines]
    # store galaxy locations: x, y
    galaxies = []
    for y in range(0, len(galaxy_lines)):
        for x in range(0, len(galaxy_lines[0])):
            if galaxy_lines[y][x] == "#":
                galaxy_lines[y][x] = len(galaxies)
                galaxies.append([x, y])

    # find empty rows, edit the coordinates of affected galaxies
    increases = 0
    for i in range(0, len(galaxy_lines)):
        line = galaxy_lines[i]
        if not any(isinstance(n, int) for n in line):
            for galaxy in list(filter(lambda n: n[1] > i + increases, galaxies)):
                galaxy[1] += ncr
            increases += ncr

    # find empty columns, edit the coordinates of affected galaxies
    increases = 0
    for i in range(0, len(galaxy_lines[0])):
        if not any(isinstance(n, int) for n in [line[i] for line in galaxy_lines]):
            for galaxy in list(filter(lambda n: n[0] > i + increases, galaxies)):
                galaxy[0] += ncr
            increases += ncr

    return galaxies


def smallest_distance(lines, ncr):
    galaxies = galaxy_array(lines, ncr)
    galaxy_pairs = list(combinations(range(0, len(galaxies)), 2))
    shortest_sum = 0

    # compute the distance between each galaxy pair
    for pair in galaxy_pairs:
        start_g = galaxies[pair[0]]
        end_g = galaxies[pair[1]]
        distance = abs(end_g[0] - start_g[0]) + abs(end_g[1] - start_g[1])
        shortest_sum += distance
    return shortest_sum


def main():
    lines = parse("day11/data.txt")

    # short expansion
    small_expansion = smallest_distance(lines, 1)

    # large expansion
    large_expansion = smallest_distance(lines, 999999)

    print(f"Sum of shortest distances: {small_expansion}")
    print(f"Sum of shortest distances with large expansion: {large_expansion}")


main()

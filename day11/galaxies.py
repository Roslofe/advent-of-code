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


def galaxy_array(lines):
    galaxy_lines = [list(line) for line in lines]
    # find out the empty rows, and double them
    i = 0
    while i < len(galaxy_lines):
        if "#" not in galaxy_lines[i]:
            galaxy_lines.insert(i, ["."] * len(galaxy_lines[0]))
            i += 2
        else:
            i += 1

    # find out the empty columns, double them
    i = 0
    while i < len(galaxy_lines[0]):
        if "#" not in [line[i] for line in galaxy_lines]:
            for line in galaxy_lines:
                line.insert(i, ".")
            i += 2
        else:
            i += 1

    # store galaxy locations: x, y
    galaxies = []
    for y in range(0, len(galaxy_lines)):
        for x in range(0, len(galaxy_lines[0])):
            if galaxy_lines[y][x] == "#":
                galaxy_lines[y][x] = len(galaxies)
                galaxies.append((x, y))

    return galaxies


def main():
    lines = parse("day11/data.txt")
    galaxies = galaxy_array(lines)
    galaxy_pairs = list(combinations(range(0, len(galaxies)), 2))
    shortest_sum = 0

    # compute the distance between each galaxy pair
    for pair in galaxy_pairs:
        start_g = galaxies[pair[0]]
        end_g = galaxies[pair[1]]
        distance = abs(end_g[0] - start_g[0]) + abs(end_g[1] - start_g[1])
        shortest_sum += distance

    print(f"Sum of shortest distances: {shortest_sum}")


main()

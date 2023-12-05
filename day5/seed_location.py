from path import Path


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


def main():
    lines = parse("day5/data.txt")
    seeds = list(map(lambda n: int(n), lines[0].split()[1:]))
    init_mapping = {}
    for seed in seeds:
        init_mapping[seed] = seed
    path = Path(init_mapping)
    # gather the mappings in each attribute
    map_groups = []
    # destination, source, range
    current_ranges = []
    for line in lines[2:]:
        if line == "":
            map_groups.append(current_ranges)
            current_ranges = []
        elif line.split()[0].isnumeric():
            split_line = tuple(map(lambda n: int(n), line.split()))
            current_ranges.append(split_line)
    map_groups.append(current_ranges)
    # go through mappings
    # for each aspect, check if the current target numbers match their sources
    # if they do, update the path
    for attribute_map in map_groups:
        for seed_value in path.seeds():
            current_destination = path.seeds()[seed_value]
            applicable_range = list(
                filter(
                    lambda n: current_destination >= n[1]
                    and current_destination <= n[1] + n[2],
                    attribute_map,
                )
            )
            if len(applicable_range) != 0:
                path.update_seed(
                    seed_value,
                    applicable_range[0][0]
                    + (current_destination - applicable_range[0][1]),
                )
    lowest = sorted(path.seeds().values())[0]
    print(f"Lowest location number: {lowest}")


main()

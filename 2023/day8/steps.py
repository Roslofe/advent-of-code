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


def aaa_to_zzz(nodes, traverse_path):
    steps = 0
    i = 0
    location = "AAA"
    # update the current location based on the directions
    while i < len(traverse_path) and not location == "ZZZ":
        if traverse_path[i] == "L":
            direction = 0
        else:
            direction = 1
        location = nodes[location][direction]
        steps += 1
        if i == len(traverse_path) - 1:
            i = 0
        else:
            i += 1
    return steps


def steps_to_z(start, nodes, traverse_path):
    steps = 0
    i = 0
    location = start
    # update the current location based on the directions
    while i < len(traverse_path) and not "Z" in location:
        if traverse_path[i] == "L":
            direction = 0
        else:
            direction = 1
        location = nodes[location][direction]
        steps += 1
        if i == len(traverse_path) - 1:
            i = 0
        else:
            i += 1
    return steps


def ghost_steps(nodes, traverse_path):
    location_nodes = list(
        map(lambda n: n[0], filter(lambda node: "A" in node[0], nodes.items()))
    )
    # the paths loop, so we only need to find the steps to reach it the first time
    steps_to_each = list(
        map(lambda l: steps_to_z(l, nodes, traverse_path), location_nodes)
    )
    multipliers = {}
    i = 1
    locations_count = len(location_nodes)
    while len(list(filter(lambda n: n == locations_count, multipliers.values()))) == 0:
        for step in steps_to_each:
            if step * i in multipliers.keys():
                multipliers[step * i] += 1
            else:
                multipliers[step * i] = 1
        i += 1
    step_count = list(filter(lambda n: n[1] == locations_count, multipliers.items()))[
        0
    ][0]
    return step_count


def main():
    lines = parse("day8/data.txt")
    traverse_path = list(lines[0])
    # map the paths
    nodes = {}
    for line in lines[2:]:
        start = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[start] = (left, right)
    singular_path = aaa_to_zzz(nodes, traverse_path)
    print(f"Number of steps from AAA to ZZZ: {singular_path}")
    ghost_path = ghost_steps(nodes, traverse_path)
    print(f"Number of steps when traveling multiple nodes simultaneously: {ghost_path}")


main()

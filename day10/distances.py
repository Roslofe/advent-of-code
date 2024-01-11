from pipe import Pipe

# keep track of which directions can be visited from each type of pipe
VALID_LOCATIONS = {
    "S": ["n", "s", "e", "w"],
    ".": [],
    "|": ["n", "s"],
    "-": ["e", "w"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
}


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


# Get a list of valid neighboring pipes
# to be valid, the coordinates must be within the range, and the pipe can be entered from the current direction
def getNeighbourPipes(current, max_x, max_y, pipes):
    possible_coords = [
        [current.x() + 1, current.y(), "e"],
        [current.x(), current.y() + 1, "s"],
        [current.x() - 1, current.y(), "w"],
        [current.x(), current.y() - 1, "n"],
    ]
    # eliminate the coordinates not in range
    valid_coords = list(
        filter(lambda n: n[0] in range(max_x) and n[1] in range(max_y), possible_coords)
    )
    # convert the coordinates into pipes
    valid_pipes = list(map(lambda n: [pipes[n[1]][n[0]], n[2]], valid_coords))
    # filter out those that have already been visited, or cannot be visited from the current pipe
    valid_pipes = list(
        filter(
            lambda n: n[1] in VALID_LOCATIONS[current.symbol()] and n[0].canMove(n[1]),
            valid_pipes,
        )
    )
    # finally, remove the directions from the elements, and return the array
    return list(map(lambda n: n[0], valid_pipes))


def main():
    lines = parse("day10/data.txt")
    # placeholder for the starting pipe
    s_pipe = []
    pipes = []
    max_y = len(lines)
    max_x = len(lines[0])
    # convert the lines into pipes, and find the start pipe
    for y in range(len(lines)):
        pipes.append([])
        for x in range(len(lines[0])):
            pipe_symbol = lines[y][x]
            pipes[y].append(Pipe(pipe_symbol, x, y))
            if pipe_symbol == "S":
                s_pipe = pipes[y][x]
    distance_from_s = 1
    curr_pipes = getNeighbourPipes(s_pipe, max_x, max_y, pipes)
    # move one step forward from each side, until the paths meet each other
    # there is an assumption that each pipe will only lead into one valid pipe
    while not len(curr_pipes) == 1:
        distance_from_s += 1
        curr_pipes = getNeighbourPipes(
            curr_pipes[0], max_x, max_y, pipes
        ) + getNeighbourPipes(curr_pipes[1], max_x, max_y, pipes)
    print(f"The steps needed to get to the farthest position: {distance_from_s}")


main()

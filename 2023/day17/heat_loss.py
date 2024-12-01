from node import Node

OPPOSITE_DIR = {"u": "d", "d": "u", "l": "r", "r": "l"}


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


def update_neighbours(curr_location, locations, max_x, max_y):
    coordinates = curr_location.location()
    # find the coordinates for each direction
    new_coordinates = {
        "l": [coordinates[0] - 1, coordinates[1]],
        "r": [coordinates[0] + 1, coordinates[1]],
        "u": [coordinates[0], coordinates[1] - 1],
        "d": [coordinates[0], coordinates[1] + 1],
    }
    # filter out the locations that are out of bounds
    new_coordinates = list(
        filter(
            lambda n: -1 < n[1][0] < max_x and -1 < n[1][1] < max_y,
            new_coordinates.items(),
        )
    )
    # go though the locations specified by the coordinates, update their costs if needed
    for coordinate in new_coordinates:
        location = locations[coordinate[1][1]][coordinate[1][0]]
        if location.can_move(coordinate[0], curr_location):
            location.update_distance(coordinate[0], curr_location)


def main():
    lines = parse("day17/data.txt")
    max_y = len(lines)
    max_x = len(lines[0])
    # "queue" for storing and visiting the locations
    locationQueue = []
    # store all the locations, so that their data can be updated
    all_locations = [[0] * max_x for i in range(max_y)]
    # initialize each location, and add them to the queue
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            curr_location = Node(x, y, int(lines[y][x]))
            # if we are at the starting point, change the current cost to 0
            if y == 0 and x == 0:
                curr_location.reset_total()
            locationQueue.append(curr_location)
            all_locations[y][x] = curr_location

    # start visiting the Nodes one by one, and updating the directions as needed
    while not len(locationQueue) == 0:
        # get the node with the smallest cost
        curr_node = min(locationQueue, key=lambda n: n.total_cost())
        locationQueue.remove(curr_node)
        # mark the node as visited
        curr_node.mark_visited()

        # update the costs of the neighbouring valid nodes
        update_neighbours(curr_node, all_locations, max_x, max_y)

        # if we have arrived at the end node, break out of the loop
        # if curr_node.location() == (max_x - 1, max_y - 1):
        #    break
    a = 3


main()

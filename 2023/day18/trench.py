import random


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


def get_next_location(current, direction, step_length):
    match direction:
        # the last point is the actual turning point, rest are part of the edge
        case "U":
            coords = [(current[0], current[1] - i) for i in range(step_length + 1)]
        case "D":
            coords = [(current[0], current[1] + i) for i in range(step_length + 1)]
        case "L":
            coords = [(current[0] - i, current[1]) for i in range(step_length + 1)]
        case _:
            coords = [(current[0] + i, current[1]) for i in range(step_length + 1)]
    return coords


def main():
    lines = parse("day18/data.txt")
    # follow the instructions in the data, determine the edge points of the trench
    # starting coordinate is (0, 0) (x, y)
    edges = []
    all_points = []
    current_coord = (0, 0)
    for dig in lines:
        direction = dig.split(" ")[0]
        length = int(dig.split(" ")[1])
        next_coords = get_next_location(current_coord, direction, length)
        all_points.extend(next_coords)
        edges.append(next_coords[-1])
        current_coord = next_coords[-1]
    # sort the data points according to the row in order to get the number of rows
    y_sorted = sorted(edges, key=lambda n: n[1])
    min_y = y_sorted[0][1]
    max_y = y_sorted[-1][1]
    # find out the width of a row
    x_sorted = sorted(edges, key=lambda n: n[0])
    min_x = x_sorted[0][0]
    max_x = x_sorted[-1][0]
    # find a random point that is inside the shape to start filling it
    fill_cord = (random.randint(min_x, max_x), random.randint(min_y, max_y))
    # using the crossing number algorithm, find a starting point that is inside the shape
    while fill_cord in all_points or (
        len(list(filter(lambda n: n[1] == fill_cord[1] and n[0] > fill_cord[0], edges)))
        % 2
        == 0
        and len(
            list(filter(lambda n: n[1] == fill_cord[1] and n[0] < fill_cord[0], edges))
        )
        % 2
        == 0
    ):
        fill_cord = (random.randint(min_x, max_x), random.randint(min_y, max_y))
    a = 3
    # lava_amount = 0
    # go through each row
    # for y in range(min_y, max_y):
    # get the edge points in that row

    # go through each row
    # for y in range(min_y, max_y):
    #    # get the edge points in that row. There should be an even amount
    #    row_eges = sorted(list(filter(lambda n: n[1] == y, edges)), key=lambda m: m[0])
    #    # form the edge points into pairs. There is trench space between them
    #    for i in range(0, len(row_eges), 2):
    #        lava = abs(row_eges[i + 1][0] - row_eges[i][0]) + 1
    #        lava_amount += lava
    #    # if there are no edges/one edge, the entire row is lava
    #    if not row_eges:
    #        lava_amount += row_len
    # a = 3


main()

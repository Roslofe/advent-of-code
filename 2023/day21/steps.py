from location import Location

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
    lines = parse("day21/data.txt")
    max_y = len(lines)
    max_x = len(lines[0])
    # keep track of the current plot
    curr_plots = []
    # garden plots, (symbol, currently on)
    garden = [[0]*max_x for i in range(max_y)]
    # Create the location objects
    for y in range(max_y):
        for x in range(max_x):
            curr_symbol = lines[y][x]
            if curr_symbol == "S":
                new_location = Location(x, y, '.')
                new_location.set_visitation(True)
                curr_plots.append(new_location)
            else:
                new_location = Location(x, y, curr_symbol)
            garden[y][x] = new_location
    steps = 64
    # start moving one step at a time
    for i in range(steps):
        # get the next steps to move in
        possible_locations = [l.places_to_move(garden, max_x, max_y) for l in curr_plots]
        # update the possible locations to those that aren't rocks
        curr_plots = list(set(filter(lambda n: not n.symbol() == "#", [p for l in possible_locations for p in l])))
    print(len(curr_plots))

main()
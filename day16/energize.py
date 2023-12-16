SPLITTER_DIRECTIONS = {
    "l": ["u", "d"],
    "r": ["u", "d"],
    "u": ["l", "r"],
    "d": ["l", "r"],
}
MIRROR_DIRECTIONS = {
    ("r", "/"): "u",
    ("l", "\\"): "u",
    ("r", "\\"): "d",
    ("l", "/"): "d",
    ("u", "\\"): "l",
    ("d", "/"): "l",
    ("u", "/"): "r",
    ("d", "\\"): "r",
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


def update_coordinate(beam):
    match beam[2]:
        case "r":
            return [beam[0] + 1, beam[1], beam[2]]
        case "l":
            return [beam[0] - 1, beam[1], beam[2]]
        case "u":
            return [beam[0], beam[1] - 1, beam[2]]
        case "d":
            return [beam[0], beam[1] + 1, beam[2]]


def move_beam(beam, location_type, max_x, max_y):
    direction = beam[2]
    # if current location is empty space or a splitter in the same direction on the x-y -axis as the beam, move to the same direction
    if (
        location_type == "."
        or (location_type == "|" and direction in ["u", "d"])
        or (location_type == "-" and direction in ["l", "r"])
    ):
        new_locations = [update_coordinate(beam)]
    # otherwise, if the location is a splitter, you get two new beams
    elif location_type in ["|", "-"]:
        new_locations = list(
            map(
                lambda n: update_coordinate([beam[0], beam[1], n]),
                SPLITTER_DIRECTIONS[direction],
            )
        )
    # if a mirror is encountered, the beam turns 90 degrees
    else:
        new_locations = [
            update_coordinate(
                [
                    beam[0],
                    beam[1],
                    MIRROR_DIRECTIONS[(direction, location_type)],
                ]
            )
        ]
    # return valid locations, i.e. the ones inside the bounds of the map
    return list(
        filter(lambda n: -1 < n[0] < max_x and -1 < n[1] < max_y, new_locations)
    )


def main():
    lines = parse("day16/data.txt")
    # keep track of each tiles symbol, if it has been energized, and which directions have been visited already from it
    locations = list(map(lambda n: [[a, False, []] for a in list(n)], lines))

    # bounds of the map
    max_x = len(locations[0])
    max_y = len(locations)

    # keep track of the beams and their coordinates
    # x, y, direction (l, r, u, d)
    beams = [(0, 0, "r")]

    # start moving the beams, treat the array as a queue
    while beams:
        curr_beam = beams.pop(0)
        beam_location = locations[curr_beam[1]][curr_beam[0]]
        # mark location as energized
        beam_location[1] = True
        # if a beam going to the same direction hasn't visited, update the locations
        if curr_beam[2] not in beam_location[2]:
            # get the new location(s) of the beam
            new_location = move_beam(curr_beam, beam_location[0], max_x, max_y)
            beams.extend(new_location)
            beam_location[2].append(curr_beam[2])
    # get the number of energized tiles
    energized_count = len(
        list(
            filter(lambda n: n, [location[2] for row in locations for location in row])
        )
    )
    print(f"Energized tiles: {energized_count}")


main()

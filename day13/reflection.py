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


# get the number of lines above/to the left of the reflection point
def reflection_line(pattern):
    # check if there is a reflection
    for i in range(len(pattern) - 1, 0, -1):
        reflected_lines = pattern[i:]
        reflecting = pattern[:i]
        reflecting.reverse()
        pairs = zip(reflected_lines, reflecting)
        if all(n[0] == n[1] for n in pairs):
            return i
    return 0


def main():
    lines = parse("day13/data.txt")
    patterns = []
    curr_pattern = []
    for line in lines:
        if line != "":
            curr_pattern.append(line)
        else:
            patterns.append(curr_pattern)
            curr_pattern = []
    patterns.append(curr_pattern)
    reflections = 0
    for pattern in patterns:
        # try the rows first
        row_reflection = reflection_line(pattern)
        if row_reflection == 0:
            # convert the columns into arrays
            columns = []
            for i in range(0, len(pattern[0])):
                columns.append("".join(map(lambda n: n[i], pattern)))
            reflections += reflection_line(columns)
        else:
            reflections += 100 * row_reflection
    print(f"From summarizing the reflections, the sum is: {reflections}")


main()

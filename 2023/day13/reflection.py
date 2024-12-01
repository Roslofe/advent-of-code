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
        # first, without modifications
        reflection_no_mods = 0
        # try the rows first
        row_reflection = reflection_line(pattern)
        if row_reflection == 0:
            # convert the columns into arrays
            columns = []
            for i in range(0, len(pattern[0])):
                columns.append("".join(map(lambda n: n[i], pattern)))
            reflection_no_mods = reflection_line(columns)
        else:
            reflection_no_mods = 100 * row_reflection
    print(f"From summarizing the reflections, the sum is: {reflections}")
    smudge_reflection = 0
    for pattern in patterns:
        # try the rows first
        reflection_value = 0
        i = 0
        j = 0
        while reflection_value == 0:
            row_reflection = pattern.copy()
            if row_reflection[i][j] == "#":
                row_reflection[i] = (
                    row_reflection[i][:j] + "." + row_reflection[i][j + 1 :]
                )
            else:
                row_reflection[i] = (
                    row_reflection[i][:j] + "#" + row_reflection[i][j + 1 :]
                )
            reflection_value = 100 * reflection_line(row_reflection)
            if reflection_value == 0:
                # convert the columns into arrays
                columns = []
                for i in range(0, len(pattern[0])):
                    columns.append("".join(map(lambda n: n[i], row_reflection)))
                reflection_value += reflection_line(columns)
            if j == len(pattern[0]):
                i += 1
                j = 0
            else:
                j += 1
        smudge_reflection += reflection_value
    a = 3


main()

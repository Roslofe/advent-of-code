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
    lines = parse("day14/data.txt")
    # convert the line data into columns:
    columns = []
    for i in range(0, len(lines[0])):
        column = list(map(lambda n: n[i], lines))
        columns.append(column)
        for j in range(0, len(column)):
            if column[j] == ".":
                n


main()

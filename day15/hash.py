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
    codes = parse("day15/data.txt")[0].split(",")
    hashes_sum = 0
    # compute the hash value for each code
    for code in codes:
        curr_value = 0
        for char in code:
            curr_value += ord(char)
            curr_value *= 17
            curr_value = curr_value % 256
        hashes_sum += curr_value
    print(f"Sum of the hash values: {hashes_sum}")


main()

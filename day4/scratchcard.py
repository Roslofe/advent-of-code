from functools import reduce


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
    lines = parse("day4/data.txt")
    point_total = 0
    # go through each line, find the winning numbers present in the card, and calculate the point total
    for line in lines:
        split_line = line.split(" | ")
        winning = split_line[0].split()[2:]
        card_numbers = split_line[1].split()
        found_winning = list(filter(lambda n: n in card_numbers, winning))
        point_total += reduce(lambda x, y: max(x * 2, 1), found_winning, 0)
    print(f"Value of the scratchcards: {point_total}")


main()

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


# find all the winning numbers in a card
def find_matches(line):
    split_line = line.split(" | ")
    winning = split_line[0].split()[2:]
    card_numbers = split_line[1].split()
    found_winning = list(filter(lambda n: n in card_numbers, winning))

    return found_winning


def card_values(lines):
    point_total = 0
    # go through each line, find the winning numbers present in the card, and calculate the point total
    for line in lines:
        found_winning = find_matches(line)
        point_total += reduce(lambda x, y: max(x * 2, 1), found_winning, 0)
    return point_total


def card_copies(lines):
    # keep track of the number of copies of each card
    copies = [1] * len(lines)
    for line in lines:
        card_id = int(line.split(":")[0].split()[1])
        card_count = copies[card_id - 1]
        win_count = len(find_matches(line))
        for i in range(0, card_count):
            for j in range(card_id, card_id + win_count):
                copies[j] += 1
    return reduce(lambda x, y: x + y, copies)


def main():
    lines = parse("day4/data.txt")
    point_total = card_values(lines)
    copy_count = card_copies(lines)
    print(f"Value of the scratchcards: {point_total}")
    print(f"Total number of card copies: {copy_count}")


main()

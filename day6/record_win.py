from race import Race


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


# compute the ways of winning for each race, and multiply them together
def main():
    lines = parse("day6/data.txt")
    race_info = zip(lines[0].split()[1:], lines[1].split()[1:])
    win_ways = 1
    for info in race_info:
        race = Race(info[0], info[1])
        win_ways *= race.winning_alts()
    print(f"Number of ways to win the races: {win_ways}")


main()

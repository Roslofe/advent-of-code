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


# calculate the number of ways to win the races
def multiple_races(lines):
    race_info = zip(lines[0].split()[1:], lines[1].split()[1:])
    win_ways = 1
    for info in race_info:
        race = Race(info[0], info[1])
        win_ways *= race.winning_alts()
    return win_ways


# calculate the ways of winning the race, when there is only one race altogether
def single_race(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    duration = int(lines[1].split(":")[1].replace(" ", ""))
    race = Race(time, duration)
    win_ways = race.winning_alts()
    return win_ways


# compute the ways of winning for each race, and multiply them together
def main():
    lines = parse("day6/data.txt")
    mult_win_ways = multiple_races(lines)
    single_win_ways = single_race(lines)
    print(f"Number of ways to win the races: {mult_win_ways}")
    print(f"When there is only one race, the number of ways to win: {single_win_ways}")


main()

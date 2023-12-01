def parse(filename):
    lines = []
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            lines = map(lambda n: n.rstrip(), contents)
            file.close()
    except OSError:
        print("Error in reading the file.")

    return lines


def main():
    lines = parse("day1/data.txt")
    sum = 0
    for line in lines:
        nums = list(filter(lambda n: n.isdigit(), line))
        sum += int(nums[0] + nums[-1])
    print(f"Calibration sum: {sum}")


main()

TEXT_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEXT_TO_CHAR = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
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

    return lines


# solution to the first part. Filter out everything but the numbers,
# and add the concatenation of the first and last numbers into the sum.
def digitsOnly(lines):
    sum = 0
    for line in lines:
        nums = list(filter(lambda n: n.isdigit(), line))
        if len(nums) > 0:
            sum += int(nums[0] + nums[-1])

    return sum


def withText(lines):
    sum = 0
    for line in lines:
        last_i = len(line) - 1
        first = ""
        last = ""
        i = 0
        while i < len(line) and (first == "" or last == ""):
            # if there is a text digit, find which one, update it to the first position
            if any(num in line[:i] for num in TEXT_DIGITS) and first == "":
                first = TEXT_TO_CHAR[
                    list(filter(lambda n: n in line[:i], TEXT_DIGITS))[0]
                ]
            # if the current character is a digit, update it to the first position
            elif line[i].isnumeric() and first == "":
                first = line[i]

            # same operation, but for the last digit
            if line[last_i - i].isnumeric() and last == "":
                last = line[last_i - i]
            if any(num in line[last_i - i :] for num in TEXT_DIGITS) and last == "":
                last = TEXT_TO_CHAR[
                    list(filter(lambda n: n in line[last_i - i :], TEXT_DIGITS))[0]
                ]
            i += 1
        sum += int(first + last)
    return sum


def main():
    lines = list(parse("day1/data.txt"))
    digit_sum = digitsOnly(lines)
    text_sum = withText(lines)
    print(f"Calibration sum: {digit_sum}")
    print(f"Calibration sum with letters: {text_sum}")


main()

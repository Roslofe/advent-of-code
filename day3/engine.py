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


# determine if there are any symbols adjacent to the current number
def is_adjacent(num_s, num_e, num_r, grid):
    row_start = max(0, num_r - 1)
    row_end = min(139, num_r + 1)
    column_start = max(0, num_s - 1)
    column_end = min(139, num_e + 1)
    valid_rows = list(
        map(lambda n: n[column_start : column_end + 1], grid[row_start : row_end + 1])
    )
    if any((not x.isnumeric()) and x != "." for row in valid_rows for x in row):
        return True
    else:
        return False


def main():
    lines = parse("day3/data.txt")
    grid = [list(w) for w in lines]
    sum = 0

    for y in range(0, len(grid)):
        curr_num = ""
        num_s = float("inf")
        for x in range(0, len(grid[0])):
            char = grid[y][x]
            if char.isnumeric():
                curr_num += char
                num_s = min(x, num_s)
                if x == 139 or not grid[y][x + 1].isnumeric():
                    if is_adjacent(num_s, x, y, grid):
                        sum += int(curr_num)
                    curr_num = ""
                    num_s = float("inf")

    print(f"Sum of valid engine numbers: {sum}")


main()

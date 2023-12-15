import re


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


# compute the hash value for each code
def hash(code):
    curr_value = 0
    for char in code:
        curr_value += ord(char)
        curr_value *= 17
        curr_value = curr_value % 256
    return curr_value


# calculate the sum of the hashes for the csv:s
def instruction_hashes(codes):
    hashes_sum = 0
    for code in codes:
        hash_val = hash(code)
        hashes_sum += hash_val
    return hashes_sum


# determine the focal power of the box configuration
def focal_power(boxes):
    lens_config_sum = 0
    # go through each box, calculate the focusing power for each
    for i in range(0, 256):
        focus_pwr = 0
        box = boxes[i]
        items = list(box.values())
        for j in range(0, len(items)):
            focus_pwr += (i + 1) * (j + 1) * items[j]
        lens_config_sum += focus_pwr
    return lens_config_sum


# populates the boxes according to the data
def arrange_boxes(codes):
    # initialize box array
    boxes = [dict() for i in range(0, 256)]
    # fill the boxes according to the instructions
    for code in codes:
        label = re.split("=|-", code)[0]
        focal_len = re.split("=|-", code)[1]
        box = boxes[hash(label)]
        # if the operation is a dash, remove the label from the box
        if code[-1] == "-" and label in box:
            del box[label]
        elif not code[-1] == "-":
            box[label] = int(focal_len)
    return focal_power(boxes)


def main():
    codes = parse("day15/data.txt")[0].split(",")
    instructions_sum = instruction_hashes(codes)
    config_power = arrange_boxes(codes)
    print(f"Sum of the hash values: {instructions_sum}")
    print(f"Total focusing power: {config_power}")


main()

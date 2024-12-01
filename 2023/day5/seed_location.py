from path import Path


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


def attribute_mappings(lines):
    # gather the mappings in each attribute
    map_groups = []
    # destination, source, range
    current_ranges = []
    for line in lines[2:]:
        if line == "":
            map_groups.append(current_ranges)
            current_ranges = []
        elif line.split()[0].isnumeric():
            split_line = tuple(map(lambda n: int(n), line.split()))
            current_ranges.append(split_line)
    map_groups.append(current_ranges)
    return map_groups


def lowest_location(seeds, lines):
    init_mapping = {}
    for seed in seeds:
        init_mapping[seed] = seed
    path = Path(init_mapping)
    # get the mappings of the attributes
    map_groups = attribute_mappings(lines)
    # go through mappings
    # for each aspect, check if the current target numbers match their sources
    # if they do, update the path
    for attribute_map in map_groups:
        # print("starting group")
        for seed_value in path.seeds():
            current_destination = path.seeds()[seed_value]
            applicable_range = list(
                filter(
                    lambda n: current_destination >= n[1]
                    and current_destination <= n[1] + n[2],
                    attribute_map,
                )
            )
            if len(applicable_range) != 0:
                path.update_seed(
                    seed_value,
                    applicable_range[0][0]
                    + (current_destination - applicable_range[0][1]),
                )
    lowest = sorted(path.seeds().values())[0]
    return lowest


# Given a list of mappings, returns a dict of new ranges based on said mapping
def update_mapping(current_range, original_range, mappings):
    not_updated = {current_range: original_range}
    updated = {}
    # go through each mapping
    for mapping in mappings:
        mapping_orig_end = mapping[1] + mapping[2] - 1
        # go through each un-updated mapping
        for old_range in not_updated.copy():
            orig_values = not_updated[old_range]
            # there are 4 possible cases (when updating is needed):
            # 1. The mapping goes over the range in both directions => update entire range
            if mapping[1] <= old_range[0] and mapping_orig_end >= old_range[1]:
                new_start = mapping[0] + abs(old_range[0] - mapping[1])
                new_end = new_start + (old_range[1] - old_range[0])
                # add the new range to the list of updated values and remove them from the not updated list
                updated[(new_start, new_end)] = orig_values
                not_updated.pop(old_range)
            # 2. The mapping start is within the range, but the end is not
            elif mapping[1] > old_range[0] and mapping_orig_end > old_range[1]:
                # get the number of elements that are not within the range
                extra_numbers = abs(mapping[1] - old_range[0])
                # extract the un-updated range
                extra_start = (old_range[0], old_range[0] + extra_numbers - 1)
                extra_end = [orig_values[0], orig_values[0] + extra_numbers - 1]
                not_updated.pop(old_range)
                not_updated[extra_start] = extra_end
                # calculate the new start and end
                new_start = mapping[0]
                new_end = new_start + (old_range[1] - old_range[0] - extra_numbers)
                updated[(new_start, new_end)] = [
                    orig_values[0] + extra_numbers,
                    orig_values[1],
                ]
            # 3. The mapping end is within the range, but the start is not
            elif mapping[1] < old_range[0] and mapping_orig_end < old_range[1]:
                # get the extra numbers from the end, that are not within the range
                extra_numbers = abs(mapping_orig_end - old_range[1])
                not_updated.pop(old_range)
                not_updated[(mapping_orig_end + 1, current_range[1])] = [
                    orig_values[1] - extra_numbers + 1,
                    orig_values[1],
                ]
                new_start = mapping[0] + abs(old_range[0] - mapping[1])
                updated[(new_start, mapping[0] + mapping[2] - 1)] = [
                    orig_values[0],
                    orig_values[1] - extra_numbers,
                ]
            # 4. Both the start and end are within the range
            elif (
                old_range[1] > mapping[1] > old_range[0]
                and old_range[0] < mapping_orig_end < old_range[1]
            ):
                not_updated.pop(old_range)
                # first, remove the extra from the start
                extra_numbers_start = abs(mapping[1] - old_range[0])
                # extract the un-updated range
                extra_start = (old_range[0], old_range[0] + extra_numbers_start - 1)
                extra_end = [orig_values[0], orig_values[0] + extra_numbers_start - 1]
                not_updated[extra_start] = extra_end
                # then remove the extra from the end
                extra_numbers_end = abs(mapping_orig_end - old_range[1])
                not_updated[(mapping_orig_end + 1, current_range[1])] = [
                    orig_values[1] - extra_numbers_end + 1,
                    orig_values[1],
                ]
                # update the applicable area
                # calculate the new start and end
                new_start = mapping[0]
                new_end = mapping[0] + mapping[2] - 1
                updated[(new_start, new_end)] = [
                    orig_values[0] + extra_numbers_start,
                    orig_values[1] - extra_numbers_end,
                ]
            # it is also possible that the mapping does not apply to the current range
            # in that case, do nothing
    # return the combination of the new and old mappings
    # the mappings that were not updated will stay the same
    return updated | not_updated


def main():
    lines = parse("day5/data.txt")
    seeds_all = list(map(lambda n: int(n), lines[0].split()[1:]))
    lowest_all = lowest_location(seeds_all, lines)
    print(f"Lowest location number: {lowest_all}")

    # start, end
    seed_ranges = {}
    while seeds_all:
        range_start = seeds_all.pop(0)
        seed_values = [range_start, range_start + seeds_all.pop(0) - 1]
        seed_ranges[(seed_values[0], seed_values[1])] = seed_values
    # destination, source, range
    location_maps = attribute_mappings(lines)
    # start going through the mappings
    for mapping in location_maps:
        updated_ranges = {}
        # for each seed range, check if the mapping applies to some of its values
        for seed_range in seed_ranges:
            # a mapping is applicable, if its start or end is within the range, or if the start is smaller and end larger than the range
            applicable_ranges = list(
                filter(
                    lambda n: seed_range[0] <= n[1] <= seed_range[1]
                    or seed_range[0] <= n[1] + n[2] - 1 <= seed_range[1]
                    or (n[1] <= seed_range[0] and n[1] + n[2] - 1 >= seed_range[1]),
                    mapping,
                )
            )
            new_mappings = update_mapping(
                seed_range, seed_ranges[seed_range], applicable_ranges
            )
            updated_ranges = updated_ranges | new_mappings
        seed_ranges = updated_ranges
    # the lowest location number is the smallest start number in the seed_ranges keys
    lowest = sorted(list(map(lambda n: n[0], seed_ranges.keys())))
    print(f"Lowest when seeds are given in ranges: {lowest}")
    # not 0


main()

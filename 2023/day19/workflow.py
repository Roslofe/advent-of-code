import re
from functools import reduce

CAT_INDICES = {"x": 0, "m": 1, "a": 2, "s": 3}

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


def process_parts(workflows, lines):
    # store the parts and the workflow they're in (excluding accepted parts)
    # x, m, a, s, workflow
    parts = []
    accepted_parts = []
    for line in lines[lines.index("") + 1 :]:
        split_part = list(
            map(lambda n: int(n.split("=")[1]), re.split("{|,|}", line)[1:-1])
        )
        parts.append(split_part + ["in"])

    # process the parts
    while parts:
        curr_part = parts.pop(0)
        workflow_reqs = workflows[curr_part[4]]
        next_flow = ""
        # go through the comparators
        for i in range(len(workflow_reqs)):
            current_req = workflow_reqs[i]
            if ":" not in current_req:
                next_flow = current_req
                break
            # get the value we are comparing, and the value we are comparing against
            comparison_categories = re.split("<|>|:", current_req)
            comparing = curr_part[CAT_INDICES[comparison_categories[0]]]
            comparing_against = int(comparison_categories[1])
            if ">" in current_req and comparing > comparing_against:
                next_flow = comparison_categories[2]
                break
            elif "<" in current_req and comparing < comparing_against:
                next_flow = comparison_categories[2]
                break
        if next_flow == "A":
            accepted_parts.append(curr_part)
        elif not next_flow == "R":
            curr_part[4] = next_flow
            parts.append(curr_part)
    return reduce(
        lambda a, b: a + b, [i for part in accepted_parts for i in part[:-1]], 0
    )


def determine_limits(workflows, curr_conds):
  curr_cond = curr_conds[0]
  # if we are at an accept, return back. No conditions
  


def main():
    lines = parse("day19/data.txt")
    # create and store the workflows
    workflows = {}
    for line in lines:
        if line == "":
            break

        split_elements = re.split("{|,|}", line)
        workflows[split_elements[0]] = split_elements[1:-1]
    accepted_sum = process_parts(workflows, lines)
    print(f"Sum of accepted parts: {accepted_sum}")


main()

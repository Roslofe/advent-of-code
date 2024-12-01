from module import Module
from queue import Queue


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
    lines = parse("day20/data.txt")
    modules = []
    # keep track of the broadcasting module
    broadcaster = []

    # used in parsing: the list of destinations for each module
    destinations = []

    # parse the lines into modules
    for line in lines:
        information = line.split(" -> ")
        if information[0][0] in ["%", "&"]:
            name = information[0][1:]
            type_symbol = information[0][0]
        else:
            name = information[0]
            type_symbol = ""
        new_module = Module(name, type_symbol)
        if name == "broadcaster":
            broadcaster = new_module
        modules.append(new_module)
        destinations.append((new_module, information[1].split(", ")))

    # add destinations to all the modules. If a module is a conjunction module, it's sources are stored as well.
    for module in modules:
        # find the destination modules, and update them to the module itself
        dest_names = list(filter(lambda n: n[0] == module, destinations))[0][1]
        dest_modules = list(filter(lambda m: m.name() in dest_names, modules))
        module.add_destinations(dest_modules)

        # if it's a conjunction module, find all its sources
        if module.type_symbol() == "&":
            sources = list(filter(lambda n: module.name() in n[1], destinations))
            module.init_sources(list(map(lambda m: m[0], sources)))

    # pulses can now be sent. A high pulse is represented by a 1, and a low pulse by 0
    # a queue for storing the not yet processed pulses. Stores the module where the pulse will be sent, its strength, and the sender
    pulses = Queue()

    # store the number of highs and lows in each iteration
    pulse_counts = []

    # TODO Currently takes too long. Instead, find how long a cycle is (check if all the modules are in their original states), and calculate the total from there
    # the button pressing process is done 1000 times

    # for i in range(1000):
    # send the initial low pulse to the broadcaster
    pulses.put((broadcaster, 0, ""))

    # store the number of high and low pulses
    hi = 0
    lo = 0

    # process pulses as long as there are some
    while not pulses.empty():
        curr_pulse = pulses.get()
        # update the number of pulses
        if curr_pulse[1] == 0:
            lo += 1
        else:
            hi += 1

        # process the pulse, and recieve the array of the pulses to be sent forward
        next_pulses = curr_pulse[0].process_pulse(curr_pulse[1], curr_pulse[2])

        # add the pulses to be processed
        for pulse in next_pulses:
            pulses.put(pulse)
        """
        if not pulse_counts or False in list(map(lambda n: n.is_default(), modules)):
            pulse_counts.append([hi, lo])
        else:
            break"""

    print(f"Total number of high and low pulses multiplied: {hi *lo}")


main()

class Module:
    def __init__(self, name, type_symbol):
        self.__name = name
        self.__type_symbol = type_symbol
        self.__destinations = []
        self.__dest_count = 0
        if type_symbol == "%":
            # for flip-flop modules, 0 is off and 1 is on
            self.__status = 0
        elif type_symbol == "&":
            # for conjunction modules, the memory is stored. 0 is low, 1 is high
            self.__sources = {}

    def name(self):
        return self.__name

    def type_symbol(self):
        return self.__type_symbol

    def init_sources(self, source_list):
        for source in source_list:
            self.__sources[source] = 0

    def add_destinations(self, dest_list):
        self.__destinations = dest_list
        self.__dest_count = len(dest_list)

    def update_status(self):
        if self.__status == 0:
            self.__status = 1
        else:
            self.__status = 0

    def process_pulse(self, pulse_type, sender):
        # processing is dependent on the module type
        if self.__type_symbol == "%":
            # for flip-flops, high modules do nothing, and low modules switch their type and send a pulse
            if pulse_type == 1:
                return []
            else:
                self.update_status()
                return list(
                    zip(
                        self.__destinations,
                        [self.__status] * self.__dest_count,
                        [self] * self.__dest_count,
                    )
                )
        elif self.__type_symbol == "&":
            # conjunctions update their memory, and send a low pulse only if its memory consists of all high pulses
            self.__sources[sender] = pulse_type
            if 0 in self.__sources.values():
                export_pulse = 1
            else:
                export_pulse = 0
            return list(
                zip(
                    self.__destinations,
                    [export_pulse, self] * self.__dest_count,
                    [self] * self.__dest_count,
                )
            )
        else:
            # in this case this is the broadcast module, and the same pulse is sent to its destinations
            return list(
                zip(
                    self.__destinations,
                    [pulse_type] * self.__dest_count,
                    [self] * self.__dest_count,
                )
            )

    # determines if the module is in its default condition
    def is_default(self):
        match self.__type_symbol:
            case "":
                return True
            case "%":
                self.__status == 0
            case "&":
                1 not in self.__sources.values()

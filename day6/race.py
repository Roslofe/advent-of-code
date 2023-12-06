from math import ceil


class Race:
    def __init__(self, t, d):
        self.__time = int(t)
        self.__distance = int(d)

    def winning_alts(self):
        win_ways = 0
        for speed in range(1, self.__time):
            # if the distance moved during the remaining duration is enough to break the record, increase the ways of winning
            if speed * (self.__time - speed) > self.__distance:
                win_ways += 1
        return win_ways

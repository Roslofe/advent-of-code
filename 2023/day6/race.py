class Race:
    def __init__(self, t, d):
        self.__time = int(t)
        self.__distance = int(d)

    def winning_alts(self):
        win_ways = 0
        smallest_speed = 0
        while smallest_speed * (self.__time - smallest_speed) <= self.__distance:
            smallest_speed += 1
        largest_speed = self.__time - 1
        while largest_speed * (self.__time - largest_speed) <= self.__distance:
            largest_speed -= 1
        # for speed in range(1, self.__time):
        #    # if the distance moved during the remaining duration is enough to break the record, increase the ways of winning
        #    if speed * (self.__time - speed) > self.__distance:
        #        win_ways += 1
        return largest_speed - smallest_speed + 1

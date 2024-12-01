class Symbol:
    def __init__(self, r, i, s):
        self.__row = int(r)
        self.__index = int(i)
        self.__symbol = str(s)

    def row(self):
        return self.__row

    def index(self):
        return self.__index

    def symbol(self):
        return self.__symbol


class EngineValue:
    def __init__(self, r, s, e, value):
        self.__value = int(value)
        self.__row = int(r)
        self.__start = int(s)
        self.__end = int(e)

    def row(self):
        return self.__row

    def start(self):
        return self.__start

    def end(self):
        return self.__end

    def value(self):
        return self.__value

    def isAdjacent(self, symbol):
        if symbol.row() in range(
            self.row() - 1, self.row() + 2
        ) and symbol.index() in range(self.start() - 1, self.end() + 2):
            return True
        else:
            return False

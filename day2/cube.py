class Cube:
    def __init__(self, amount, color):
        self.__amount = int(amount)
        self.__color = str(color[0])

    # check if the amount is over the limit for the first half
    def too_many(self):
        match self.__color:
            case "r":
                return self.__amount > 12
            case "g":
                return self.__amount > 13
            case "b":
                return self.__amount > 14
            case _:
                return False

    def amount(self):
        return self.__amount

    def color(self):
        return self.__color

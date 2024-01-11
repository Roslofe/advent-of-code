# keep track of which directions can be visited from each type of pipe
VALID_LOCATIONS = {
    "S": ["n", "s", "e", "w"],
    ".": [],
    "|": ["n", "s"],
    "-": ["e", "w"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
}


class Pipe:
    def __init__(self, symbol, x, y):
        self.__symbol = symbol
        self.__x = x
        self.__y = y
        if symbol == "S":
            self.__visited = True
        else:
            self.__visited = False

    def symbol(self):
        return self.__symbol

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    # determine if the pipe can be moved into from the provided direction
    # if the move is allowed, mark the pipe as visited
    def canMove(self, direction):
        if self.symbol == "." or self.__visited:
            return False
        match direction:
            case "n":
                valid_pipes = ["|", "7", "F"]
            case "s":
                valid_pipes = ["|", "L", "J"]
            case "e":
                valid_pipes = ["-", "J", "7"]
            case "w":
                valid_pipes = ["-", "L", "F"]
        if self.__symbol in valid_pipes:
            self.__visited = True
            return True
        return False

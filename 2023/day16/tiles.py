class Tile:
    def __init__(self):
        self.__energized = False

    def energized(self):
        return self.__energized
    

class EmptyTile(Tile):
    def __init__(self):
        super.__init__(self)

    def pass_through(self, beam_dir):
        self.__energized = True
        return beam_dir

class Splitter(Tile):
    def __init__(self, dir):
        super.__init__(self)
        self.__direction = dir

    def direction(self):
        return self.__direction
    
    def pass_through(self, beam_dir):
        if beam_dir

class Mirror(Tile):
    def __init__(self, dir):
        super.__init__(self)
        self.__direction = dir

    def direction(self):
        return self.__direction
    

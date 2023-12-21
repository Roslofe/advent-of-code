class Location:

  def __init__(self, x, y, symbol):
    self.__x = x 
    self.__y = y 
    self.__symbol = symbol
    self.__visiting = False

  def coordinates(self): return (self.__x, self.__y)

  def symbol(self): return self.__symbol

  def visiting(self): return self.__visiting

  def set_visitation(self, status):
    self.__visiting = status

  def places_to_move(self, garden, max_x, max_y):
    coordinates = [(self.__x, self.__y + 1), (self.__x, self.__y - 1), (self.__x + 1, self.__y), (self.__x - 1, self.__y)]
    possible_locations = list(filter(lambda n: -1 < n[0] < max_x and -1 < n[1] < max_y, coordinates))
    return list(map(lambda l: garden[l[1]][l[0]], possible_locations))

class Node:
    def __init__(self, x, y, cost):
        self.__x = x
        self.__y = y
        self.__cost = cost
        self.__visited = False
        self.__total_cost = float("inf")
        # keep track of not going into the same direction three times
        self.__direction_moved = ["", 0]

    def location(self):
        return (self.__x, self.__y)

    def cost(self):
        return self.__cost

    def visited(self):
        return self.__visited

    def mark_visited(self):
        self.__visited = True

    def total_cost(self):
        return self.__total_cost

    # helper for the first location
    def reset_total(self):
        self.__total_cost = 0

    # update the cost and direction moved
    def update_distance(self, direction, source):
        if self.total_cost() < self.__cost + source.total_cost():
            return
        self.__total_cost = self.cost() + source.total_cost()
        if direction == source.direction_moved()[0]:
            self.__direction_moved = [direction, source.direction_moved()[1] + 1]
        else:
            self.__direction_moved = [direction, 1]

    def direction_moved(self):
        return self.__direction_moved

    # determine if the node can be entered from the given direction (and the node has not already been visited)
    def can_move(self, direction, source):
        if (self.visited() and direction == self.direction_moved()[0]) or (
            source.direction_moved()[0] == direction
            and source.direction_moved()[1] == 3
        ):
            return False
        else:
            return True

    # comparators for the queue
    def __lt__(self, other):
        return self.__total_cost < other.total_cost()

    def __gt__(self, other):
        return self.__total_cost > other.total_cost()

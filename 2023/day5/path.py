class Path:
    def __init__(self, seeds):
        self.__seeds = dict(seeds)

    def seeds(self):
        return self.__seeds

    def update_seed(self, seed, destination):
        self.__seeds[seed] = destination

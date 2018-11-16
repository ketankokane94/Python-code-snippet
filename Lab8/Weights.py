class Weight:
    __slots__ = 'weight','distance_from_center','unknown_weight'

    def __init__(self, weight, distance_from_center):
        if type(weight).__name__ == 'int' and int(weight) == -1 :
            self.weight = 0
            self.unknown_weight = True
        else:
            self.weight = weight
            self.unknown_weight = False
        self.distance_from_center = int(distance_from_center)
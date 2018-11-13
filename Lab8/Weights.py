class Weight:
    __slots__ = 'weight','distance_from_center'

    def __init__(self,weight,distance_from_center):
        self.weight = weight
        self.distance_from_center = int(distance_from_center)
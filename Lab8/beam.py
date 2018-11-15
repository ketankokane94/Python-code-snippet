
class Beam:
    __slots__ = 'balanced','unknown_weight','total_weight','name','weights'

    def __init__(self, name):
        self.name = name
        self.balanced  = False
        self.unknown_weight = False
        self.total_weight = 0
        self.weights = []

    def add_weight(self,w):
        if type(w.weight).__name__ != 'int':
            self.weights.append(w)
            self.total_weight +=w.weight.total_weight
            self.unknown_weight = self.unknown_weight  or w.unknown_weight
        else:
            self.weights.append(w)
            self.total_weight += w.weight
            self.unknown_weight = self.unknown_weight  or w.unknown_weight

    def calculate_torque(self):
        torque = 0
        if self.unknown_weight:
            for weight in self.weights:
                if type(weight.weight).__name__ == 'int':
                    if weight.unknown_weight:
                        x = weight.distance_from_center
                    else:
                        torque += weight.weight * weight.distance_from_center
                else:
                    torque += weight.weight.total_weight * \
                              weight.distance_from_center

            pan = torque / x
            if pan < 0:
                pan *= -1
            print('to balance beam ',self.name,'the weight of the unknown '
                                               'pan should be',pan)
        else:
            for weight in self.weights:
                if type(weight).__name__ != 'int':
                    if type(weight.weight).__name__ != 'int':
                        weight.weight.calculate_torque()




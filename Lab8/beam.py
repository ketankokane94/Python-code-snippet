
from Weights import  Weight

class Beam:
    __slots__ = 'balanced','unknown_weight','total_weight','name','weights'

    def __init__(self,name):
        self.name = name
        self.balanced  = False
        self.unknown_weight = False
        self.total_weight = 0
        self.weights = []

    def add_weight(self,w):
        if type(w.weight).__name__ != 'int':
            self.weights.append(w)
            self.total_weight +=w.weight.total_weight
        else:
            self.weights.append(w)
            self.total_weight += w.weight


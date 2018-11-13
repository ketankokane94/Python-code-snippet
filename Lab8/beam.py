
from Weights import  Weight

class Beam:
    __slots__ = 'balanced','unknown_weight','total_weight','name','weights'

    def __init__(self,name):
        self.name = name
        self.balanced  = False
        self.unknown_weight = False
        self.total_weight = 0
        self.weights = []

    def calculate_torque(self):
        pass


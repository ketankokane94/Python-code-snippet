from beam import Beam
from Weights import Weight

tree_data = {}

def read_file():
    with open('test.txt') as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(' ')
            tree_data[line[0]] = line



def create_beam(data):
    beam = Beam(data[0])
    for _ in range(1,len(data),2):
    # if even then its the location
    # its either the weight or the beam name
        if 'B' in data[_+1]:

            pass
        else:
            w = Weight(int(data[_+1]),data[_])
            beam.weights.append(w)
    return beam




if __name__ == '__main__':
    read_file()
    print(tree_data)
    beam = create_beam(tree_data['B'])
    print(beam)
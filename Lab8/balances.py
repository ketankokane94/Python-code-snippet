from beam import Beam
from Weights import Weight
import turtle

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
            w = Weight(create_beam(tree_data[data[_+1]]),data[_])
            beam.add_weight(w)
            #beam.weights.append(w)
        else:
            w = Weight(int(data[_+1]),data[_])
            beam.add_weight(w)
            #beam.weights.append(w)
    return beam


def align_turtle(my_turtle,forward_length):
    my_turtle.right(90)
    my_turtle.forward(forward_length)
    my_turtle.left(90)


def drawBeam(beam,my_turtle,vertical_factor = 30):
    '''
    pre 0 0 east
    post 0 0 east
    :param beam:
    :param my_turtle:
    :return:
    '''
    horizontal_factor = 40
    my_turtle.write(beam.name,align="left", font=("Arial", 16, "normal"))
    start = my_turtle.position()
    for weight in beam.weights:
        dis = weight.distance_from_center * horizontal_factor
        print(dis)
        my_turtle.forward(dis)
        if type(weight.weight).__name__ != 'int':
            vertical_factor +=30
            align_turtle(my_turtle,vertical_factor)
            drawBeam(weight.weight,my_turtle)
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()
        else:
            align_turtle(my_turtle,vertical_factor)
            my_turtle.write(weight.weight,align="center", font=("Arial", 16,
                                                           "normal"))
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()




if __name__ == '__main__':
    read_file()
    print(tree_data)
    beam = create_beam(tree_data['B'])
    print(beam)
    my_turtle = turtle.Turtle()
    my_turtle.speed(6)
    my_turtle.up()
    my_turtle.setpos(0,300)
    my_turtle.down()
    drawBeam(beam,my_turtle)
    turtle.done()
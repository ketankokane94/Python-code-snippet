#todo
from beam import Beam
#todo
from Weights import Weight
import turtle

# python dictionary to store data read from text file
tree_data = {}


def read_file():
    with open('test.txt') as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(' ')
            # key value pair e.g. 'B' : [B -1 B1 1 B3 8 2]
            tree_data[line[0]] = line


def create_beam(data):
    beam = Beam(data[0])
    for _ in range(1,len(data), 2):
    # if even then its the location
    # its either the weight or the beam name
        if 'B' in data[_+1]:
            w = Weight(create_beam(tree_data[data[_+1]]), data[_])
            beam.add_weight(w)
        else:
            w = Weight(int(data[_+1]),data[_])
            beam.add_weight(w)
    return beam


def align_turtle(t, forward_length):
    t.right(90)
    t.forward(forward_length)
    t.left(90)


def make_anotation(t, name):
    t.up()
    t.right(90)
    t.fd(20)
    t.down()
    t.write(name, align="left", font=("Arial", 16, "normal"))
    t.up()
    t.fd(-20)
    t.left(90)
    t.down()


def drawBeam(beam, my_turtle, vertical_factor = 10, horizontal_factor = 50):
    '''
    pre 0 0 east
    post 0 0 east
    :param beam:
    :param my_turtle:
    :return:
    '''

    #make_anotation(my_turtle, beam.name)
    my_turtle.circle(3)
    start = my_turtle.position()
    number_of_things_hanging = 1 + determine_horizontal_factor(beam, depth=0)
    horizontal_factor = (horizontal_factor // number_of_things_hanging)

    for weight in beam.weights:
        dis = weight.distance_from_center * horizontal_factor
        my_turtle.forward(dis)
        if type(weight.weight).__name__ != 'int':
            align_turtle(my_turtle, vertical_factor+30)
            drawBeam(weight.weight, my_turtle, vertical_factor+30,
                     horizontal_factor)
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()
        else:
            align_turtle(my_turtle,vertical_factor)
            make_anotation(my_turtle, weight.weight)
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()


def compute_blank_value():
    if beam.unknown_weight:
        beam.calculate_torque()
    else:
        for weight in beam.weights:
            if type(weight).__name__ != 'int':
                if type(weight.weight).__name__ != 'int':
                    weight.weight.calculate_torque()


def determine_horizontal_factor(beam, depth):
    if depth < 0:
        return 0
    number_of_pan_hanging = 1
    for thing_hanging in beam.weights:
        if type(thing_hanging.weight).__name__ == 'int':
            number_of_pan_hanging += 1
        else:
            number_of_pan_hanging += determine_horizontal_factor(
                thing_hanging.weight, depth-1)

    return number_of_pan_hanging


if __name__ == '__main__':
    read_file()
    beam = create_beam(tree_data['B'])
    my_turtle = turtle.Turtle()
    turtle.setup(width=1400, height=800)
    #my_turtle.speed(6)
    my_turtle.up()
    my_turtle.setpos(0, 300)
    my_turtle.down()
    #drawBeam(beam,my_turtle, horizontal_factor=800)
    compute_blank_value()
    turtle.done()


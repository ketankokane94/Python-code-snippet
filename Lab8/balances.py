__author__='KK'
__author__='SB'

"""

CSCI-603 Lab 8: Balanced Beams
This program reads an input file containing details about beams, weights and 
empty pans. The input file is of the format beam,position,weight in order.
The code reads these details and draws the beam diagram using turtle.

If a weight is missing, the code computes the missing weight required to balance
the beam, then draws the beam diagram using turtle.

Author: Ketan Kokane
Author: Siddharth Bapat
"""

#todo
from beam import Beam
#todo
from Weights import Weight
import turtle

# python dictionary to store data read from text file
tree_data = {}


def read_file():
    """
    This function reads the given input file
    :return:
    """
    # each key value pair is added to the dictionary
    with open('test.txt') as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(' ')
            # key value pair e.g. 'B' : [B -1 B1 1 B3 8 2]
            tree_data[line[0]] = line


def create_beam(data):
    """
    This function creates a beam using the list of values passed
    :param data:
    :return:
    """
    #creates an object of the class Beam
    beam = Beam(data[0])
    for _ in range(1,len(data), 2):
    # if even then its the location
    # its either the weight or the beam name
        if 'B' in data[_+1]: #checking if the weight is another beam
            #recursive call to create further beams
            w = Weight(create_beam(tree_data[data[_+1]]), data[_])
            #add the weight(beam) to the weight list for this object
            beam.add_weight(w)
        else:
            #the weight is a weight and not a beam
            w = Weight(int(data[_+1]),data[_])
            #add the weight to the weight list for this object
            beam.add_weight(w)
    return beam


def align_turtle(t, forward_length):
    """
    This function aligns the turtle
    :param t:
    :param forward_length:
    :return:
    """
    t.right(90)
    t.forward(forward_length)
    t.left(90)


def make_anotation(t, name):
    """
    This function specifies the turtle movements
    :param t:
    :param name:
    :return:
    """
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
    This function draws the beams as per the data available
    pre 0 0 east
    post 0 0 east
    :param beam:
    :param my_turtle:
    :return:
    '''

    #make_anotation(my_turtle, beam.name)
    my_turtle.circle(3)
    start = my_turtle.position()
    #calculate the total number of weights hanging on the beam
    number_of_things_hanging = 1 + determine_horizontal_factor(beam, depth=0)
    horizontal_factor = (horizontal_factor // number_of_things_hanging)

    for weight in beam.weights:
        dis = weight.distance_from_center * horizontal_factor
        my_turtle.forward(dis)
        if type(weight.weight).__name__ != 'int':
            #if weight is a beam
            align_turtle(my_turtle, vertical_factor+30)
            drawBeam(weight.weight, my_turtle, vertical_factor+30,
                     horizontal_factor)
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()
        else:
            #if weight is a weight
            align_turtle(my_turtle,vertical_factor)
            make_anotation(my_turtle, weight.weight)
            my_turtle.up()
            my_turtle.goto(start)
            my_turtle.setheading(0)
            my_turtle.down()


def compute_blank_value():
    """
    This function determines if there exists an unknown weight.
    If present, it proceeds to calculate the weight required to insert into the
    empty pan to balance the beam
    :return:
    """
    if beam.unknown_weight:
        #beam contains an unknown weight so the weight to be inserted is
        #calculated
        beam.calculate_torque()
    else:
        #if there are sub-beams, it's weights are used to calculate the torgue
        for weight in beam.weights:
            if type(weight).__name__ != 'int':
                if type(weight.weight).__name__ != 'int':
                    weight.weight.calculate_torque()


def determine_horizontal_factor(beam, depth):
    """
    THis function returns the number of weights hanging on the beam
    :param beam:
    :param depth:
    :return:
    """
    if depth < 0:
        return 0
    number_of_pan_hanging = 1
    for thing_hanging in beam.weights:
        #if the weight is an integer value, add it to the number of weights
        if type(thing_hanging.weight).__name__ == 'int':
            number_of_pan_hanging += 1
        else:
            #if it is a beam, this function is called again to compute the
            #number of weights in the inner beam
            number_of_pan_hanging += determine_horizontal_factor(
                thing_hanging.weight, depth-1)

    return number_of_pan_hanging


if __name__ == '__main__':
    read_file()
    #creating a beam using the list of values for 'B' to begin with
    beam = create_beam(tree_data['B'])
    my_turtle = turtle.Turtle()
    turtle.setup(width=1400, height=800)
    my_turtle.speed(6)
    my_turtle.up()
    my_turtle.setpos(0, 300)
    my_turtle.down()
    #draws the beams and weights as per the data available
    drawBeam(beam,my_turtle, horizontal_factor=800)
    #check if there are empty pans(unknown weights)
    compute_blank_value()
    turtle.done()
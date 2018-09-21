# Every function is worked out by Pre Post Condition
# @author : Ketan Balbhim Kokane


import math
import turtle

# A Reusable function to draw A, no points are hard coded

def draw_a():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    my_turtle.down()
    my_turtle.left(90)
    my_turtle.fd(Height)
    my_turtle.right(90)
    my_turtle.fd(Width)
    my_turtle.right(90)
    draw_line(Height)
    my_turtle.down()
    my_turtle.fd(Height/2)
    my_turtle.right(90)
    my_turtle.fd(Width)
    my_turtle.up()
    go_to_start_position()


def draw_e():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    draw_line(Width)
    my_turtle.left(90)
    draw_line(Height)
    my_turtle.fd(Height/2)
    my_turtle.right(90)
    draw_line(Width)
    my_turtle.left(90)
    my_turtle.fd(Height/2)
    my_turtle.right(90)
    draw_line(Width)
    my_turtle.up()
    go_to_start_position()


def draw_t():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    my_turtle.left(90)
    my_turtle.fd(Height)
    my_turtle.right(90)
    draw_line(Width)
    my_turtle.fd(Width/2)
    my_turtle.right(90)
    my_turtle.down()
    my_turtle.fd(Height)
    my_turtle.up()
    go_to_start_position()


def draw_k():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    half_of_height = Height/2
    my_turtle.left(90)
    draw_line(Height)
    my_turtle.fd(half_of_height)
    my_turtle.right(45)
    draw_line(half_of_height * math.sqrt(2))
    my_turtle.right(90)
    draw_line(half_of_height * math.sqrt(2))
    my_turtle.up()
    go_to_start_position()


def space():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    my_turtle.fd(Width+10)


# Function to draw a line and come back to the start position, to remove duplicated block of code
def draw_line(length):
    # Pre: Pos (0,0), Heading Unknown, UP
    # Post: Pos (0,0),Same Heading as Pre , UP
    my_turtle.down()
    my_turtle.fd(length)
    my_turtle.bk(length)
    my_turtle.up()


def draw_n():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    my_turtle.down()
    my_turtle.left(90)
    my_turtle.fd(Height)
    pos = my_turtle.position()
    my_turtle.right(90)
    my_turtle.up()
    my_turtle.fd(Width)
    my_turtle.down()
    my_turtle.right(90)
    my_turtle.fd(Height)
    my_turtle.right(150)
    my_turtle.goto(pos)
    my_turtle.up()
    go_to_start_position()


def draw_o():
    # Pre: Pos (0,0), Head East, UP
    # Post: Pos (0,0), Head East, UP
    note_start_position()
    my_turtle.down()
    my_turtle.fd(Width)
    my_turtle.left(90)
    my_turtle.fd(Height)
    my_turtle.left(90)
    my_turtle.fd(Width)
    my_turtle.left(90)
    my_turtle.fd(Height)
    go_to_start_position()


# instead of every character having to figure out how to go back to the initial position, used a generic function which stores the initial position
# of the turtle before starting to draw anything and once the character is draw simply returns to the start position, using goto function 
def go_to_start_position():
    my_turtle.up()
    my_turtle.goto(start_pos)
    my_turtle.setheading(0)


def note_start_position():
    global start_pos
    start_pos = my_turtle.position()

def draw_first_name():
    draw_k()
    space()
    draw_e()
    space()
    draw_t()
    space()
    draw_a()
    space()
    draw_n()



def draw_last_name():
    draw_k()
    space()
    draw_o()
    space()
    draw_k()
    space()
    draw_a()
    space()
    draw_n()
    space()
    draw_e()
    space()


start_pos = (0, 0)
my_turtle = turtle.Turtle()
my_turtle.up()
my_turtle.setposition(-300, 100)
Height = 100
Width = 50

draw_first_name()
my_turtle.setposition(-300, -100)
draw_last_name()
turtle.done()

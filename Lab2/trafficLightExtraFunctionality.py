import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()

# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)

# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1

    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2

    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# Adjust the turtle's pen width
def increase_pen_size():
    current_size = tess.width()
    tess.width(current_size + 1)
    
    if current_size + 1 > 20:
        tess.width(20)

def decrease_pen_size():
    current_size = tess.width()
    tess.width(current_size - 1)
    
    if current_size - 1 < 1:
        tess.width(1)

# Change the turtle's color
def color_red():
    tess.color('red')

def color_green():
    tess.color('green')

def color_yellow():
    tess.color('yellow')

# Move the turtle
def move_forward():
    tess.forward(5)

def turn_left():
    tess.left(15)

def turn_right():
    tess.right(15)

# Change circle size
def increase_circle():
    (current_size, _, _) = tess.shapesize()
    if current_size < 20:
        tess.shapesize(current_size + 1)

def decrease_circle():
    (current_size, _, _) = tess.shapesize()
    if current_size > 1:
        tess.shapesize(current_size - 1)

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(increase_pen_size, "plus")
wn.onkey(decrease_pen_size, "minus")

wn.onkey(color_red, "r")
wn.onkey(color_yellow, "y")
wn.onkey(color_green, "g")

wn.onkey(move_forward, 'Up')
wn.onkey(turn_left, 'Left')
wn.onkey(turn_right, 'Right')

wn.onkey(increase_circle, 'i')
wn.onkey(decrease_circle, 'o')

wn.listen() # Listen for events
wn.mainloop()
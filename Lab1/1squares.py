import turtle

window = turtle.Screen()
artist = turtle.Turtle()

# draw the squares
for i in range(5):
    # draw the current square
    for side in range(4):
        artist.forward(20 + 20 * i)
        artist.left(90)

    # stop drawing
    artist.penup()

    # get position and move to start of next square
    position = artist.position()
    artist.goto(position[0] - 10, position[1] - 10)

    # start drawing
    artist.pendown()

window.mainloop()
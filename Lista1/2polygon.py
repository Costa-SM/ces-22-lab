import turtle

def draw_poly(t, n, sz):
    """
    :param t: turtle in canvas.
    :type t: Turtle.
    :param n: number of polygon sides.
    :type n: int.
    :param sz: length of the polygon side.
    :type sz: int.
    """
    
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)



window = turtle.Screen()
artist = turtle.Turtle()

draw_poly(artist, 8, 50)

window.mainloop()
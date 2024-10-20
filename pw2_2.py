import turtle

def draw_axes():

    turtle.goto(-170, 0)
    turtle.color("blue")
    turtle.forward(340)  # Draw x
    turtle.penup()
    turtle.goto(0, -170)
    turtle.pendown()
    turtle.left(90)
    turtle.color("blue")
    turtle.forward(340)  # Draw y

def plot_function():
    turtle.color("red")
    turtle.penup()
    turtle.goto(-160, (-160 / 5) + 7)
    turtle.pendown()
    for x in range(-160, 160):
        y = x / 5 + 7
        turtle.goto(x, y)

turtle.speed(0)
draw_axes()
plot_function()
turtle.done()


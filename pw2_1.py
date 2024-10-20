import turtle

def draw_star(n, length):

    if n % 2 == 0:
        print("n must be odd.")
        return
    if n == 1 or n == 3:
        print("n cannot be 1 or 3.")
        return

    angle = 180 - 180/n  

    for n in range(n):
        turtle.forward(length)
        turtle.right(angle)


turtle.speed(0) 
draw_star(21, 300)  
turtle.done()

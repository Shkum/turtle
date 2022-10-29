import turtle

window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')

border = turtle.Turtle()
border.up()
border.speed(5)
border.goto(-500, 300)
border.color('green')
border.begin_fill()
border.pensize(10)
border.down()
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270)
border.hideturtle()
for i in range(25):
    if i % 2:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()




window.mainloop()

import turtle, random, time

window = turtle.Screen()

border = turtle.Turtle()
border.speed(5)
border.color('red')
border.pensize(6)
border.penup()
border.goto(300, 300)
border.pendown()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
dx = 5
dy = 5
ball.up()
ball.speed(3)

ball.goto(random.randint(-290, 290), random.randint(-295, 295))
ball.showturtle()
ball.color('blue')

while True:
    x, y = ball.position()

    ball.goto(x + dx, y + dy)
    if x + dx >= 290 or x + dx <= -290:
        dx = -dx
    if y + dy >= 290 or y + dy <= -290:
        dy = -dy

window.mainloop()

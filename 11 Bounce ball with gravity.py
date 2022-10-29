import turtle

window = turtle.Screen()
window.bgcolor('yellow')

border = turtle.Turtle()
border.up()
border.goto(-250, 250)
border.down()
border.pensize(10)
border.color('red')
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)

ball = turtle.Turtle(shape='circle')
ball.up()
ball.hideturtle()
ball.color('blue')
ball.goto(0, 240)
ball.showturtle()

ball.speedY = -1
ball.speedX = 2

gravity = 0.1

while True:
    ball.speedY -= gravity
    ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
    if ball.ycor() < -245:
        ball.speedY = -ball.speedY
    if ball.xcor() > 245 or ball.xcor() < -245:
        ball.speedX = -ball.speedX

window.mainloop()
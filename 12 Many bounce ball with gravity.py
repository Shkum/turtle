import turtle, random

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

shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
balls = []
count = 5
for i in range(count):
    ball = turtle.Turtle(shape='circle')
    ball.up()
    ball.speed(0)
    ball.hideturtle()
    r = random.random()
    g = random.random()
    b = random.random()
    ball.shape(random.choice(shapes))
    ball.color(r, g, b)
    ball.goto(random.randint(-240, 240), 240)
    ball.showturtle()

    ball.speedY = -1
    ball.speedX = random.randint(-5, 5)
    balls.append(ball)

    ball.gravity = random.randint(5, 20) / 100

while True:
    for ball in balls:
        ball.speedY -= ball.gravity
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
        if ball.ycor() < -230:
            ball.speedY = -ball.speedY
        if ball.xcor() > 230 or ball.xcor() < -230:
            ball.speedX = -ball.speedX

window.mainloop()

import turtle, random

window = turtle.Screen()
window.bgcolor('yellow')
window.tracer(25)

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
count = 40

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

    ball.speedY = -2
    ball.angle = random.randint(-5, 5)
    ball.speedX = random.randint(-3, 3)
    balls.append(ball)

    ball.gravity = random.randint(1, 30) / 100

while True:
    window.update()
    for ball in balls:
        ball.left(ball.angle)
        ball.speedY -= ball.gravity
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
        if ball.ycor() < -230:
            ball.sety(-230)
            ball.speedY = -ball.speedY
        if ball.xcor() > 230 or ball.xcor() < -230:
            ball.speedX = -ball.speedX


        # radius = 15
        # for another_ball in balls:
        #     if another_ball == ball:
        #         continue
        #     if abs(another_ball.xcor() - ball.xcor()) < radius and abs(another_ball.ycor() - ball.ycor()) < radius:
        #         ball.speedX *= -1
        #         ball.speedY *= -1


window.mainloop()

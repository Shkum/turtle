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

balls = []
count = 5
# colors = ['red', 'green', 'blue', 'orange', 'yellow', 'pink']

for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('circle')
    # ball.color(random.choice(colors))

    r = random.random()
    g = random.random()
    b = random.random()
    ball.color(r, g ,b)

    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    ball.up()
    ball.speed(20)
    ball.goto(random.randint(-290, 290), random.randint(-295, 295))
    ball.showturtle()
    balls.append([ball, dx, dy])

while True:
    for i in range(count):
        balls[i]
        x, y = balls[i][0].position()
        if x + balls[i][1] >= 290 or x + balls[i][1] <= -290:
            balls[i][1] = -balls[i][1]
        if y + balls[i][2] >= 290 or y + balls[i][2] <= -290:
            balls[i][2] = -balls[i][2]
        balls[i][0].goto(x + balls[i][1], y + balls[i][2])

window.mainloop()

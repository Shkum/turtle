import turtle, time

pen = turtle.Turtle()


def starFill(n, dlina):
    pen.color('red')
    pen.begin_fill()
    star(n, dlina)
    pen.end_fill()


def star(n, dlina):
    if n % 2:
        for i in range(n):
            pen.forward(dlina)
            angle = n // 2 * 360 / n
            pen.left(angle)

for i in range(5, 16, 2):
    pen.speed(10)
    starFill(i, 200)
    time.sleep(1)
    pen.clear()

turtle.exitonclick()

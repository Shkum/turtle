import turtle

pen = turtle.Turtle()
pen.speed(50)
pen.up ()
pen.setposition(-30, -30)
pen.down()


def rightMNOG(n, dlina):
    sumAngle = (n - 2) * 180
    if sumAngle // n:
        angle = sumAngle // n
        for i in range(n):
            pen.forward(dlina)
            pen.left(180 - angle)



for i in range(3, 11):
    rightMNOG(i, 100)

turtle.exitonclick()

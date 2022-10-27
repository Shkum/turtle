import turtle, random


def starFill(n, dlina):
    pen.left(random.randint(10, 350))
    pen.begin_fill()
    if n % 2:
        for i in range(n):
            pen.forward(dlina)
            angle = n // 2 * 360 / n
            pen.left(angle)
    pen.end_fill()


window = turtle.Screen()
window.bgcolor('black')
window.setup(700, 500)
turtle.shape(name='circle')
pen = turtle.Turtle()
pen.color('yellow')
pen.speed(0)

pen.hideturtle()

for i in range(5):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220)
    size = random.randint(10, 20)
    vershina = random.choice([5, 7, 9, 11, 13, 15])
    clr = random.choice(['red', 'green', 'yellow', 'orange', 'blue'])
    pen.color(clr)
    pen.up()
    pen.setposition(x, y)
    pen.down()
    starFill(vershina, size)


def move(x, y):
    pen.up()
    pen.setposition(x, y)
    pen.down()
    clr = random.choice(['red', 'green', 'yellow', 'orange', 'blue'])
    pen.color(clr)
    size = random.randint(10, 20)
    vershina = random.choice([5, 7, 9, 11, 13, 15])
    starFill(vershina, size)


window.onclick(move)
window.listen()

turtle.mainloop()

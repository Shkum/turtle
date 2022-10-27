import turtle

speed = 5

def moveUp():
    x, y = pen.position()
    pen.setposition(x, y + speed)


def moveDown():
    x, y = pen.position()
    pen.setposition(x, y - speed)


def moveRight():
    x, y = pen.position()
    pen.setposition(x + speed, y)


def moveLeft():
    x, y = pen.position()
    pen.setposition(x - speed, y)

def change():
    if pen.isdown():
        pen.up()
    else:
        pen.down()

def speedUp():
    global speed
    speed += 5

def speedDown():
    global speed
    speed -= max(0, speed - 1)  # avoid negative mean of variable

window = turtle.Screen()
pen = turtle.Turtle()

# window.onkey(функция, клавиша)
window.onkey(moveUp, 'Up')
window.onkey(moveDown, 'Down')
window.onkey(moveRight, 'Right')
window.onkey(moveLeft, 'Left')
window.onkey(change, 'space')
window.onkey(speedUp, '+')
window.onkey(speedDown, '-')


window.listen()

window.mainloop()

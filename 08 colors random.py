import turtle, random, time

window = turtle.Screen()

colors = ['red', 'green', 'yellow', 'purple', 'orange']

def chooseRandomColor():
    red = random.random()  # 0 - 1
    green = random.random()
    blue = random.random()
    return red, green, blue

bob = turtle.Turtle()
bob.color(chooseRandomColor())
bob.forward(100)

while True:
    # window.bgcolor(random.choice(colors))

    # window.bgcolor(RED GREEN BLUE)


    window.bgcolor(chooseRandomColor())
    time.sleep(.5)

window.mainloop()

import turtle


def sq(a):
    for i in range(4):
        joe.color(colors[i % (len(colors))])
        joe.forward(a)
        joe.left(90)


colors = ['red',  'brown', 'green', 'blue']

joe = turtle.Turtle()
joe.speed(10000)

d = 30

for i in range(60):
    # sq(d)
    joe.circle(d)
    joe.right(10)
    d += 4

turtle.exitonclick()

# turtle.mainloop()           # Стандартное зацикливание из Tkinter
# turtle.done()               # Рисунок закончен
# turtle.exitonclick()        # Выход при нажатии мышкой в окне Turtle

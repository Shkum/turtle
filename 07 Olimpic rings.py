import turtle

window = turtle.Screen()

# pen = turtle.Turtle()

r = 80

europe = turtle.Turtle()
afrika = turtle.Turtle()
amerika = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europe, afrika, amerika, asia, australia]:
    i.up()

europe.goto(-2*r, 2*r)
afrika.goto(0, 2*r)
amerika.goto(2*r, 2*r)
asia.goto(-r, r)
australia.goto(r, r)

for i in [europe, afrika, amerika, asia, australia]:
    i.down()
    i.pensize(10)

europe.color('blue')
afrika.color('black')
amerika.color('red')
asia.color('yellow')
australia.color('green')

for i in [europe, afrika, amerika, asia, australia]:
    i.circle(r)

window.mainloop()

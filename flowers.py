import turtle

turtle.bgcolor('black')
turtle.speed(80)
turtle.hideturtle()

Colors = ["blue", "purple", "blue", "purple"]

for i in range(120):
    for c in Colors:
        turtle.color(c)
        turtle.circle(180-i, 80)
        turtle.lt(90)
        turtle.circle(180-i, 80)
        turtle.end_fill()

turtle.mainloop()
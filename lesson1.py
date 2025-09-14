from turtle import *

speed(15)
width(3)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# door time

forward(70)
color("orange")
begin_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()

width(3)
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10,115)
pendown()

left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(140, 115)
pendown()

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


exitonclick()

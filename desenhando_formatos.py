from turtle import *
shape("turtle")
speed(1)

#QUADRADO
color('red')
pensize(5)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

#INTERVALO
penup()
left(90)
backward(100)
right(90)
backward(100)
pendown()

#TRIÂNGULO
color("black")
pensize(5)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#INTERVALO
penup()
backward(500)
pendown()

#CASA
pensize(10)
forward(350)
right(90)
forward(175)
right(90)
forward(350)
right(90)
forward(175)

#TELHADO
color("blue")
pensize(10)
right(45)
forward(175)
right(45)
forward(227)
right(90)
forward(125)
penup()
forward(175)
right(90)
forward(227)
right(90)
pendown()
forward(300)


done()

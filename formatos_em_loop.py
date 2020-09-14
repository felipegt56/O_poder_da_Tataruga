speed(1)
shape("turtle")

#PENTAGONO
for count in range(5):
    color('red')
    forward(100)
    left(72)

penup()
backward(200)
pendown()

#HEXAGONO
for count in range(6):
    color('blue')
    forward(100)
    left(60)

penup()
backward(150)
pendown()

#CIRCULO
for count in range(360):
    color('black')
    forward(1)
    left(1)


done()

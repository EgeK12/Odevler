import turtle as t
t.speed("fastest")
t.penup()
t.goto(-400,0)
t.pendown()
t.right(-45)
t.color("blue")
t.forward(200)
t.color("green")
t.begin_fill()
t.forward(30)
t.left(270)
t.forward(30)
t.left(45)
t.end_fill()
t.color("blue")
t.right(45)
t.forward(200)
t.left(90)
t.forward(200)
t.color("green")
t.begin_fill()
t.forward(30)
t.left(270)
t.forward(30)
t.left(45)
t.end_fill()
t.color("blue")
t.right(45)
t.forward(150)
t.left(90)
t.color("blue")
t.forward(150)
t.color("green")
t.begin_fill()
t.forward(30)
t.left(270)
t.forward(30)
t.left(45)
t.end_fill()
t.color("blue")
t.right(45)
t.forward(200)

t.penup()
t.goto(-110,100)
t.color("orange")
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
t.color("black")
t.circle(50)

t.penup()
t.goto(-230,-100)
t.color("green")
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.color("black")
t.circle(40)

t.penup()
t.right(-45)
t.goto(-212,-112)
t.pendown()
t.forward(20)
t.right(90)
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(90)

t.penup()
t.goto(-70,-100)
t.color("green")
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.color("black")
t.circle(40)

t.penup()
t.goto(-120,-140)
t.right(-270)
t.pendown()
t.forward(20)
t.right(90)
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(90)

#Ağaçların kenar dallarını yapamadım.

t.mainloop()
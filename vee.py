import turtle

screen = turtle.Screen()
screen.bgcolor("black")

#create a turtle object
tom = turtle.Turtle()
tom.color('green')
tom.speed(0)
tom.width(5)



tom.penup()
tom.goto(-200, 100)
tom.pendown()

tom.fd(360)
tom.circle(-10,91)
tom.fd(200)
tom.circle(-10,89)
tom.fd(390)
tom.circle(-10,89)
tom.fd(200)
tom.circle(-10,91)
tom.fd(100)

tom.penup()
tom.goto(-160, 20)
tom.pendown()

tom.setheading(0)
tom.circle(1000,5)
tom.rt(90)
tom.circle(-50, 185)
tom.rt(90)
tom.fd(10)
tom.lt(135)
tom.fd(20)
tom.bk(20)
tom.rt(133)
tom.fd(20)
tom.lt(135)
tom.fd(20)
tom.bk(20)
tom.rt(135)
tom.rt(90)
tom.begin_fill()
tom.circle(25, 180)
tom.end_fill()

tom.penup()
tom.goto(10, 20)
tom.pendown()

tom.setheading(0)
tom.circle(1000,5)
tom.rt(90)
tom.circle(-50, 185)
tom.rt(90)
tom.fd(10)
tom.lt(135)
tom.fd(20)
tom.bk(20)
tom.rt(133)
tom.fd(20)
tom.lt(135)
tom.fd(20)
tom.bk(20)
tom.rt(135)
tom.rt(90)
tom.begin_fill()
tom.circle(25, 180)
tom.end_fill()


tom.penup()
tom.goto(-80, -50)
tom.pendown()

tom.rt(150)
tom.circle(50,125)
tom.rt(90)
tom.fd(10)
tom.bk(15)

#done
turtle.done()

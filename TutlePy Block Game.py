import turtle

#screen
screen = turtle.Screen()
screen.screensize(canvwidth = 618, canvheight = 618, bg = "black")

#border
turtle.speed(100)
turtle.penup()
turtle.goto(-363,-300)
turtle.color('white')
turtle.pendown()
turtle.pensize(4)
turtle.forward(720)
turtle.left(90)
turtle.forward(610)
turtle.left(90)
turtle.forward(720)
turtle.left(90)
turtle.forward(610)
turtle.hideturtle()
turtle.penup()

#spaceship
ship = turtle.Turtle()
ship.goto(0,0)
ship.shape("square")
ship.color("white")
ship.shapesize(1,1)
ship.penup()

#right_movement
def ship_right():
	x = ship.xcor()
	x += 20
	ship.setx(x)

#left_movement
def ship_left():
	x = ship.xcor()
	x -= 20
	ship.setx(x)

#up_movement
def ship_up():
	y = ship.ycor()
	y += 20
	ship.sety(y)

#down_movement
def ship_down():
	y = ship.ycor()
	y -= 20
	ship.sety(y)

#key_bindings
screen.onkey(ship_right, "d")
screen.onkey(ship_left, "a")
screen.onkey(ship_up, "w")
screen.onkey(ship_down, "s")

screen.listen()

turtle.done()
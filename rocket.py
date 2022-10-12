from time import sleep
import turtle
import random
import math
s = turtle.Screen()
s.setup(width = 550, height = 550)


incoming_missile = turtle.Turtle()
interceptor = turtle.Turtle()
incoming_missile.color("red")
incoming_missile.penup()
interceptor.color("blue")
interceptor.penup()

incoming_missile.hideturtle()
incoming_missile.goto(-250, -250)
incoming_missile.showturtle()
incoming_missile.left(45)

interceptor.hideturtle()
interceptor.goto(0, -250)
interceptor.showturtle()
interceptor.left(90)
while True:

        # incoming missile random movement
        direction = random.randint(0,14)

        if(direction >= 0 and direction <= 10):
           incoming_missile.forward(3)
        elif(direction == 12):
           incoming_missile.left(15)
           incoming_missile.forward(3)
        elif(direction == 13):
           incoming_missile.right(15)
           incoming_missile.forward(3)
        
        # target is up and left

        if(incoming_missile.xcor() < interceptor.xcor() and incoming_missile.ycor() > interceptor.ycor()):
            dx = interceptor.xcor() - incoming_missile.xcor()
            dy = incoming_missile.ycor() - interceptor.ycor()

            delta = dx / dy
            heading =math.degrees(math.atan(delta))
            interceptor.setheading(heading + 90)

        # target is up and right

        if(incoming_missile.xcor() > interceptor.xcor() and incoming_missile.ycor() > interceptor.ycor()):
            dx = incoming_missile.xcor() - interceptor.xcor()
            dy = incoming_missile.ycor() - interceptor.ycor()

            delta = dx / dy
            heading =math.degrees(math.atan(delta))
            interceptor.setheading(90 - heading)

        # target is down and right

        if(incoming_missile.xcor() > interceptor.xcor() and incoming_missile.ycor() < interceptor.ycor()):
            dx = incoming_missile.xcor() - interceptor.xcor()
            dy = interceptor.ycor() - incoming_missile.ycor()

            delta = dy / dx
            heading =math.degrees(math.atan(delta))
            interceptor.setheading(360 - heading)


        interceptor.forward(3)
        
        
turtle.done()

from time import sleep
import turtle
import random
import math
s = turtle.Screen()
s.setup(width = 550, height = 550)

# set up both missiles
incoming_missile = turtle.Turtle()
incoming_missile.hideturtle()

interceptor = turtle.Turtle()
interceptor.hideturtle()

incoming_missile.color("red")
incoming_missile.penup()
interceptor.color("blue")
interceptor.penup()

# incoming missile in left corner
incoming_missile.goto(-250, -250)
incoming_missile.showturtle()
incoming_missile.left(45)

# interceptor missile in bottom center
interceptor.goto(0, -250)
interceptor.showturtle()
interceptor.left(90)
while True:

        # incoming missile random movement
        direction = random.randint(-10, 10) #maximum of 10 degrees

        incoming_missile.setheading(direction + incoming_missile.heading())
        incoming_missile.forward(5)
        
        # target is up and left

        if(incoming_missile.xcor() < interceptor.xcor() and incoming_missile.ycor() > interceptor.ycor()):
            dx = interceptor.xcor() - incoming_missile.xcor()
            dy = incoming_missile.ycor() - interceptor.ycor()

            delta = dx / dy
            heading =math.degrees(math.atan(delta))
            interceptor.setheading(heading + 90)

        # we get the interceptor heading by calculating the arctangent in the rectangle formed by the x and y coordinates
        # then convert it to degrees and offest it from de horizontal for each case

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

        # target is down and left

        if(incoming_missile.xcor() < interceptor.xcor() and incoming_missile.ycor() < interceptor.ycor()):
            dx = interceptor.xcor() - incoming_missile.xcor()
            dy = interceptor.ycor() - incoming_missile.ycor()

            delta = dy / dx
            heading =math.degrees(math.atan(delta))
            interceptor.setheading(180 + heading)

        interceptor.forward(3)

        # if the interceptor is on the right course it will accelerate
        if(abs(incoming_missile.heading() - interceptor.heading()) < 20):
            interceptor.forward(10)

        # when the missiles colide

        if((interceptor.distance(incoming_missile)) < 3):
            
            # new turtle to draw the explosion
            incoming_missile.hideturtle()
            interceptor.hideturtle()
            explosion = turtle.Turtle()
            explosion.hideturtle()
            explosion.color("orange")
            explosion.pensize(1)
            explosion.penup()
            explosion.goto(incoming_missile.pos())
            explosion.pendown()

            #draw explosion
            for i in range(20):
                angle = random.randint(0, 45)
                distance = random.randint(0 ,30)
                explosion.right(angle)
                explosion.forward(distance)
                explosion.backward(distance)

            break


        
        
turtle.done()

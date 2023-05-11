import turtle as t
import time
import random

delay = 0.1
bodyParts = []
speed = 1

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)

head = t.Turtle(shape="square")
head.color("lime green")
head.speed(speed)
head.penup()
head.turtlesize(1)
head.goto(0,0)

food = t.Turtle(shape="square")
food.color("red")
food.speed(0)
food.penup()
food.goto(80,0)
food.turtlesize(0.5)

def up():
    if head.heading != "down":
        head.heading = "up"
def left():
    if head.heading != "right":
        head.heading = "left"
def right():
    if head.heading != "left":
        head.heading = "right"
def down():
    if head.heading != "up":
        head.heading = "down"
def move():
    if head.heading == "up":
        head.sety(head.ycor()+20)
    elif head.heading == "down":
        head.sety(head.ycor()-20)
    elif head.heading == "right":
        head.setx(head.xcor()+20)
    elif head.heading == "left":
        head.setx(head.xcor()-20)

def hideTheBodyParts():
    global bodyParts
    head.goto(0,0)
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts = []

wn.onkeypress(up,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")
wn.listen()

while True:
    wn.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        hideTheBodyParts()
    
    if head.distance(food) < 20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        speed += 5
        
        part = t.Turtle(shape="square")
        part.color("lime green")
        part.speed(speed)
        part.turtlesize(0.9)
        part.penup()
        bodyParts.append(part)

    for i in range(len(bodyParts)-1,0,-1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
     
    if len(bodyParts)>0:
              x=head.xcor()
              y=head.ycor()
              bodyParts[0].goto(x,y)

    move()
    
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()

    head.speed(speed)
 
    time.sleep(delay)

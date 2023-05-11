import turtle as t
import time
import random as r

delay = 0.1
bodyParts = []
bodyPartsA = []
speed = 2
speedA = 2
run = r.randint(0,3)

n = 20 
m = 14

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)

head = t.Turtle(shape="square")
head.color("lime green")
head.speed(speed)
head.penup()
head.turtlesize(1)
head.goto(20,0)
head.setheading = "up"

headA = t.Turtle(shape="square")
headA.color("sky blue")
headA.speed(speed)
headA.penup()
headA.turtlesize(1)
headA.goto(-20,0)
headA.setheading = "up"

food = t.Turtle(shape="square")
food.color("red")
food.speed(0)
food.penup()
food.goto(0,40)
food.turtlesize(0.5)

place = list(range(n, (m+1)*n, n))
negplace=[-x for x in place]
place.extend(negplace)

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
    head.goto(20,0)
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts = []

wn.onkeypress(up,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")
wn.listen()

def upA():
    if headA.heading != "down":
        headA.heading = "up"
        headA.sety(headA.ycor()+20)
def leftA():
    if headA.heading != "right":
        headA.heading = "left"
        headA.setx(headA.xcor()-20)
def rightA():
    if headA.heading != "left":
        headA.heading = "right"
        headA.setx(headA.xcor()+20)
def downA():
    if headA.heading != "up":
        headA.heading = "down"
        headA.sety(headA.ycor()-20)

def hideTheBodyPartsA():
    global bodyPartsA
    headA.goto(-20,0)
    for eachPart in bodyPartsA:
        eachPart.goto(1000,1000)
    bodyPartsA = []
 
while True:
    wn.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        hideTheBodyParts()
    
    if head.distance(food) < 20:
        food.goto(r.choice(place),r.choice(place))
         
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

    if headA.xcor() > 290 or headA.xcor() < -290 or headA.ycor() > 290 or headA.ycor() < -290:
        hideTheBodyPartsA()

    if headA.distance(food) < 20:
        food.goto(r.choice(place),r.choice(place))
        
        speedA += 5
        
        partA = t.Turtle(shape="square")
        partA.color("sky blue")
        partA.speed(speedA)
        partA.turtlesize(0.9)
        partA.penup()
        bodyPartsA.append(partA)

    for i in range(len(bodyPartsA)-1,0,-1):
        x=bodyPartsA[i-1].xcor()
        y=bodyPartsA[i-1].ycor()
        bodyPartsA[i].goto(x,y)
     
    if len(bodyPartsA)>0:
              x=headA.xcor()
              y=headA.ycor()
              bodyPartsA[0].goto(x,y)

    if headA.ycor() > food.ycor():
        downA()
    elif headA.ycor() < food.ycor():
        upA()
    if headA.xcor() > food.xcor():
        leftA()
    elif headA.xcor() < food.xcor():
        rightA()
         
    move()
    
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()

    for partA in bodyPartsA:
        if partA.distance(headA) < 10:
            hideTheBodyPartsA()

    for part in bodyParts:
        if part.distance(headA) < 10:
            hideTheBodyPartsA()
            
    for parta in bodyPartsA:
        if parta.distance(head) < 10:
            hideTheBodyParts()
            
    if head.distance(headA) < 10:
        hideTheBodyParts()
        hideTheBodyPartsA()

    head.speed(speed)
    headA.speed(speedA)
 
    time.sleep(delay)

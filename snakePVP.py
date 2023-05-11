import turtle as t
import time
import random

delay = 0.02
bodyParts = []
bodyPartsa = []
speed = 1
speeda = 1

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)

head = t.Turtle(shape="square")
head.color("lime green")
head.speed(speed)
head.penup()
head.turtlesize(1)
head.goto(20,0)

heada = t.Turtle(shape="square")
heada.color("sky blue")
heada.speed(speeda)
heada.penup()
heada.turtlesize(1)
heada.goto(-20,0)

food = t.Turtle(shape="square")
food.color("red")
food.speed(0)
food.penup()
food.goto(0,100)
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

def upa():
    if heada.heading != "down":
        heada.heading = "up"
def lefta():
    if heada.heading != "right":
        heada.heading = "left"
def righta():
    if heada.heading != "left":
        heada.heading = "right"
def downa():
    if heada.heading != "up":
        heada.heading = "down"
def movea():
    if heada.heading == "up":
        heada.sety(heada.ycor()+20)
    elif heada.heading == "down":
        heada.sety(heada.ycor()-20)
    elif heada.heading == "right":
        heada.setx(heada.xcor()+20)
    elif heada.heading == "left":
        heada.setx(heada.xcor()-20)

def hideTheBodyPartsa():
    global bodyPartsa
    heada.goto(-40,0)
    for eachParta in bodyPartsa:
        eachParta.goto(1000,1000)
    bodyPartsa = []

wn.onkeypress(upa,"i")
wn.onkeypress(lefta,"j")
wn.onkeypress(righta,"l")
wn.onkeypress(downa,"k")
wn.listen()

while True:
    wn.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        hideTheBodyParts()
    
    if heada.xcor() > 290 or heada.xcor() < -290 or heada.ycor() > 290 or heada.ycor() < -290:
        hideTheBodyPartsa()
    
    if head.distance(food) < 20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        speed += 5
        
        part = t.Turtle(shape="square")
        part.color("lime green")
        part.speed(0)
        part.turtlesize(0.9)
        part.penup()
        bodyParts.append(part)
        
    if heada.distance(food) < 20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        speeda += 5
        
        parta = t.Turtle(shape="square")
        parta.color("sky blue")
        parta.speed(0)
        parta.turtlesize(0.9)
        parta.penup()
        bodyPartsa.append(parta)

    for i in range(len(bodyParts)-1,0,-1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
     
    if len(bodyParts)>0:
              x=head.xcor()
              y=head.ycor()
              bodyParts[0].goto(x,y)
              
    for j in range(len(bodyPartsa)-1,0,-1):
        x=bodyPartsa[j-1].xcor()
        y=bodyPartsa[j-1].ycor()
        bodyPartsa[j].goto(x,y)
     
    if len(bodyPartsa)>0:
              x=heada.xcor()
              y=heada.ycor()
              bodyPartsa[0].goto(x,y)
    
    move()
    movea()
    
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()
            
    for parta in bodyPartsa:
        if parta.distance(heada) < 10:
            hideTheBodyPartsa()
    
    for part in bodyParts:
        if part.distance(heada) < 10:
            hideTheBodyPartsa()
            
    for parta in bodyPartsa:
        if parta.distance(head) < 10:
            hideTheBodyParts()
            
    if head.distance(heada) < 10:
        hideTheBodyParts()
        hideTheBodyPartsa()
    
    
    head.speed(speed)
    heada.speed(speeda)
    
    
    time.sleep(delay)

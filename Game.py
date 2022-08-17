#libraries
import turtle
import random
from tkinter import *
import pygame

#gameScreen
form = turtle.Screen()
form.screensize(600,600)
form.title('Turtle Game')
form.bgcolor("lightblue")
form.tracer(2)#oyun hızı

#turtle
size=2
player = turtle.Turtle()
player.color('black')
player.shape('turtle')
player.shapesize(size)
player.penup() #bir şekil çizmeyeceğini belirtiyor

#good foods
maxGoodFoods=5
goodFoods=[]
for i in range(maxGoodFoods):
    goodFoods.append(turtle.Turtle())
    goodFoods[i].penup()
    goodFoods[i].color('green')
    goodFoods[i].shape('circle')
    goodFoods[i].shapesize(random.randint(1,2))
    goodFoods[i].speed(0)
    goodFoods[i].setposition(random.randint(-310,310),random.randint(-310,310))#biraz sınır dışından aldım çünkü kaybolsun yön değiştirsin diye

#bad foods
maxBadFoods=5
badFoods=[]
for i in range(maxBadFoods):
    badFoods.append(turtle.Turtle())
    badFoods[i].penup()
    badFoods[i].color('red')
    badFoods[i].shape('circle')
    badFoods[i].shapesize(random.randint(1,2))
    badFoods[i].speed(0)
    badFoods[i].setposition(random.randint(-310,310),random.randint(-310,310))

#score
score=0
displayScore=turtle.Turtle()
displayScore.speed(0)
displayScore.color('black')
displayScore.penup()
displayScore.hideturtle() #şekli gizliyor çizmiyor...
displayScore.goto(-300,300)#ekrandaki konumu belirler
displayScore.write("Score= {}".format(score), align="center", font=("Courier", 24, "bold"))

#speed
speed=1
displaySpeed=turtle.Turtle()
displaySpeed.speed(0)
displaySpeed.color('black')
displaySpeed.penup()
displaySpeed.hideturtle() #şekli gizliyor çizmiyor...
displaySpeed.goto(-90,300)#ekrandaki konumu belirler
displaySpeed.write("Speed= {}x".format(speed), align="center", font=("Courier", 24, "bold"))


#functions
def moveLeft():
    player.left(30)

def moveRight():
    player.right(30)

def increaseSpeed():
    global speed
    speed+=1
    displaySpeed.clear()
    displaySpeed.write("Speed= {}x".format(speed), align="center", font=("Courier", 24, "bold"))

def decreaseSpeed():
    global speed
    speed-=1
    displaySpeed.clear()
    displaySpeed.write("Speed= {}x".format(speed), align="center", font=("Courier", 24, "bold"))

def stopGame():
    global stop
    if stop==True:
        stop=False
    else:
        stop=True


#-----------------
def restartGame():
    global game,score,stop,speed
    if not game:
        score=0
        speed=1
        loseGame.clear()
        form.bgcolor("lightblue")
#-----------------


#keyboard actions
form.listen()
form.onkey(moveLeft, 'Left')
form.onkey(moveRight, 'Right')
form.onkey(increaseSpeed, 'Up')
form.onkey(decreaseSpeed, 'Down')
form.onkey(stopGame,'p' or 'P')
form.onkey(restartGame,'r')


game=True
stop=False
#main 
while game:
    form.update()
    if not stop:
        #background
        #pic=pygame.image.load("deneme.png")
        #form.blit(pic,(0,0))

        player.forward(speed)

        #border check
        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180)
        if player.ycor() >300 or player.ycor() <-300:
            player.left(180)

        
        #goodFood
        for i in range(maxGoodFoods):
            goodFoods[i].forward(3)

            #good food hareketleri
            if goodFoods[i].xcor() > 500 or goodFoods[i].xcor() < -500:
                goodFoods[i].right(random.randint(150,250))
            if goodFoods[i].ycor() > 500 or goodFoods[i].ycor() < -500:
                goodFoods[i].right(random.randint(150,250))

            #when turtle eat food=oyuncu ve hedef arasındaki uzaklığı ölçer eğer değerse işlem yapar
            if player.distance(goodFoods[i]) < 40:
                goodFoods[i].setposition(random.randint(-300,300),random.randint(-300,300))
                
                #size arttırma
                size=size+1
                player.shapesize(size)
        
                #oyun kazanma
                if score >9:
                    #game=False
                    form.bgcolor("green")
                    winGame=turtle.Turtle()
                    winGame.speed(0)
                    winGame.color('white')
                    winGame.penup()
                    winGame.hideturtle()   
                    winGame.goto(0,0)
                    winGame.write("YOU WON!!!", align="center", font=("Courier", 35, "bold"))

                #hedeflerin açı değiştirmesi için 
                goodFoods[i].right(random.randint(0,360))
                
                #goodfood yendiğinde puan artacak
                score+=1
                displayScore.clear()
                displayScore.write("Score= {}".format(score), align="center", font=("Courier", 24, "bold"))

        #bad foods
        for i in range(maxBadFoods):
            badFoods[i].forward(3)

            #food hareketleri
            if badFoods[i].xcor() > 500 or badFoods[i].xcor() < -500:
                badFoods[i].right(random.randint(150,250))
            if badFoods[i].ycor() > 500 or badFoods[i].ycor() < -500:
                badFoods[i].right(random.randint(150,250))

            #when turtle eat food=oyuncu ve hedef arasındaki uzaklığı ölçer eğer değerse işlem yapar
            if player.distance(badFoods[i]) < 40:
                badFoods[i].setposition(random.randint(-300,300),random.randint(-300,300))
                
                #size düşürme
                if size <=0:
                    size=1
                else:
                    size=size-1
                    player.shapesize(size)

                #hedeflerin açı değiştirmesi için 
                badFoods[i].right(random.randint(0,360))
                
                #badfood yendiğinde puan azalacak
                score-=1
                displayScore.clear()
                displayScore.write("Score= {}".format(score), align="center", font=("Courier", 24, "bold"))
        
        #oyunu kaybedince
        if score <0:
            game=False
            form.bgcolor("red")
            loseGame=turtle.Turtle()
            loseGame.speed(0)
            loseGame.color('white')
            loseGame.penup()
            loseGame.hideturtle()   #şekli gizliyor çizmiyor...
            loseGame.goto(0,0)      #ekrandaki konumu belirler
            loseGame.write("GAME OVER!\nPress R to restart...", align="center", font=("Courier", 35, "bold"))
            form.exitonclick()
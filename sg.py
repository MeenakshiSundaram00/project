import turtle
import random
field=turtle.Screen()
field.bgpic("field.gif")
field.addshape("right.gif")
field.addshape("left.gif")
field.addshape("body.gif")
field.addshape("up.gif")
field.addshape("down.gif")
segmant=[]
food=turtle.Turtle()
food.penup()
food.goto(200,200)
food.speed(0)
food.color("red")
snake=turtle.Turtle()
snake.penup()
snake.speed(0)
snake.shape("right.gif")
result=turtle.Turtle()
result.penup()
result.goto(0,300)
result.write("score 0")
score=0
food.color("red")
food.shape("circle")
snake.speed(30)
def move():
    snake.forward(10)
def right():
    if snake.heading()!=180:
     snake.shape("right.gif")
     snake.setheading(0)


def left():
   if snake.heading()!=0:
      snake.shape("left.gif")
      snake.setheading(180)
def up():
   if snake.heading()!=270:
      snake.shape("up.gif")
      snake.setheading(90)
def down():
   if snake.heading()!=90:
      snake.shape("down.gif")
      snake.setheading(270)
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
while True:
    field.update()
    if snake.xcor()>290 or snake.ycor()>290 or snake.xcor()<-290 or snake.ycor()<-290 :
       field.bgpic("gameover.gif")
       snake.hideturtle()
       food.hideturtle()
    for i in segmant:
       if i.distance(snake)<10:
          field.bgpic("gameover.gif")
          snake.hideturtle()
          food.hideturtle()
    
    
    if snake.distance (food)<15 :
       x=random.randint(-280,280)
       y=random.randint(-280,280)
       food.goto(x,y)
       score=score+1
       result.clear()
       result.goto(0,300)
       result.write("score - {}".format(score),font=("Arial",8,"bold"))
       body=turtle.Turtle()
       body.shape("body.gif")
       body.penup()
       body.speed(500)
       segmant.append(body)
    for i in range(len(segmant)-1,0,-1):
       x=segmant[i-1].xcor()
       y=segmant[i-1].ycor()
       segmant[i].goto(x,y)

    if len(segmant)>0:
       x=snake.xcor()
       y=snake.ycor()
       segmant[0].goto(x,y) 
    
    move()
turtle.done()
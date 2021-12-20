import turtle
import time
import random
from playsound import playsound
import winsound

score=0
delay=0.1
high_score=0

#window screen
is_paused=False


#exit screen
def exitprogram():
    scn.bye()

def close():
    close = turtle.Turtle()
    close.speed(0)
    close.color("white")
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    scn.listen()
    scn.onkeypress(exitprogram, "Escape")
    #scn.onkeypress(close.clear())


#game over screen
def gameover():
    gm=turtle.Turtle()
    gm.speed(0)
    gm.color("RED")
    gm.penup()
    gm.hideturtle()
    gm.goto(0,0)
    gm.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
    time.sleep(2)
    scn.listen()
    scn.onkeypress(gm.clear())
    
def toggle_pause():
       global is_paused
       if is_paused==True:
           is_paused=False
       else:
           is_paused=True
           
             
    
scn=turtle.Screen()
scn.title("Snake Game")
scn.bgcolor("black")
scn.setup(width=600, height=600)
scn.tracer(0)
scn.onkeypress(close, "Escape")

#snake body

head=turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction= "stop"

# food 
food=turtle.Turtle()
food.speed(0)
colors = random.choice(['red', 'green', 'blue'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# screen detailing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-290, 280)
pen.write("Score: 0 High Score: 0", align="left", font=("Comic Sans MS", 10, "normal"))


# assigning key directions
def goUp():
    if head.direction != "down":
        head.direction = "up"
 
 
def goDown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goLeft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goRight():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
scn.listen()
scn.onkeypress(goUp, "w")
scn.onkeypress(goUp, 'Up')

scn.onkeypress(goDown, "s")
scn.onkeypress(goDown, 'Down')

scn.onkeypress(goLeft, "a")
scn.onkeypress(goLeft, 'Left')

scn.onkeypress(goRight, "d")
scn.onkeypress(goRight, 'Right')

#gameplay
segments=[]

while True:
	scn.update()
	if head.xcor() > 270 or head.xcor() < -270 or head.ycor() > 280 or head.ycor() < -280:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		color = random.choice(['red', 'blue', 'green'])
		shape = random.choice(['square', 'circle'])
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		winsound.PlaySound('lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
		delay = 0.1
  
		pen.clear()
  
		pen.write("Score: 0 High Score: 0", align="left", font=("Comic Sans MS", 10, "normal"))
		gameover()
		
        
	if head.distance(food) < 20:
		winsound.PlaySound("point.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("grey") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 1
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
			winsound.PlaySound('lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
			gameover()
			break
	        
	time.sleep(delay)

scn.mainlool()
        
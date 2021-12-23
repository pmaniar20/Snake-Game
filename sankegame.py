import turtle
import time
import random
import keyboard
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
    close=turtle.Turtle()
    close.speed(0)
    close.color("white")
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    #scn.listen()
    while True:
        try:
            if keyboard.is_pressed('Escape'):
               # close.write("Pressed esc key", align="center", font = ("Courier", 24, "normal"))
                exitprogram()
                break
        except:
            break
    
    #close.clear() 

#congratulations screen
def congratulations():
    cg=turtle.Turtle()
    cg.speed(0)
    cg.color("Yellow")
    cg.penup()
    cg.hideturtle()
    cg.goto(0,0)
    cg.write("CONGRATULATIONS", align="center", font=("Courier", 30, "normal"))
    time.sleep(2)
    #scn.listen()
    exitprogram()

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
    #scn.listen()
    scn.onkeypress(gm.clear())  
    
scn=turtle.Screen()
scn.title("Snake Game")
scn.bgcolor("black")
scn.setup(width=600, height=600)
scn.tracer(0)
scn.onkeypress(close, "Escape")


#draw grid lines
trtl=turtle.Turtle()
trtl.hideturtle()

def drawy(val):
	trtl.up()
	trtl.setpos(val,-290)
	trtl.down()
	trtl.forward(580)
	
def drawx(val):
	trtl.up()
	trtl.setpos(-290,val)
	trtl.down()
	trtl.forward(580)

# set turtle features
trtl.speed(100)
trtl.left(90)
trtl.color('grey')

# y lines
for i in range(-11, 13):
	drawy(25*(i)-12.5)
#drawy(25*(-11)-12.5)
#drawy(25*(12)-12.5)

# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(0,0)
trtl.down()

# x lines
for i in range(-11, 13):
	drawx(25*(i)-12.5)
#drawx(25*(-11)-12.5)
#drawx(25*(12)-12.5)


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
colors=random.choice(['red', 'green', 'blue'])
shapes='circle'
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# screen detailing
pen=turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-290, 280)
pen.write("Score: 0 High Score: 0", align="left", font=("Comic Sans MS", 10, "normal"))


# assigning key directions
def goUp():
    if head.direction!="down":
        head.direction="up"
 
 
def goDown():
    if head.direction!="up":
        head.direction="down"
 
 
def goLeft():
    if head.direction!="right":
        head.direction="left"
 
 
def goRight():
    if head.direction!="left":
        head.direction="right"
 
 
def move():
    time.sleep(0.1)
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+25)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-25)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-25)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+25)
 
 
scn.listen()
time.sleep(0.1)
scn.onkeypress(goUp, "w")
scn.onkeypress(goUp, "W")
scn.onkeypress(goUp, 'Up')

time.sleep(0.1)
scn.onkeypress(goDown, "s")
scn.onkeypress(goDown, "S")
scn.onkeypress(goDown, 'Down')

time.sleep(0.1)
scn.onkeypress(goLeft, "a")
scn.onkeypress(goLeft, "A")
scn.onkeypress(goLeft, 'Left')

time.sleep(0.1)
scn.onkeypress(goRight, "d")
scn.onkeypress(goRight, "D")
scn.onkeypress(goRight, 'Right')

#gameplay
segments=[]

while True:
	scn.update()
	if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		color=random.choice(['red', 'blue', 'green'])
		shape='circle'
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score=0
		winsound.PlaySound('lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
		#delay=0.1
		gameover()
		pen.clear()
		
		pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
		
		
        
	if head.distance(food)<25:
		winsound.PlaySound("point.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		x=random.randrange((-260//25), (260//25))*25
		y=random.randrange((-260//25), (260//25))*25

		i=0
		j=0
		f=0
		while i<=len(segments):
			if(j>10*len(segments)):
				f=1
				break
			if i==0:
				X=head.xcor()
				Y=head.ycor()
			else:
				X=segments[i-1].xcor()
				Y=segments[i-1].ycor()
			i=i+1
			if abs(X-x)<25 and abs(Y-y)<25:
				x=random.randrange((-260//25), (260//25))*25
				y=random.randrange((-260//25), (260//25))*25
				i=0
				j=j+1

		if j>len(segments) and f>0:
			score=0
			delay=0.1
			congratulations()
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
			winsound.PlaySound('lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
			
   
		food.goto(x, y)

		# Adding segment
		new_segment=turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("grey") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay-=0.001
		score+=1
		if score>high_score:
			high_score=score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x=segments[index-1].xcor()
		y=segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head)<25:
			time.sleep(1)
			head.goto(0, 0)
			head.direction="stop"
			colors=random.choice(['red', 'blue', 'green'])
			shapes='circle'
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()

			score=0
			delay=0.1
			gameover()
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Comic Sans MS", 10, "normal"))
			winsound.PlaySound('lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
			
			break
	        
	time.sleep(delay)

scn.mainlool()
        

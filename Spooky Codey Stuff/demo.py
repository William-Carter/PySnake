#Copyright William Carter 2018
import turtle, random, time, sys

#light, dark, gray
theme = "light"
wall_list = [
     (-50, -50), (-50, -40), (-50, -30), (-50, -20), (-50, -10),
     (-50, 0), (-50, 10), (-50, 20), (-50, 30), (-50, 40), (-50, 50),
     (-50, 60), (-50, 70), (-50, 80), (-50, 90), (-50, 100), (-50, 110),

     (110, -50), (110, -40), (110, -30), (110, -20), (110, -10),
     (110, 0), (110, 10), (110, 20), (110, 30), (110, 40), (110, 50),
     (110, 60), (110, 70), (110, 80), (110, 90), (110, 100), (110, 110),

     (-40, -50), (-30, -50), (-20, -50), (-10, -50), (0, -50),
     (10, -50), (20, -50), (30, -50), (40, -50), (50, -50), (60, -50),
     (70, -50), (80, -50), (90, -50), (100, -50),

     (-40, 110), (-30, 110), (-20, 110), (-10, 110), (0, 110),
     (10, 110), (20, 110), (30, 110), (40, 110), (50, 110), (60, 110),
     (70, 110), (80, 110), (90, 110), (100, 110)
]

cherryList = []

lineListY = [(-35, -50), (-25, -50), (-15, -50), (-5, -50), (5, -50), (15, -50),
            (25, -50), (35, -50), (45, -50), (55, -50), (65, -50), (75, -50),
            (85, -50), (95, -50)]

lineListX = [(110, -35), (110, -25), (110, -15), (110, -5), (110, 5), (110, 15),
            (110, 25), (110, 35), (110, 45), (110, 55), (110, 65), (110, 75),
            (110, 85), (110, 95)]




#defining the game window and it's properties
window = turtle.Screen()
window.title("PySnake 1.1")
if theme == "light":
    window.bgcolor("white")
elif theme == "dark":
    window.bgcolor("black")
elif theme == "gray":
    window.bgcolor("dark gray")
    
turtle.tracer(0, 0)

#defining the setup turtle
setup = turtle.Turtle()
setup.shape("square")
setup.turtlesize(0.45)
setup.speed(0)
setup.up()
if theme == "light":
    setup.color("black")
elif theme == "dark":
    setup.color("white")
elif theme == "gray":
    setup.color("light gray")

#defining the gridlines
line = turtle.Turtle()
line.color("gray")
for m in range(len(lineListY)):
    line.up()
    line.setpos(lineListY[m])
    line.down()
    line.seth(90)
    line.forward(160)

for n in range(len(lineListX)):
    line.up()
    line.setpos(lineListX[n])
    line.down()
    line.seth(180)
    line.forward(160)
line.hideturtle()

#making a function to draw onto the screen a wall_list array
def drawBoundary():
    global setup
    global wall_list
    setup.clearstamps()
    for i in range(len(wall_list)):
        setup.setpos(wall_list[i])
        setup.stamp()



#changing the theme during play for demo purposes
def changeTheme():
    global theme, snake, cherry, setup, window
    if theme == "light":
        theme = "dark"
    elif theme == "dark":
        theme = "gray"
    elif theme == "gray":
        theme = "light"


    if theme == "light":
        setup.color("black")
        snake.color("dark green")
        cherry.color("red")
        window.bgcolor("white")
    elif theme == "dark":
        setup.color("white")
        snake.color("orange")
        cherry.color("light blue")
        window.bgcolor("black")
    elif theme == "gray":
        setup.color("light gray")
        snake.color("gray")
        cherry.color("white")
        window.bgcolor("dark gray")

    drawBoundary()
    drawSnake()
    turtle.update()
    
    
    

    
#drawing the wall_list
drawBoundary()
setup.hideturtle()

#updating the screen to give the player a sense of where they will be playing
turtle.update()



#draws the body of the snake
def drawSnake():
    snake.clearstamps()
    returnpos = snake.pos()
    for j in range(len(stampList)):
        snake.setpos(stampList[j])
        snake.stamp()
    snake.setpos(returnpos)
    
#wipes all stamps, removes the oldest stamp and then replaces all those remaining
def removeLastStamp():
    global stampList
    global snake
    global turtle
    stampList.pop(0)
    drawSnake()
    
receive = 0

#debug function for testing the snake's behaviour at high lengths
#commented out bind to P in the control array
def placeCherry():
    global receive
    receive = 1

#defining cherry
cherry = turtle.Turtle()
cherry.shape("square")
cherry.turtlesize(0.45)
cherry.up()
if theme == "light":
    cherry.color("red")
elif theme == "dark":
    cherry.color("light blue")

elif theme == "gray":
    cherry.color("white")
#spawning in the cherry
def spawnCherry():
    global cherry
    global stampList
    meme = True
    lis = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    while meme:
        spot1 = int(random.choice(lis))
        spot2 = int(random.choice(lis))
        cherry.setpos(spot1, spot2)
        if not cherry.pos() in stampList:
            cherryList.append(cherry.pos())
            cherry.stamp()
            meme = False
            
#custom function to stamp the snake and add it to the stamp list
def stampify(var):
    var.stamp()
    stampList.append((round(var.xcor(),2),round(var.ycor(),2)))

stampList = []


#defining the snake
snake = turtle.Turtle()
snake.seth(270)
snake.up()
if theme == "light":
    snake.color("dark green")
elif theme == "dark":
    snake.color("orange")

elif theme == "gray":
    snake.color("gray")
snake.shape("square")
snake.turtlesize(0.45)
snake.setpos(0, 50)
stampify(snake)
snake.setpos(0, 40)
stampify(snake)
count = 0
#making the functions for moving the snake
def snakeleft():
    global snake, counter555, count
    if not snake.heading() == 0 and count != counter555:
        snake.seth(180)
        count = counter555
        
def snakeright():
    global snake, counter555, count
    if not snake.heading() == 180 and count != counter555:
       snake.seth(0)
       count = counter555
       
def snakeup():
    global snake, counter555, count
    if not snake.heading() == 270 and count != counter555:
       snake.seth(90)
       count = counter555
       
def snakedown():
    global snake, counter555, count
    if not snake.heading() == 90 and count != counter555:
        snake.seth(270)
        count = counter555

#unnecessary function that could easily have been raw code because it's only
#referenced once in the entire script
def cherryThisTurn():
    global receive
    if receive == 1:
        receive = 0
        return True
    if receive == 0:
        return False


#main collision detection function
def check():
    global wall_list
    global snake
    global receive
    if snake.pos() in wall_list:
        print("\nGame Over")
        print(score)
        sys.exit()
    if snake.pos() in stampList:
        print("\nGame Over")
        print(score)
        sys.exit()
    if snake.pos() in cherryList:
        receive = 1

        
#control array  
window.onkeypress(snakeup, "w")
window.onkeypress(snakedown, "s")
window.onkeypress(snakeright, "d")
window.onkeypress(snakeleft, "a")
window.onkeypress(sys.exit, "q")
window.onkeypress(changeTheme, "m")
#window.onkeypress(placeCherry, "p")#

window.listen()


#final setup for main loop
spawnCherry()
counter555 = 0
score = 0

time.sleep(2)

#loop that uses previously defined functions to run the game
while True:

    turtle.update()
    snake.forward(10)
    counter555 += 1
    time.sleep(0.09)
    snake.setpos(round(snake.xcor(),2),round(snake.ycor(),2))
    check()
    if not cherryThisTurn():
        removeLastStamp()
        stampify(snake)
    else:
        stampify(snake)
        cherry.clearstamps()
        cherryList = []
        spawnCherry()
        score += 1
        



    




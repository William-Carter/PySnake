# Copyright William Carter 2019
import turtle
import random
import time
import sys
import os
import themeList
canToggleSettings = True
opSystem = sys.platform
devmode = False

# Error handling cause god knows we need it


def bigFatError(inp):
    turtle.clearscreen()
    errorReport = turtle.Turtle()
    errorReport.hideturtle()
    errorReport.up()

    time.sleep(0.3)
    errorReport.write("Uh oh, someone did a fucky wucky\n"+inp, font=("Arial", 25, "normal"), align="center")
    quit()

# Checking for developer mode


if len(sys.argv) > 1:
    if sys.argv[1] == "-devmode":
        devmode = True
    else:
        bigFatError("Error 745: Unknown argument")
        sys.exit()

# Version display function
pysnakeVersion = (2, 3, 0)


def returnVersion(precision):
    global pysnakeVersion
    if precision > len(pysnakeVersion):
        return("If you're seeing this, William is a dickwad")
        bigFatError("Error 652: Version index out of range")

    else:
        empty = ""
        for i in range(precision-1):
            empty = empty+str(pysnakeVersion[i])
            empty = empty+"."
        empty = empty+str(pysnakeVersion[precision-1])
        return empty

# Variable setup

globalSnakeTiming = 0.1
globalSnakeMove = 10

# Defining locations


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

lineListY = [(-35, -50), (-25, -50), (-15, -50), (-5, -50), (5, -50), (15, -50),
            (25, -50), (35, -50), (45, -50), (55, -50), (65, -50), (75, -50),
            (85, -50), (95, -50)]

lineListX = [(110, -35), (110, -25), (110, -15), (110, -5), (110, 5), (110, 15),
            (110, 25), (110, 35), (110, 45), (110, 55), (110, 65), (110, 75),
            (110, 85), (110, 95), (110, 105)]

# Initial theme setup
dir_path = os.path.dirname(os.path.realpath(__file__))
if sys.platform == "linux" or "darwin":
    f = open(dir_path+"/theme.txt", "r+")
elif sys.platform == "win32" or "cygwin":
    f = open(dir_path+"\\theme.txt", "r")

theme = f.read()
f.close()
print(theme)
rng_seed = 0

# Global turtle setup
window = turtle.Screen()

titleString = "PySnake"
if devmode:
    titleString = "[Dev]Pysnake"
window.title((titleString,returnVersion(3)))
turtle.tracer(0, 0)

# Setup turtles
setup = turtle.Turtle()
setup.hideturtle()
setup.up()
setup.shape("square")
setup.turtlesize(0.45)
setup.speed(0)
line = turtle.Turtle()
line.color("gray")

# Function for drawing gridlines


def drawLines():
    global line
    line.clear()
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


drawLines()
line.hideturtle()

# Draws walls


def drawBoundary():
    global setup
    global wall_list
    setup.clearstamps()
    for i in range(len(wall_list)):
        setup.setpos(wall_list[i])
        setup.stamp()

# Changes theme


def changeTheme():
    global theme
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if sys.platform == "linux" or "darwin":
        f = open(dir_path+"/theme.txt", "w")
    elif sys.platform == "win32" or "cygwin":
        f = open(dir_path+"\\theme.txt", "w")

    currentVal = themeList.themeIndex.index(theme)
    if not currentVal + 1 == len(themeList.themeIndex):
        themeIn = themeList.themeIndex[currentVal+1]
    else:
        themeIn = themeList.themeIndex[0]
        print(themeList.themeIndex[0])
    f.write(themeIn)
    f.close()
    setTheme(themeIn)
# Function to change theme while settings is open


def settingsTheme():
    changeTheme()
    settingsBoi.clear()
    settingsBoi.setpos(-200, 100)
    settingsBoi.write("1. Theme: "+theme, font=("Arial", 25, "normal"), align="left")

# Directly sets theme


def setTheme(thame):
    global theme, snake, cherry, setup, window, drawturt, settingsOpen
    theme = thame
    setup.color(themeList.themes[thame]["setup"])
    snake.color(themeList.themes[thame]["snake"])
    cherry.color(themeList.themes[thame]["cherry"])
    window.bgcolor(themeList.themes[thame]["background"])
    drawturt.color(themeList.themes[thame]["text"])
    highscore.color(themeList.themes[thame]["highscore"])
    line.color(themeList.themes[thame]["line"])
    settingsBoi.color(themeList.themes[thame]["settings"])

    scoreify(score)
    drawHighScore()
    if not settingsOpen:
        drawLines()

        drawSnake()
        drawBoundary()

    turtle.update()

    if settingsOpen:
        setup.setpos(0, 200)
        setup.write("Settings", font=("Arial", 32, "normal"), align="center")
        setup.setpos(0, -250)
        setup.write("Press H to return", font=("Arial", 32, "normal"), align="center")


drawBoundary()


def drawSnake():
    snake.clearstamps()
    returnpos = snake.pos()
    for j in range(len(stampList)):
        snake.setpos(stampList[j])
        snake.stamp()
    snake.setpos(returnpos)


def removeLastStamp():
    global stampList
    global snake
    global turtle
    stampList.pop(0)
    drawSnake()


receive = 0


def placeCherry():
    global receive
    receive = 1


cherry = turtle.Turtle()
cherry.shape("square")
cherry.turtlesize(0.45)
cherry.up()


def spawnCherry():
    global cherry
    global stampList
    global rng_seed
    meme = True
    listNeg = [-40, -30, -20, -10, 0, 10, 20, 30]
    listPos = [30, 40, 50, 60, 70, 80, 90, 100]
    while meme:
        global rng_seed
        if rng_seed == 0:
            spot1 = int(random.choice(listNeg))
            spot2 = int(random.choice(listPos))

        elif rng_seed == 1:
            spot1 = int(random.choice(listNeg))
            spot2 = int(random.choice(listNeg))

        elif rng_seed == 2:
            spot1 = int(random.choice(listPos))
            spot2 = int(random.choice(listPos))

        elif rng_seed == 3:
            spot1 = int(random.choice(listPos))
            spot2 = int(random.choice(listNeg))

        cherry.setpos(spot1, spot2)
        if not cherry.pos() in stampList:
            cherryList.append(cherry.pos())
            cherry.stamp()
            meme = False


def stampify(var):
    var.stamp()
    stampList.append((round(var.xcor(), 2), round(var.ycor(), 2)))


stampList = []


# defining the snake
snake = turtle.Turtle()
snake.seth(270)
snake.up()
snake.shape("square")
snake.turtlesize(0.45)
snake.setpos(30, 50)
stampify(snake)
snake.setpos(30, 40)
stampify(snake)
count = 0

settingsOpen = False

settingsBoi = turtle.Turtle()
settingsBoi.speed(0)
settingsBoi.hideturtle()
settingsBoi.up()


def openSettings():
    global settingsOpen, canToggleSettings
    if canToggleSettings:
        canToggleSettings = False
        stopDemo()
        line.clear()
        window.onkeypress(None, "space")
        window.onkeypress(startDemo, "h")
        settingsOpen = True
        setup.clear()
        setup.setpos(0, 200)
        setup.write("Settings", font=("Arial", 32, "normal"), align="center")
        setup.setpos(0, -250)
        setup.write("Press H to return", font=("Arial", 32, "normal"), align="center")
        snake.clearstamps()
        cherry.clearstamps()
        snake.hideturtle()
        cherry.hideturtle()
        settingsBoi.setpos(-200, 100)
        window.onkeypress(settingsTheme, "1")
        settingsBoi.write("1. Theme: "+theme, font=("Arial", 25, "normal"), align="left")
        turtle.update()


rng_seed = 0


def snakeleft():
    global snake, counter555, count, rng_seed
    rng_seed = 0
    if not snake.heading() == 0 and count != counter555:
        snake.seth(180)
        count = counter555


def snakeright():
    global snake, counter555, count, rng_seed
    rng_seed = 1
    if not snake.heading() == 180 and count != counter555:
        snake.seth(0)
        count = counter555


def snakeup():
    global snake, counter555, count, rng_seed
    rng_seed = 2
    if not snake.heading() == 270 and count != counter555:
        snake.seth(90)
        count = counter555


def snakedown():
    global snake, counter555, count, rng_seed
    rng_seed = 3
    if not snake.heading() == 90 and count != counter555:
        snake.seth(270)
        count = counter555


def cherryThisTurn():
    global receive
    if receive == 1:
        receive = 0
        return True
    if receive == 0:
        return False


high_score = 0
score = 0


def check():
    global wall_list
    global snake
    global receive
    global score
    global enableNoClip
    if not enableNoClip:
        if snake.pos() in wall_list:
            gameover()

            reset()
            score = 0
        if snake.pos() in stampList:
            gameover()

            reset()
            score = 0

    if snake.pos() in cherryList:
        receive = 1


demo = True


def stopDemo():
    global demo
    demo = False
    window.onkeypress(None, "h")
    window.onkeypress(None, "space")


drawturt = turtle.Turtle()
drawturt.hideturtle()
drawturt.up()


def instaCherry():
    global receive
    receive = 1


def gameover():
    drawturt.setpos(0, 200)
    drawturt.write("Game Over", font=("Arial", 64, "normal"), align="center")
    drawturt.setpos(0, 150)
    drawturt.write("You Scored "+str(score)+" points", font=("Arial", 32, "normal"), align="center")
    time.sleep(1)
    drawturt.clear()


def startGame():
    global demo, noStart
    demo = False
    noStart = False


window.onkeypress(startGame, "space")
window.onkeypress(openSettings, "h")

window.listen()


def startDemo():
    global demo, noStart, settingsOpen, canToggleSettings, demoCounter
    if canToggleSettings:
        demo = True
        noStart = True
        settingsOpen = False
        snake.showturtle()
        cherry.showturtle()
        window.onkeypress(startGame, "space")
        window.onkeypress(openSettings, "h")
        window.onkeypress(None, "1")
        window.listen()
        setup.clear()
        setup.setpos(0, 200)

        settingsBoi.clear()

        setup.write("PySnake "+returnVersion(2), font=("Arial", 64, "normal"), align="center")
        setup.setpos(0, -250)
        setup.write("Press Space to Start", font=("Arial", 32, "normal"), align="center")
        setup.setpos(0, -300)
        setup.write("Press H for Settings", font=("Arial", 24, "normal"), align="center")

        drawBoundary()
        setTheme(theme)
        canToggleSettings = False
        demoCounter = 0
        turtle.update()


def customCherry(x, y):
    global cherry
    cherry.setpos(x, y)
    cherry.stamp()


def demoCheck():
    global wall_list
    global snake
    global receive
    if snake.pos() in wall_list:
        resetDemo()
    if snake.pos() in stampList:
        resetDemo()

    if snake.pos() in cherryList:
        receive = 1


def reset():
    global high_score, cherryList
    cherry.clearstamps()
    global snake
    global stampList
    stampList = []
    snake.clearstamps()
    snake.setpos(30, 50)
    stampify(snake)
    snake.setpos(30, 40)
    stampify(snake)
    snake.setpos(30, 30)
    snake.seth(270)
    cherry.clearstamps()
    cherryList = []
    if score > high_score:
        if score > 400:
            print("cheater")

        if not devmode:
            high_score = score
            newHighScore()

    time.sleep(0.5)

    drawHighScore()

    spawnCherry()


def resetDemo():
    global high_score, cherryList
    cherry.clearstamps()
    global snake
    global stampList
    stampList = []
    snake.clearstamps()
    snake.setpos(30, 50)
    stampify(snake)
    snake.setpos(30, 40)
    stampify(snake)
    snake.setpos(30, 30)
    time.sleep(0.0)
    snake.seth(270)
    cherry.clearstamps()
    cherryList = []
    spawnCherry()


highscore = turtle.Turtle()
highscore.hideturtle()
highscore.up()


def newHighScore():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path+"/highscore.txt", "w")
    f.write("#If you're going to cheat, at least bloody modify the code to do it. Don't be lazy.\n")
    f.write(str(high_score))
    f.close()


def drawHighScore():
    global high_score
    highscore.setpos(-290, 200)
    highscore.clear()
    highscore.write(high_score, font=("Arial", 40, "normal"), align="center")


def scoreify(x):
    global drawturt
    drawturt.clear()
    drawturt.setpos(290, 200)
    drawturt.write(x, font=("Arial", 40, "normal"), align="center")


cherryList = []
spawnCherry()
counter555 = 0
movecount = 0
setTheme(theme)
startDemo()
noStart = True
demoCounter = 0
canToggleSettings = False
while noStart:
    canToggleSettings = True

    turtle.update()
    if demo:
        movecount += 1

        snake.forward(globalSnakeMove)
        counter555 += 1
        time.sleep(globalSnakeTiming)
        snake.setpos(round(snake.xcor(), 2), round(snake.ycor(), 2))
        if movecount == 2:
            movecount = 0
            thiccchic = ["up", "down", "left", "right"]
            rand = random.choice(thiccchic)
            if rand == "up":
                snakeup()
            if rand == "down":
                snakedown()
            if rand == "left":
                snakeleft()
            if rand == "right":
                snakeright()

        demoCheck()
        if not cherryThisTurn():
            removeLastStamp()
            stampify(snake)
        else:
            stampify(snake)
            cherry.clearstamps()
            cherryList = []
            spawnCherry()

    if demoCounter < 5:
        demoCounter += 1

    elif demoCounter == 5:
        canToggleSettings = True


resetDemo()
setup.clear()
drawBoundary()
snake.clear()
reset()
demo = False

window.onkeypress(snakeup, "w")
window.onkeypress(snakedown, "s")
window.onkeypress(snakeright, "d")
window.onkeypress(snakeleft, "a")


window.onkeypress(None, "h")
window.onkeypress(None, "1")
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+"/highscore.txt", "r")
high_score = int(file.readlines()[1])
file.close()
score = 0
snake.seth(270)
drawHighScore()
enableNoClip = False


def noClip():
    global enableNoClip
    if not enableNoClip:
        enableNoClip = True
    elif enableNoClip:
        enableNoClip = False


if devmode:
    window.onkeypress(changeTheme, "m")
    window.onkeypress(noClip, "p")
    window.onkeypress(instaCherry, "c")


window.listen()
while True:
    scoreify(score)
    turtle.update()
    snake.forward(globalSnakeMove)
    counter555 += 1
    time.sleep(globalSnakeTiming)
    snake.setpos(round(snake.xcor(), 0), round(snake.ycor(),  0))
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

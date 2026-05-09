import turtle as t
import random
t.setup(410, 400)
t.pendown()
t.tracer(0, 0)
t.hideturtle()
t.bgcolor("black")
t.pencolor("white")
t.title("breakout")

gameon=0
bx=0
by=100
vx=10
vy=10
vxi=1
vyi=1
px=0
py=-150
level=0
bricks=[]
for u in range(4):
    for i in range(5):
        bricks.append({
            "x":-150+i*60,
            "y":180-u*30,
            "broken":0
        })

def ball():
    global bx, by, vx, vy, vyi, vxi
    
    bx = bx + (vx * vxi)
    by = by + (vy * vyi)
    
    # Wall bounces — push ball INSIDE the boundary
    if bx >= 190:
        vxi = -vxi
        bx = 189  # Force ball just inside the right wall
        vx = abs(vy) - random.randint(1, abs(vy))
        vy = 10 - vx
    if bx <= -190:
        vxi = -vxi
        bx = -189  # Force ball just inside the left wall
        vx = abs(vy) - random.randint(1, abs(vy))
        vy = 10 - vx
    if by >= 190:
        vyi = -vyi
        by = 189  # Force ball just below the top wall
        vx = abs(vy) - random.randint(1, abs(vy))
        vy = 10 - vx
    if by <= -190:
        reset()
        
    # Paddle collision
    if vyi == -1:
        if by - 10 <= py + 10 and by - 10 >= py - 5:
            if px - 5 <= bx <= px + 45:
                vyi = -vyi
                by = py + 20  # Well above the paddle
                vx = abs(vy) - random.randint(1, abs(vy))
                vy = 10 - vx
                
    # Brick collisions — also push ball away from brick
    for i in bricks:
        if i["broken"] != 1:
            if i["x"] - 5 <= bx <= i["x"] + 45:
                # Ball hitting from below the brick
                if by - 10 <= i["y"] + 10 and by - 10 >= i["y"]:
                    vyi = -vyi
                    by = i["y"] + 20  # Push above the brick
                    vx = abs(vy) - random.randint(1, abs(vy))
                    vy = 10 - vx
                    i["broken"] = 1
                # Ball hitting from above the brick
                elif by + 10 >= i["y"] and by + 10 <= i["y"] + 10:
                    vyi = -vyi
                    by = i["y"] - 20  # Push below the brick
                    vx = abs(vy) - random.randint(1, abs(vy))
                    vy = 10 - vx
                    i["broken"] = 1
    
    # Draw ball
    t.penup()
    t.goto(bx, by)
    t.pendown()
    t.circle(10)
    t.penup()
    

def brickslist():
    global bricks, level, bx, by, px, py
    c=0
    bc=0
    for i in bricks:
        c+= 1
        if i["broken"] != 1:
            t.goto(i["x"],i["y"])
            t.pendown()
            t.goto(i["x"],i["y"])
            t.goto(i["x"]+40,i["y"])
            t.goto(i["x"]+40,i["y"]+10)
            t.goto(i["x"],i["y"]+10)
            t.goto(i["x"],i["y"])
            t.penup()
        elif i["broken"]==1:
            bc+=1
    if c==bc:
        level+=1
        reset()
def reset():
    global bricks, level, bx, by, px, py, vx, vy, vxi, vyi

    bricks=[]
    for u in range(4+level):
        for i in range(5):
            bricks.append({
                "x":-150+i*60,
                "y":180-u*30,
                "broken":0
            })
    bx=0
    by=100
    px=0
    py=-150
    vx=10
    vy=10
    vxi=1
    vyi=1

def paddle():
    t.goto(px,py)
    t.pendown()
    t.goto(px,py)
    t.goto(px+40,py)
    t.goto(px+40,py+10)
    t.goto(px,py+10)
    t.goto(px,py)
    t.penup()
    
    t.goto(200,200)
    t.pendown()
    t.goto(200,200)
    t.goto(200,-200)
    t.goto(-200,-200)
    t.goto(-200,200)
    t.goto(200,200)
    t.penup()

mv= 0

def right():
    global px
    if mv==1:
        if 1==1:
            if px <=200:
                px+=10
        
def left():
    global px
    if mv == -1:
        if px >=-200:
            px-=10
        
def sr():
    global mv
    mv=1
def rs():
    global mv
    mv=0
def sl():
    global mv
    mv=-1
def ls():
    global mv
    mv=0
def click(x,y):
    global gameon
    if gameon==0:
        gameon=1
    else:
        global px
        if 0 < x and px <= 200:
            px+=40
        elif x < 0 and px >= -200:
            px-=40
def menu():
    global gameon
    t.goto(0, 0)
    t.write("BREAKOUT \n press space to start")
def start():
    global gameon
    if gameon ==0:
        gameon=1
    else:
        gameon=0
t.onkeypress(sr, "d") 
t.onkeyrelease(rs, "d")
t.onkeypress(sl, "a") 
t.onkeyrelease(ls, "a")
t.onkeypress(sr, "Right") 
t.onkeyrelease(rs, "Right")
t.onkeypress(sl, "Left") 
t.onkeyrelease(ls, "Left")
t.onkey(start, "space")
t.onscreenclick(click)
t.listen()
def mainloop():
    if gameon==1:
        t.clear()
        right()
        left()
        ball()
        paddle()
        brickslist()
        t.update()
        t.ontimer(mainloop,50)
    else:
        t.clear()
        menu()
        t.update()
        t.ontimer(mainloop,50)
mainloop()
t.mainloop()

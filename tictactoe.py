import turtle

t = turtle.Turtle()
def drawLine(x, y):
    t.hideturtle()
    t.speed(10000)
    if x>=0:
        t.setheading(90)
    elif y<0:
        t.setheading(0)
    else:
        t.penup()
        t.goto(-75,175)
        t.pendown()
        t.setheading(0)
    t.forward(250)
    t.backward(250)
    t.penup()
    if x>=0:
        t.setheading(0)
    else:
        t.setheading(270)
    t.forward(100)
    
    if x>=0:
        t.setheading(270)
    else:
        t.setheading(90)
    t.pendown()

drawLine(50, 100)
drawLine(50, 100)

drawLine(-50,100)
drawLine(-50,-100)

click = 0
a, b, c, d, e, f, g, h, i = [0]*9

def goto(x, y):
    global click, a, b, c, d, e, f, g, h, i
    
    print('Moving to {}, {}'.format(x,y))

    if -82<x<175 and -3<y<255:
        turtle.goto(x, y-50)
        if 0<x<100 and 75<y<175:
            if a == 1:
                pass
            elif click%2 == 0:
                turtle.goto(50, 75)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                a = 1
                
            else:
                turtle.goto(50, 75)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                a = 1
                

        if 0<x<100 and 0<y<75:
            if b == 1:
                pass
            elif click%2 == 0:
                turtle.goto(50, -25)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                b = 1
                
            else:
                turtle.goto(50, -25)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                b = 1
                

        if 0<x<100 and 175<y<255:
            if c == 1:
                pass
            elif click%2 == 0:
                turtle.goto(50, 175)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                c = 1
                
            else:
                turtle.goto(50, 175)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                c = 1
                

        if -100<x<0 and 175<y<255:
            if d == 1:
                pass
            elif click%2 == 0:
                turtle.goto(-50, 175)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                d = 1
                
            else:
                turtle.goto(-50, 175)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                d = 1
                

        if -100<x<0 and 75<y<155:
            if e == 1:
                pass
            elif click%2 == 0:
                turtle.goto(-50, 75)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                e = 1
                
            else:
                turtle.goto(-50, 75)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                e = 1
                

        if -100<x<0 and -25<y<55:
            if f == 1:
                pass
            elif click%2 == 0:
                turtle.goto(-50, -25)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                f = 1
                
            else:
                turtle.goto(-50, -25)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                f = 1
                

        if 100<x<200 and 75<y<175:
            if g == 1:
                pass
            elif click%2 == 0:
                turtle.goto(150, 75)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                g = 1
                
            else:
                turtle.goto(150, 75)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                g = 1
                

        if 100<x<200 and 175<y<275:
            if h == 1:
                pass
            elif click%2 == 0:
                turtle.goto(150, 175)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                h = 1
                
            else:
                turtle.goto(150, 175)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                h = 1
                

        if 100<x<200 and -25<y<75:
            if i == 1:
                pass
            
            elif click%2 == 0:
                turtle.goto(150, -25)
                turtle.write("X", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                i =1
                
            else:
                turtle.goto(150, -25)
                turtle.write("O", font = ('Arial', 64, 'normal'), align = 'center')
                click += 1
                i = 1
                

turtle.penup()
turtle.hideturtle()
turtle.onscreenclick(goto)


    


    
    

    
    
    
    


import turtle

count = 0
cheak = 0
y = 0

while(cheak < 25):
    turtle.forward(100)
    turtle.left(90)
    count = count + 1
    if(count%4 ==0):
        cheak = cheak + 1
        turtle.penup()
        if(cheak%5 == 0):
            y = y+100
        turtle.goto((cheak%5)*100, y)
        turtle.pendown()

turtle.penup()
turtle.home()
turtle.exitonclick()

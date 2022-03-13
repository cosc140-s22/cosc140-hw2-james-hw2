#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle 


def main():
    ninja = turtle.Turtle()
    s = ninja.getscreen()
    s.title("The Cardiff Wizard")
    s.setworldcoordinates(0, 0, 400, 400)
    s.bgcolor("royal blue")
    ninja.speed(100)

    ninja.pencolor("green")
    ninja.forward(40)

    ninja.pencolor("black")
    ninja.fillcolor("grey")
    ninja.begin_fill()

    ninja.left(90)
    ninja.forward(20)

    for i in range(11):
        ninja.right(90)
        ninja.forward(40)
        ninja.right(90)
        ninja.forward(20)
        ninja.right(90)
        ninja.forward(40)
        ninja.right(90)
        ninja.forward(40)
    ninja.end_fill()

    ninja.begin_fill()
    ninja.forward(10)
    ninja.right(90)
    ninja.forward(15)
    ninja.right(90)
    ninja.forward(30)
    ninja.right(90)
    ninja.forward(10)
    ninja.left(180)
    ninja.forward(10)
    ninja.end_fill()
    ninja.forward(30)

    ninja.pencolor("brown")
    ninja.forward(120)
    ninja.left(90)

    ninja.fillcolor("gold")
    ninja.begin_fill()
    ninja.pencolor("gold")
    for i in range(2):
        ninja.forward(125)
        ninja.right(90)
        ninja.forward(5)
        ninja.right(90)
    ninja.forward(125)
    ninja.left(90)
    ninja.end_fill()

    ninja.fillcolor("red")
    ninja.pencolor("green")

    ninja.begin_fill()
    ninja.forward(40)
    ninja.left(90)
    ninja.forward(20)
    ninja.left(90)
    ninja.forward(40)
    ninja.left(90)
    ninja.forward(20) 
    ninja.end_fill()

    ninja.penup()
    ninja.right(90)
    ninja.forward(5)
    ninja.right(90)
    ninja.forward(125)
    ninja.left(90)
    ninja.pendown()

    ninja.pencolor("brown")
    ninja.forward(120)



    ninja.fillcolor("brown")
    ninja.pencolor("brown")
    ninja.begin_fill()
    for i in range(2):
        ninja.right(90)
        ninja.forward(15)
        ninja.right(90)
        ninja.forward(250)
    ninja.end_fill()
    ninja.fillcolor("grey")
    ninja.pencolor("black")
    for i in range(11):
        ninja.begin_fill()
        ninja.forward(40)
        ninja.right(90)
        ninja.forward(20)
        ninja.right(90)
        ninja.forward(40)
        ninja.right(90)
        ninja.forward(20)
        ninja.end_fill()
        ninja.right(180)
        ninja.forward(20)
        ninja.left(90)
        ninja.end_fill()
    ninja.fillcolor("saddle brown")
    ninja.begin_fill()
    ninja.left(180)
    ninja.forward(250)
    ninja.right(90)
    ninja.forward(205)
    ninja.right(90)
    ninja.forward(250)
    ninja.right(90)
    ninja.forward(205)
    ninja.end_fill()


    ninja.right(180)
    ninja.forward(220)
    ninja.right(90)
    ninja.forward(25)
    ninja.pencolor("black")
    ninja.fillcolor("grey")
    ninja.begin_fill()
    ninja.left(90)
    ninja.forward(30)
    ninja.right(90)
    ninja.forward(15)
    ninja.right(90)
    ninja.forward(30)
    ninja.right(90)
    ninja.forward(15)
    ninja.end_fill()
    ninja.forward(300)
    ninja.right(90)
    ninja.begin_fill()
    ninja.forward(30)
    ninja.left(90)
    ninja.forward(15)
    ninja.left(90)
    ninja.forward(30)
    ninja.left(90)
    ninja.forward(15)
    ninja.end_fill()
    ninja.forward(155)
    ninja.right(90)
    ninja.penup()
    ninja.forward(220)
    ninja.pendown()



    ninja.right(270)
    colors = ["red", "blue", "green", "gray", "orange", "black"]

    for i in range(70, 0, -4):
        ninja.fillcolor(colors[i%6])
        ninja.begin_fill()
        ninja.circle(i)
        ninja.end_fill()

    ninja.penup()
    ninja.left(90)
    ninja.forward(70)
    ninja.pendown()

    ninja.right(90)
    ninja.fillcolor("tan")
    ninja.begin_fill()
    ninja.circle(10)
    ninja.end_fill()

    ninja.penup()
    ninja.left(90)
    ninja.forward(20)
    ninja.pendown()

    ninja.fillcolor("purple")
    ninja.begin_fill()
    ninja.right(90)
    ninja.forward(10)
    ninja.left(120)
    ninja.forward(20)
    ninja.left(120)
    ninja.forward(20)
    ninja.end_fill()
    ninja.left(120)
    ninja.forward(10)
    ninja.right(90)

    ninja.penup()
    ninja.forward(10)
    ninja.left(90)

    ninja.forward(3)

    ninja.pendown()
    ninja.forward(2)
    ninja.penup()



    ninja.left(180)
    ninja.forward(8)

    ninja.pendown()
    ninja.forward(2)
    ninja.penup()

    ninja.right(180)
    ninja.forward(5)
    ninja.right(90)

    ninja.forward(5)
    ninja.pendown()

    ninja.left(90)
    ninja.forward(5)
    ninja.left(180)
    ninja.forward(10)
    ninja.right(180)
    ninja.forward(5)
    ninja.right(90)

    ninja.penup()
    ninja.forward(5)
    ninja.pendown()
    ninja.begin_fill()
    ninja.right(35)
    ninja.forward(50)
    ninja.left(125)
    ninja.forward(60)
    ninja.left(130)
    ninja.forward(55)
    ninja.end_fill()
    turtle.done()


if __name__ == "__main__":
    main()
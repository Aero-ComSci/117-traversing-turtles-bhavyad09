import turtle as trtl
import random

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtleCols = ["red", "blue", "green", "orange", "purple", "gold"]

class Turtle117:
    def __init__(self, shapes, colors):

        self.turtles = [trtl.Turtle(shape=s) for s in shapes]
        self.colors = colors

        for turtle in self.turtles:
            turtle.color(random.choice(self.colors))

        self.x = 0
        self.y = 0

    def moveTurtle(self):

        i = 0
        for turtle in self.turtles:
        
            turtle.goto(self.x + (i * 50), self.y + (i * 50))
            turtle.right(45)
            turtle.forward(50)

            if i == 4:
                break

            i += 1

    def spiral(self):

        direction = 50
        inc = 20  
        forwardDis = 100  
        
        i = 0
        for turtle in self.turtles:
            
            turtle.penup()
            turtle.setheading(direction)
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(forwardDis)

            forwardDis += inc
            direction += 45

            self.x, self.y = turtle.pos()
            if i == 15:
                break

            i += 1

    def shape(self):

        direction = 50
        i = 0
        for turtle in self.turtles:

            turtle.penup()
            turtle.setheading(direction)
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(100)
            direction += 45
            self.x, self.y = turtle.pos()

            i += 1
  

    def drawwHeadings(self, headings):

        i = 0
        for turtle in self.turtles:

            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.setheading(headings[i % len(headings)])
            turtle.forward(100)

            if i == 10:
                break

            i += 1

    def drawwPenSizes(self, pen_sizes):

        i = 0
        for turtle in self.turtles:
        
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.pensize(pen_sizes[i % len(pen_sizes)])
            turtle.forward(100)

            if i == 10:
                break

            i += 1

    def drawwLengths(self, lengths):

        i = 0
        for turtle in self.turtles:
        
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(lengths[i % len(lengths)])

            if i == 10:
                break

            i += 1

    def __str__(self):

        return "\n".join([f"Turtle Shape: {t.shape()}, Color: {t.color()[0]}" for t in self.turtles])

drawTool = Turtle117(turtleShapes, turtleCols)
print(drawTool)

wn = trtl.Screen()
#drawTool.moveTurtle()
#drawTool.shape()
#drawTool.spiral()
#drawTool.drawwLengths([50, 100, 150, 200, 250, 300])
#drawTool.drawwHeadings([0, 50, 100, 150])
#drawTool.drawwPenSizes([1, 2, 3, 4, 5, 6])
wn.mainloop()

from Turtle import *

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
for i in range(4):
  forward(100)
  right(90)

#BEGIN EXERCISE 1

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
for i in range(3):
  forward(100)
  right(120)

#END EXERCISE 1

#BEGIN EXERCISE 2

def draw_triangle(side_length):
  right(120)
  for i in range(3):
    forward(side_length)
    right(120)

#END EXERCISE 2

#BEGIN EXERCISE 3

initializeTurtle()
a = 300
b = 300
l = 100
speed(13)
penup()
goto(a,b)
pendown()
draw_triangle(l)
penup()
goto(a + l/2, 300)
pendown()
right(-90)
draw_triangle(l/2)

#END EXERCISE 3

#BEGIN EXERCISE 4

def sierpinski(start_length, min_length):
  assert min_length > 0, "min_length must be positive"
  if start_length < min_length:
    return
  else:
    for i in range(3):
      new_length = start_length / 2
      draw_triangle(new_length)
      sierpinski(new_length, min_length)
      forward(start_length)
      right(120)

#END EXERCISE 4

#BEGIN EXERCISE 5

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
right(30)
sierpinski(200, 200)
hideturtle()

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
right(30)
sierpinski(200, 100)
hideturtle()

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
right(30)
sierpinski(200, 50)
hideturtle()

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
right(30)
sierpinski(200, 25)
hideturtle()

initializeTurtle()
speed(13)
penup()
goto(350,300)
pendown()
right(30)
sierpinski(200, 10)
hideturtle()

#END EXERCISE 5

# import turtle module
import turtle as trtl
import random
# create turtle object
painter = trtl.Turtle()
#size
TwiceS = 90 / 2
Normal = 90
TwiceB = 90 * 2
#Ask the user for input
size = input("How big do you want the middle of the flower to be (TwiceS, Normal, TwiceB): ")
sides_one = int(input("How many sides do you want one of the flower pedals to be:"))
sides_two = int(input("How many sides do you want one of the other flower pedals to be:"))
sides_three = int(input("How many sides do you want one of the other flower pedals to be:"))
sides_four = int(input("How many sides do you want one of the other flower pedals to be:"))
color_one = input("What do you want the color of one of the flower pedals to be: ")
color_two = input("What do you want the color of one of the other flower pedals to be: ")
color_three = input("What do you want the color of one of the other flower pedals to be: ")
color_four = input("What do you want the color of one of the other flower pedals to be: ")
#list
pedal_color = [color_one, color_two, color_three, color_four]
pedal_shapes = [sides_one, sides_two, sides_three, sides_four]
#define
pedals = 15
length = 90
#if value
if size == 'TwiceS':
  pedals = pedals / 2
  length = length / 4
elif size == 'TwiceB':
  pedals = pedals * 2
  length = length * 4
#Define how to make the flower
def body():
  painter.penup()
  painter.setposition(0,-100)
  painter.pendown()
  painter.left(90)
  painter.forward(length)
  painter.right(90)
  painter.begin_fill()
  painter.circle(pedals * 4)
  painter.color("yellow")
  painter.end_fill()
  painter.color("black")
def peddypeddy():
  shashasha = random.choice(pedal_shapes)
  cococolor = random.choice(pedal_color)
  painter.begin_fill()
  painter.color("black")
  painter.circle(pedals, 360, shashasha)
  painter.color(cococolor)
  painter.end_fill()
  painter.penup()
  painter.left(33.75)
  painter.forward(pedals * 4)
  painter.pendown()
#draw it like a man
body()
painter.right(90)
painter.forward(pedals * 2)
painter.left(90)
painter.penup()
painter.forward(pedals * 2)
painter.pendown()
for i in range(10):
  peddypeddy()
#Congradulate the user
print("Congrats you made a weird but pretty flower!")
# create screen obfect and make it persist
wn = trtl.Screen()
wn.mainloop()
import sys
# Space Invaders - Part1
# Set up the screen
import turtle
import os
import math
import random

# Greetings and setup
from time import clock

# user_name= input("Hello, what's your name? ")
# print("Hi ", user_name, " let's play space invader")
alien_amount = 4  # int(input("Choose the amount of aliens (betwein 2-6)"))

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# Register the shapes
turtle.register_shape("sanders.gif")
turtle.register_shape("trump.gif")

# Draw border
border_pen = turtle.Turtle()  # We basically make a pixel that floats around and makes a border
border_pen.speed(0)  # fastest speed
border_pen.color("white")
border_pen.penup()  # So it starts drawing at the corner and not in the middle. Try it without this to see what happens
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for sind in range(4):
	border_pen.fd(600)  # forward 600 and then turn 90 degrees, then 600 forward
	border_pen.lt(90)  # left 90 degrees
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s"%score  # % replaces anything we write
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle, which we move aorund
player = turtle.Turtle()
player.color("yellow")
player.shape("trump.gif")
player.penup()
player.speed('fastest')
player.setposition(0, -250)  # position of turtle
player.setheading(90)

# We want the play to move by using functions & bind them to a key
playerspeed = 15

# Choose a number of enemies
number_of_enemies = alien_amount
# Creat an empty list
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
	# Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:  # all the enemies are there and now we make this for each enemy
	enemy.color("red")
	enemy.shape("sanders.gif")
	enemy.penup()
	enemy.speed('fastest')  # "lag“
	x = random.randint(-200, 200)
	y = random.randint(200, 280)
	enemy.setposition(x, y)

enemyspeed = 2  # how fast it most

# Creat the player's bullet
bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()  # don't draw a line
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()  # it should be hidden, but ready to be fired

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# functions for moving
def move_left():
	x = player.xcor()  # x-coordinate
	x -= playerspeed  # substracts playerspeed
	if x < -280:
		x = -280  # lowest value we accept is 280
	player.setx(x)  # change the player's position to new coordinate


def move_right():
	x = player.xcor()  # x-coordinate
	x += playerspeed  # add playerspeed
	if x > 280:
		x = 280  # highest value we accept is 280
	player.setx(x)  # change the player's position to new coordinate


def fire_bullet():
	# Declare bulletstate as a global if it need changed
	global bulletstate  # we need to change bulletstate globally
	if bulletstate == "ready":
		bulletstate = "fire"
		# Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor()+10
		bullet.setposition(x, y)
		bullet.showturtle()  # Need to show turtle


def isCollision(t1, t2):  # turtle1 = t1
	distance = math.sqrt(
		math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))  # pythagoras distance
	if distance < 15:
		return True
	else:
		return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
	
	for enemy in enemies:
		# Move the enemies
		x = enemy.xcor()  # from above
		x += enemyspeed
		enemy.setx(x)
		
		# Making enemy staying inside box
		if enemy.xcor() > 280:
			for e in enemies:  # if one touched the side, all go down
				y = enemy.ycor()
				y -= 40  # every time it hits the border, it drops down
				e.sety(y)
			enemyspeed *= -1  # changing the speed to -2 instead of 2
		
		if enemy.xcor() < -280:
			for e in enemies:
				y = enemy.ycor()
				y -= 40  # every time it hits the border, it drops down
				e.sety(y)
			enemyspeed *= -1  # changing the speed to -2 instead of 2 for only one enemy
		
		# Check for a collision betwee the bullet and enemy
		if isCollision(bullet, enemy):
			# Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)  # put it outside the frame
			# Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			# Update the score
			score += 10
			scorestring = "Score: %s"%score
			score_pen.clear()  # clear anything that was drwasn
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game over")
			break
	
	# Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	# Check to se if bullet inside
	if bullet.ycor() > 275:
		bullet.hideturtle()  # Make bullet disappear
		bulletstate = "ready"

wn.mainloop()
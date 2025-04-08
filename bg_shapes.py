"""
    CS 5001
    Fall 2024
    bg_shapes
    Alexander Gutting
"""

# Imports turtle module
import turtle

def background():
    """
    Function background
    Gives the terminal a title and sets the color of the background
    """
    s = turtle.Turtle()
    s.ht()
    s.screen.title("Memory Game")
    s.screen.bgcolor("light blue")

def moves_and_matches(turtle_pen):
    """
    Function moves_and_matches
    Takes one parameter: A turtle pen (turtle_pen)
    Draws a rectangle at the bottom left of the screen, which displays the
    total number of moves and total number of matches
    """
    # Pen settings
    turtle_pen.speed(10)
    turtle_pen.color("dark green")
    turtle_pen.setpos(-400, -275)
    turtle_pen.pensize(2.5)
    turtle_pen.showturtle()
    turtle_pen.pendown()

    # Draws the shape
    for i in range(2):
        turtle_pen.forward(575)
        turtle_pen.right(90)
        turtle_pen.forward(100)
        turtle_pen.right(90)
    turtle_pen.hideturtle()

def card_storage(turtle_pen2):
    """
    Function card_storage
    Takes one parameter: A turtle pen (turtle_pen2)
    Draws a square in the middle of the screen, which displays 8-12 cards
    """
    # Pen settings
    turtle_pen2.speed(10)
    turtle_pen2.color("dark red")
    turtle_pen2.setpos(-400, 375)
    turtle_pen2.pensize(5)
    turtle_pen2.showturtle()
    turtle_pen2.pendown()

    # Draws the shape
    for i in range(2):
        turtle_pen2.forward(575)
        turtle_pen2.right(90)
        turtle_pen2.forward(600)
        turtle_pen2.right(90)
    turtle_pen2.hideturtle()

def l_b_display(turtle_pen3):
    """
    Function l_b_display
    Takes one parameter: A turtle pen (turtle_pen3)
    Draws a rectangle on the right of the screen displaying the leaders/scores
    """
    # Pen settings
    turtle_pen3.speed(10)
    turtle_pen3.color("dark blue")
    turtle_pen3.setpos(210, 375)
    turtle_pen3.pensize(2.5)
    turtle_pen3.showturtle()
    turtle_pen3.pendown()

    # Draws the shape
    for i in range(2):
        turtle_pen3.forward(200)
        turtle_pen3.right(90)
        turtle_pen3.forward(600)
        turtle_pen3.right(90)
    turtle_pen3.hideturtle()
"""
    CS 5001
    Fall 2024
    messages
    Alexander Gutting
"""

# Imports turtle module
import turtle

# Imports time module
import time

# If the user wants to quit the game
def quit_game(x, y):
    """
    Function quit_game
    Takes two parameters: The coordinates of where the quit button is
    located (x, y)
    If the user clicks quit, the game will end
    """
    if 245 <= x <= 305 and -345 <= y <= -305:
        turtle.Turtle("quitmsg.gif")
        time.sleep(1)
        turtle.bye()

def card_error():
    """
    Function card_error
    If the user enters an odd number in the range of 8 and 12, this function
    will return a card warning
    """
    c_w = turtle.Turtle("card_warning.gif")
    c_w.ht()

def l_b_display_error():
    """
    Function l_b_display_error
    If the user enters an name that is over 12 characters long or enters
    nothing at all, this function will return a leaderboard error
    """
    l_b_error = turtle.Turtle("leaderboard_error.gif")
    l_b_error.ht()

def file_error():
    """
    Function file_error
    If the directory file isn't directly called in the cards function, this
    function will return a file error and kill the terminal
    """
    turtle.Turtle("file_error.gif")
    time.sleep(1)
    turtle.bye()

def win():
    winner = turtle.Turtle("winner.gif")
    winner.ht()
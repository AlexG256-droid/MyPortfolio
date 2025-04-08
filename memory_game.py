"""
    CS 5001
    Fall 2024
    memory_game
    Alexander Gutting
"""

# Imports the directive by using os.path module
import os.path

# Imports leaderboard and shape functions from the bg_shapes file
from bg_shapes import moves_and_matches, card_storage, l_b_display, background

# Imports message functions from the messages file
from messages import quit_game, card_error, l_b_display_error, file_error, win

# Imports Card class
from card import Card

# Imports turtle module
import turtle

# Imports random module
import random

# Imports time module
import time

# Defines turtle.Screen() as a variable (s)
s = turtle.Screen()

# Defines an empty dictionary storing all the card information (face_cards)
face_cards = {}

# Defines an empty list that stores pairs of identical cards (identical_cards)
identical_cards = []

# Defines an empty list that stores instances of the Card class (instances)
instances = []

# Defines two empty lists storing information of both sides of a clicked card
back_sides = []
front_sides = []

# Default numbers of guesses/matches
guesses = 0
matches = 0

def leaderboard(l_b_file, l_b, iswon, name, guesses):
    """
    Function leaderboard
    Takes five parameters: A directory file (l_b_file), a list (l_b), a
    boolean (iswon), a string (name), and an integer (guesses)
    This function reads the directory file and writes the updated leaderboard
    info to it
    """
    # The following code works if there are no issues with any files
    try:
        # Reads the directory file as l_b_file and sorts the leaderboard info
        fullpath = os.path.join(os.path.dirname(__file__), l_b_file)
        with open(fullpath, mode="r") as r_file:
            l_b_info = r_file.readlines()
            
            # Iterates through info
            if l_b == []:
                for info in l_b_info:
                    l_b.append(info.strip("\n"))

            # Updates info after user finishes a game
            if iswon == True:
                if guesses < 10:
                    l_b.append(f"0{guesses} - {name}")
                else:
                    l_b.append(f"{guesses} - {name}")

            # Sorts out the leaderboard data by lowest to highest # of guesses
            l_b.sort()

        # Writes the directory file as w_file and writes the info to the file
        with open(l_b_file, mode="w") as w_file:
            if len(l_b) >= 1:
                for i in range(len(l_b)):
                    w_file.write(f"{l_b[i]}\n")

    # If the file can't be found, this function raises an error
    except FileNotFoundError or OSError:
        file_error()

def cards(card_data_file, no_of_cards, t_cards):
    """
    Function cards
    Takes three parameters: A directory file (card_data_file), the number of
    cards inputted by the user (no_of_cards), and a list of turtle pens
    (t_cards) (short for turtle cards)
    Collects the card information and displays them in Turtle
    """
    # The following code works if there are no issues with any files
    try:
        # Reads the directory file as c_file and separates the cards
        fullpath = os.path.join(os.path.dirname(__file__), card_data_file)
        with open(fullpath, mode="r") as c_file:
            individual_cards = c_file.readlines()

            # Stores the data of the cards (face down and face up)
            face_down = []
            face_up = []
            
            # Removes some cards depending on the value of no_of_cards
            if int(no_of_cards) == 8:
                for cards in individual_cards:
                    if len(individual_cards) > 3:
                        individual_cards = individual_cards[:5]
                        t_cards = t_cards[:8] + t_cards[-1:]
            elif int(no_of_cards) == 10:
                for cards in individual_cards:
                    if len(individual_cards) > 4:
                        individual_cards = individual_cards[:6]
                        t_cards = t_cards[:10] + t_cards[-1:]
            else:
                for cards in individual_cards:
                    if len(individual_cards) > 5:
                        individual_cards = individual_cards[:7]

            # Sorts out the cards
            card_types = []
            list_of_cards = []
            for cards in individual_cards:
                card = cards.strip("\n")
                card_types.append(card)
            turtle.addshape(card_types[0])
            t_cards[-1].shape(card_types[0])
            
            # Assigns an image to each turtle pen in the t_cards list
            for i in range(len(individual_cards) - 1):
                i = i * 2
                turtle.addshape(card_types[int(i / 2 + 1)])
                t_cards[i].shape(card_types[int(i / 2 + 1)])
                t_cards[i].ht()
                t_cards[i].penup()
                t_cards[i].speed(10)
                t_cards[i + 1].shape(card_types[int(i / 2 + 1)])
                t_cards[i + 1].ht()
                t_cards[i + 1].penup()
                t_cards[i + 1].speed(10)

            # Adds to the identical_cards dictionary 
            for i in range(int(no_of_cards + 1)):
                list_of_cards.append(t_cards[i])
                if int(no_of_cards) == 8:
                    if i % 2 == 0 and i < 8:
                        identical_cards.append([t_cards[i], t_cards[i + 1]])
                elif int(no_of_cards) == 10:
                    if i % 2 == 0 and i < 10:
                        identical_cards.append([t_cards[i], t_cards[i + 1]])
                else:
                    if i % 2 == 0 and i < 12:
                        identical_cards.append([t_cards[i], t_cards[i + 1]])

            # X and y coordinates for cards
            x_and_y = []
            if int(no_of_cards) == 8:
                x_and_y = [
                    (-300, 175), (-175, 175), (-50, 175), (75, 175),
                    (-300, 0), (-175, 0), (-50, 0), (75, 0)
                ]
            elif int(no_of_cards) == 10:
                x_and_y = [
                    (-300, 250), (-175, 250), (-50, 250), (75, 250),
                    (-300, 75), (-175, 75), (-50, 75), (75, 75),
                    (-175, -100), (-50, -100)
                ]
            else:
                x_and_y = [
                    (-300, 250), (-175, 250), (-50, 250), (75, 250),
                    (-300, 75), (-175, 75), (-50, 75), (75, 75),
                    (-300, -100), (-175, -100), (-50, -100), (75, -100)
                ]

            # Assigns the positions for the cards (the back sides)
            for i in range(int(no_of_cards)):
                face_down.append(list_of_cards[-1].clone())
            for i in range(len(face_down)):
                face_down[i].setpos(x_and_y[i])
                face_down[i].st()

            # Index numbers for face-up cards to be sorted out randomly
            index_numbers = []
            if int(no_of_cards) == 8:
                index_numbers = [0, 1, 2, 3, 4, 5, 6, 7]
            elif int(no_of_cards) == 10:
                index_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                index_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

            # Assigns the positions for the cards (the front sides)
            for i in range(len(list_of_cards[:-1])):
                face_up.append(list_of_cards[i])
            for i in range(len(face_up)):
                rand_int = random.randint(0, (len(index_numbers) - 1))
                face_cards[face_down[i]] = face_up[index_numbers[rand_int]]
                face_up[index_numbers[rand_int]].setpos(x_and_y[i])
                index_numbers.remove(index_numbers[rand_int])

    # If the file can't be found, this function raises an error
    except FileNotFoundError or OSError:
        file_error()

def button_and_messages(b_and_m_data_file, turtle_pen4):
    """
    Function buttons_and_messages
    Takes two parameters: A directory file (b_and_m_data_file), a turtle pen
    (turtle_pen4)
    Collects the message information to be used in Turtle
    Also displays the quit button on the bottom right of the terminal
    """
    # The following code works if there are no issues with any files
    try:
        # Reads the directory file as d_file & separates the buttons/messages
        fullpath = os.path.join(os.path.dirname(__file__), b_and_m_data_file)
        with open(fullpath, mode="r") as d_file:
            b_and_m_list = d_file.readlines()

            # Sorts out the data
            list_of_data = []
            for data in b_and_m_list:
                b_and_m = data.strip("\n")
                turtle.addshape(b_and_m)
                turtle_pen4 = turtle.Turtle(b_and_m)
                turtle_pen4.ht()
                turtle_pen4.penup()
                turtle_pen4.speed(10)
                list_of_data.append(turtle_pen4)

            # Quit Button
            list_of_data[0].setpos(275, -325)
            list_of_data[0].st()

    # If the file can't be found, this function raises an error
    except FileNotFoundError or OSError:
        turtle.bye()

def guess_match_update(g_m, l_b, no_of_cards, name):
    """
    Function guess_match_update
    Takes three parameters: Two turtle pens (g_m, l_b), an integer
    (no_of_cards), and a string (name)
    This function is called by the is_match function after every guess. This
    function ends the guess process by updating the number of guesses and/or
    matches and determines whether or not the user won.
    """
    # Clears out the following lists to end the process of a "guess"
    back_sides.clear()
    front_sides.clear()
    instances.clear()

    # If both chosen cards are the same, one is added to the variable matches
    align = "center"
    font = ("Helvetica", 20, "bold")
    g_m.clear()
    g_m.setpos(-124, -335)
    g_m.write(f"Guesses: {guesses}   Matches: {matches}", True, align, font)

    # Calls the is_won function if there are no more cards
    is_won(l_b, no_of_cards, name)
        
def is_won(l_b, no_of_cards, name):
    """
    Function is_won
    Takes three parameters: A turtle pen (l_b), an integer (no_of_cards), and
    a string (name)
    This function is called by the guess_match_update function after every
    guess. If the global variable matches is equal to the value of no_of_cards
    divided by 2, the terminal will ask the user for another game. If the user
    says yes, a new game starts. If the user says no, the terminal ends.
    """
    # Calls the global keyword on guesses and matches
    global guesses
    global matches

    # If user wins a winner message would show up
    if matches == int(no_of_cards / 2):
        for i in range(10):
            s.ontimer(win, 100)
            s.update()

        # Adds info to the leaderboard
        leaderboard("leaderboard.txt", l_b, True, name, guesses)
        
        # Asks user for a rematch
        again = turtle.textinput("Play again", "Do you want to play again?")
        while again.lower() != "yes" and again.lower() != "no":
            again = turtle.textinput("Play again", "Do you want to play again?")

        # Starts a new game if user says "yes" and clears screen/resets values
        if again.lower() == "yes":
            s.clearscreen()
            guesses = 0
            matches = 0
            main()

        # Kills terminal if user says "no"
        elif again.lower() == "no":
            turtle.bye()

def screen_click(x, y, g_m, no_of_cards, l_b, name):
    """
    Function screen_click
    Takes six parameters: The coordinates of where a specfic card is located
    (x, y), two turtle pens (g_m, l_b), an integer (no_of_cards), and a string
    (name)
    This function comes into effect when a card is clicked on (whenever the
    user clicks on that card, it will be revealed) or when the quit button is
    clicked on
    """
    # If the user clicks on a specific card
    flip_card(x, y)

    # Determines whether or not user matches two cards
    is_match(g_m, no_of_cards, l_b, name)

    # Kills terminal if the "Quit Button" is clicked
    quit_game(x, y)

def flip_card(x, y):
    """
    Function flip_card
    Takes two parameters: The coordinates of where a specfic card is located
    (x, y)
    This function comes into effect when a card is clicked on (whenever the
    user clicks on that card, it will be revealed)
    """
    # Iterates through the face_cards dictionary and gives coordinate ranges
    for back_side, front_side in face_cards.items():
        xmin = ((front_side.xcor()) - 50)
        xmax = ((front_side.xcor()) + 50)
        ymin = ((front_side.ycor()) - 75)
        ymax = ((front_side.ycor()) + 75)

        # If one of the cards is clicked on, the front side shows and the back is hidden
        if xmin <= x <= xmax and ymin <= y <= ymax and back_side.isvisible():
            my_class = Card(back_side, front_side)
            my_class.flip()
            back_sides.append(back_side)
            front_sides.append(front_side)
            instances.append(my_class)

def is_match(g_m, no_of_cards, l_b, name):
    """
    Function is_match
    Takes four parameters: Two turtle pens (g_m, l_b), an integer
    (no_of_cards), and a string (name)
    This function determines whether or not a match is occured. If both cards
    are similar, both the front sides and the back sides are hidden. If not,
    only the front sides are hidden.
    """
    # Calls the global keyword on guesses and matches
    global guesses
    global matches
    
    # is_match comes to effect after user clicks on two cards (calls is_pair)
    if len(instances) == 2:
        time.sleep(1)
        if instances[0].is_pair(instances[1]):

            # Iterates through the identical_cards list
            for i in range(len(identical_cards)):
                if front_sides[1] in identical_cards[i]:
                    boolean1 = (front_sides[0] in identical_cards[i])
                    boolean2 = (front_sides[1] in identical_cards[i])

                    # If both front sides are similar, both cards are hidden
                    if boolean1 is True and boolean2 is True:
                        front_sides[0].ht()
                        front_sides[1].ht()
                        matches += 1
                                        
                    # If the front sides are different the back sides reappear
                    else:
                        front_sides[0].ht()
                        front_sides[1].ht()
                        back_sides[0].st()
                        back_sides[1].st()
                    guesses += 1

            # Calls the guess_match_update function
            guess_match_update(g_m, l_b, no_of_cards, name)
            
def main():
    # Sets the background color and title
    background()

    # Defines some turtle pens
    turtle_pen = turtle.Turtle()
    turtle_pen2 = turtle.Turtle()
    turtle_pen3 = turtle.Turtle()
    turtle_pen4 = turtle.Turtle()
    g_m = turtle.Turtle()
    l_b_header = turtle.Turtle()
    leaders = turtle.Turtle()

    # Defines more turtle pens (these will be used for the cards function)
    card1 = turtle.Turtle()
    card1_copy = turtle.Turtle()
    card2 = turtle.Turtle()
    card2_copy = turtle.Turtle()
    card3 = turtle.Turtle()
    card3_copy = turtle.Turtle()
    card4 = turtle.Turtle()
    card4_copy = turtle.Turtle()
    card5 = turtle.Turtle()
    card5_copy = turtle.Turtle()
    card6 = turtle.Turtle()
    card6_copy = turtle.Turtle()
    back_side = turtle.Turtle()

    # Stores the pen variables in a list
    turtle_pens = [
        turtle_pen, turtle_pen2, turtle_pen3, turtle_pen4, g_m, l_b_header,
        leaders
    ]

    # Stores the card pens in a list
    t_cards = [
        card1, card1_copy, card2, card2_copy, card3, card3_copy, card4,
        card4_copy, card5, card5_copy, card6, card6_copy, back_side
    ]

    # Iterates through the turtle_pens list to hide the pens/turtles
    for i in range(len(turtle_pens)):
        turtle_pens[i].ht()
        turtle_pens[i].penup()
        turtle_pens[i].speed(10)

    # Iterates through the t_cards list to hide the pens/turtles
    for i in range(len(t_cards)):
        t_cards[i].ht()
        t_cards[i].penup()
        t_cards[i].speed(10)

    # Calls the button/message directory function
    button_and_messages("button_and_messages.txt", turtle_pen4)

    # Asks for the users name
    name = turtle.textinput("Name", "Enter your name (max 12 characters)")
    while len(name) > 12 or len(name) == 0:
        for i in range(10):
            s.ontimer(l_b_display_error, 100)
            s.update()
        name = turtle.textinput("Name", "Enter your name (max 12 characters)")

    # Asks how many cards the user wants to play with
    question = "How many cards to play with (8, 10, or 12)?"
    no_of_cards = turtle.numinput("How many cards", question, None, 8, 12)
    card_no_variations = [8, 10, 12]
    while no_of_cards not in card_no_variations:
        for i in range(10):
            s.ontimer(card_error, 100)
            s.update()
        no_of_cards = turtle.numinput("How many cards", question, None, 8, 12)

    # Calls the turtle_data shape functions
    moves_and_matches(turtle_pen)
    card_storage(turtle_pen2)
    l_b_display(turtle_pen3)

    # If card_data_file isn't found, the file_error function is returned
    if not cards:
        file_error()

    # Calls the card directory functions if file is found
    cards("cards.txt", no_of_cards, t_cards)

    # Displays the default values of guesses/matches in the green rectangle
    g_m.setpos(-124, -335)
    align = "center"
    font = ("Helvetica", 20, "bold")
    g_m.write("Guesses: 0   Matches: 0", True, align, font)

    # Defines an empty list called l_b
    l_b = []

    # Calls the leaderboard function
    leaderboard("leaderboard.txt", l_b, False, name, guesses)

    # Displays the number of guesses and matches in the green rectangle
    l_b_header.setpos(312, 320)
    l_b_header.write("Leaders:", True, "center", ("Helvetica", 24, "bold"))

    # Y coordinates for leaderboard
    y_coord = [265, 215, 165, 115, 65, 15, -35, -85]
    
    # Writes out the leaderboard info using turtle
    if 0 < len(l_b) < 8:
        for i in range(len(l_b)):
            leaders.speed(10)
            leaders.setpos(312, y_coord[i])
            leaders.write(l_b[i], True, "center", ("Helvetica", 24, "normal"))
    elif len(l_b) >= 8:
        for i in range(8):
            leaders.speed(10)
            leaders.setpos(312, y_coord[i])
            leaders.write(l_b[i], True, "center", ("Helvetica", 24, "normal"))

    # Allows the user to flip a card or click the quit button
    s.onclick(lambda x, y: screen_click(x, y, g_m, no_of_cards, l_b, name))

    # This method is here so the terminal doesn't end unless user quits
    s.mainloop()

if __name__ == "__main__":
    main()
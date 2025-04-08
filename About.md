This project was made using a variety of functions from various imported files. All external data is transferred to
the memory_game.py file, which the game will be played on. First of all, the background function from the
bg_shapes.py file is called with a blue background. The button_and_messages function is then called to import the
quit button and several different messages that pop up if needed. This data is collected from the
button_and_messages.txt file. Two text inputs are given to the user in the main() function (name and number of
cards). If the user enters an invalid input, the terminal will give some sort of error and ask the user to enter a
valid input. After the valid inputs are entered, the last three functions from the bg_shapes.py file are called,
drawing out the shapes in the terminal. Then, the cards function is called to spread the cards randomly. The card
data is gotten from the cards.txt file and added to the face_cards dictionary. If a message pops up, that means a
function was called from the messages.py file (e.g. if the user clicks on the quit button, the quit_game function
will be called from messages.py showing the quit message and the game will end). The default number of guesses and
default number of matches show up as well as the leaderboard scores (the leaderboard data is taken from the
leaderboard.txt file).

When the game starts, the user has 8-12 cards to click on. The screen_click function allows the user to flip
cards or click on the quit button using onclick. Whether a certain card is flipped, a class called Card is called
from the card.py file and retrieves an instance. That instance will determine whether or not one or two cards are
flipped. Once the user clicks on a card, onclick will call the flip_card function and the flip function from the
Card class on the instance. After that function is called, the card will flip over (it will hide the back side
of the card and show the front side). The user can then click on another card that will call the same function,
causing that card to "flip over" as well. The functions is_match and is_pair (also from the Card class) are then
called where if the two cards are similar (according to the identical_cards dictionary), they disappear and 1 is
added to the variable matches from the guess_match_update function. If the two cards aren't equal, they flip back.
One is added to the variable guesses after each "guess". This process repeats until all the cards (both front and
back sides) are hidden and the matches variable is equal to the value of the no_of_cards variable divided by 2 or
if the user clicks on the quit button. If the user wins, a winning message will show based on the called win
function in the messages.py file.

The computer asks the user for a rematch after the game is done after calling the is_won function. If the user
says yes, a new game will start and everything will be undone (except for the leaderboard info). If the user says
no, the terminal will be killed.

NOTE: Run this project using the memory_game.py file

"""
    CS 5001
    Fall 2024
    card
    Alexander Gutting
"""

# Imports the turtle module
import turtle

class Card(turtle.RawTurtle):
    """
    Class Card
    This class takes the back and front sides of two chosen cards and
    determines whether or not both cards are equal
    """
    def __init__(self, back_side, front_side):
        """
        Constructor function
        Takes three parameters: an instance (self) and two turtle objects
        (back_side, front_side) and defines them (this function raises a
        TypeError if one or both parameters passed isn't a turtle object)
        """
        # Defines the other two parameters
        self.back_side = back_side
        self.front_side = front_side

        # If there is a parameter that isn't a turtle, a TypeError is raised
        instance_back_side = isinstance(self.back_side, turtle.Turtle)
        instance_front_side = isinstance(self.front_side, turtle.Turtle)
        if instance_back_side is not True or instance_front_side is not True:
            raise TypeError

    def flip(self):
        """
        Function flip
        Takes the self parameter and hides the back side of a chosen card and
        shows the front side
        """
        # Defines new variables, hides the back side, and shows the front side
        front_side = self.front_side
        back_side = self.back_side
        if back_side.isvisible() is True:
            back_side.ht()
            front_side.st()

        # Returns an instance of the "flipped" card
        return Card(back_side, front_side)

    def is_pair(self, other):
        """
        Function is_pair
        Takes the self parameter and another instance (other) as a parameter
        and takes the back and front sides of those instances
        Returns a boolean that is determined by whether or not the front sides
        of the two instances are visible
        """
        # Defines new variables for both the front and back sides of two cards
        back_side_self = self.back_side
        front_side1 = self.front_side
        back_side_other = other.back_side
        front_side2 = other.front_side

        # Only comes to effect after both chosen cards are flipped
        if front_side1.isvisible() and front_side2.isvisible():
            return True
        else:
            return False
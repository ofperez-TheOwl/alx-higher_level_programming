#!/usr/bin/python3
"""Module : 6-rectangle
Defines a class Rectangle with width and height as private instance attriubutes
and number of instances as public class attribute
Initiates instance attributes
Computes perimeter and area of rectangle
Can be printed with #s
Can be represented by repr
Can be deleted
"""


class Rectangle():
    """Definition of class Rectangle

    Args:
        number_of_instances (int) : current number of Rectangle instances

        width (int): size of the horizontal side of Rectangle
        height (int): size of the vertical side of Rectangle
    Functions:
        __init__(self, width, height)
        height(self)
        height(self, value)
        width(self)
        witdth.(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initiates attributes
        Attributes:
            width (int): size of the horizontal side of Rectangle
            height (int): size of the vertical side of Rectangle
        """
        self.height = height
        self.width = width
        self.number_of_instances = self.number_of_instances + 1

    @property
    def width(self):
        """width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width  to provided value
        Args:
            value (int) : size of rectangle's width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height to provided value
        Args:
            value (int) : size of rectangle height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Compute and return perimeter of rectangle
        """
        return ((2 * (self.__height + self.__width))
                if (self.__height != 0 and self.__width != 0) else 0)

    def __str__(self):
        """Representation of Rectangle as a string
        When print is called it returns the output of this function
        """
        string = ""
        if (self.__height != 0 and self.__width != 0):
            for i in range(0, self.__height):
                if (i != self.__height - 1):
                    string = string + self.__width * '#' + '\n'
                else:
                    string = string + self.__width * '#'
        return (string)

    def __repr__(self):
        """Representation of Rectangle as a string that can be read by eval()
        """
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        """Prints a message when the rectangle is deleted
        """
        print("Bye rectangle...")
        self.number_of_instances = self.number_of_instances - 1

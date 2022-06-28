#!/usr/bin/python3
"""Module : 8-rectangle
Defines a class Rectangle with width and height as private instance attriubutes
and number of instances and a char symbol as public class attributes
Initiates instance attributes
Computes perimeter and area of rectangle
Can be printed with char symbol as units
Can be represented by repr
Can be deleted
Can compare two rectangle area with a static method
"""


class Rectangle():
    """Definition of class Rectangle

    Args:
        /* public class attributes*/
        number_of_instances (int) : current number of Rectangle instances
        print_symbol (char): symbol used to print the Rectangle instances

        /* private instance attributes */
        width (int): size of the horizontal side of Rectangle
        height (int): size of the vertical side of Rectangle
    Functions:
        __init__(self, width, height)

        /* static methods */
        bigger_or_equal(rect_1, rect_2)

        /* properties */
        height(self)
        height(self, value)
        width(self)
        witdth.(self, value)

        /* normal instance methods */
        area(self)
        perimeter(self)

        /* magic instance methods */
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initiates attributes
        Attributes:
            width (int): size of the horizontal side of Rectangle
            height (int): size of the vertical side of Rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances = type(self).number_of_instances + 1

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
                    string = string + self.__width * str(self.print_symbol) \
                                    + '\n'
                else:
                    string = string + self.__width * str(self.print_symbol)
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
        type(self).number_of_instances = type(self).number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare the size of two instances of rectangle
        Args:
            rect_1 (Rectangle) : first rectangle
            rect_2 (Rectangle) : second rectangle
        Return: bigger rectangle
        """
        if (type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() < rect_2.area()):
            return (rect_2)
        return (rect_1)

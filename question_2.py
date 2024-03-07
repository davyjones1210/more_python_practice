# Write a class called Vector3D that represents a direction and length in 3D space.

class Vector3D:
    def __init__(self, max_size: int) -> None:

        #private data variables here

        pass

# The class should have three private data members to represent position in x,y,z coordinates.
# The class should have public member functions that perform the following:
#
# Vector3D() - constructor
#
# cross()    - returns the cross product of itself with another vector

    def cross_product(self):
        # returns the cross product of itself with another vector

        pass

    #
# dot()      - returns the dot product of itself with another vector
    def dot(self):

        pass

#
# getX()     - returns the x coordinate

    def getX(self):
        pass


# getY()     - returns the y coordinate

    def getY(self):
        pass

#
# getZ()     - returns the z coordinate

    def getZ(self):
        pass


# input()    - handle inputting the coordinates from the user

    def input(self):
        pass
#
# length()   - returns the length of the vector

    def length(self):
        pass
#
# output()   - prints the vector out to the screen neatly. Eg. “(1, 2, 3)”

    def output(self):
        pass

#
# set()      - set the coordinates of the vector

    def set(self):
        pass


# In the member functions above, you need to determine the return type as well as the arguments for each (if any).


#
#
# In the main function, ask the user to enter two vectors, and output the dot and cross product results.
#
# For example the program could look like this:
#
#
# Please enter the coordinates of the first vector: 1 2 3
#
# Please enter the coordinates of the first vector: 4 5 6
#
#
# The dot   product of these vectors is: 32
#
# The cross product of these vectors is: (-3, 6, -3)
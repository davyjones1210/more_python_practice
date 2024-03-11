import numpy as np
import math


# Write a class called Vector3D that represents a direction and length in 3D space.



class Vector3D:

    # The class should have three private data members to represent position in x,y,z coordinates.
    def __init__(self, x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

        self.internal_dict = {}
        self.get_user_input = ""


        #private data variables here


# The class should have public member functions that perform the following:
#
# Vector3D() - constructor
#
# cross()    - returns the cross product of itself with another vector

    def cross(self):

        # returns the cross product of itself with another vector



        cross_product = ((self.y[0] * self.z[1]) - (self.z[0] * self.y[1]),
                         (self.z[0] * self.x[1]) - (self.x[0] * self.z[1]),
                         (self.x[0] * self.y[1]) - (self.y[0] * self.x[1]))

        print("The cross product of these vectors is: ", cross_product)

        return cross_product



# dot()      - returns the dot product of itself with another vector
    def dot(self):

        # a = (x0, y0, z0)
        # b = (x1, y1, z1)

        # x = (a0, b0)
        # y = (a1, b1)
        # y = (a2, b2)

        a = (self.x[0], self.y[0], self.z[0])
        b = (self.x[1], self.y[1], self.z[1])

        dot_product = sum(x*y for x, y in zip(a, b))    #+ 100

        print("The dot product of these vectors is: ", dot_product)

        return dot_product

#
# getX()     - returns the x coordinate

    def getX(self):

        return self.x

# getY()     - returns the y coordinate

    def getY(self):

        return self.y   # +10

#
# getZ()     - returns the z coordinate

    def getZ(self):

        return self.z  # +10


# input()    - handle inputting the coordinates from the user

    def input(self):
        number_of_iterations = 2    # Hard coding the number of iterations to 2

        for i in range(0, number_of_iterations):
            try:
                self.get_user_input = input("Please enter the coordinates of the first vector: ")
            except:
                Exception

            self.internal_dict[i] = self.get_user_input

        return self.internal_dict


# length()   - returns the length of the vector

    def length(self):

        a = (self.x[0], self.y[0], self.z[0])
        b = (self.x[1], self.y[1], self.z[1])

        len_a, len_b = (math.sqrt(sum(i ** 2 for i in a)), math.sqrt(sum(i ** 2 for i in b)))

        return len_a, len_b


# output()   - prints the vector out to the screen neatly. Eg. “(1, 2, 3)”

    def output(self):

        # a = (x0, y0, z0)
        # b = (x1, y1, z1)

        # x = (a0, b0)
        # y = (a1, b1)
        # y = (a2, b2)

        print("The entered vectors are: ")
        print("1st vector: ", (self.x[0], self.y[0], self.z[0]))
        print("2st vector: ", (self.x[1], self.y[1], self.z[1]))
        #print(a)

# set()      - set the coordinates of the vector

    def set(self, internal_dict: dict):

        a_values_from_dict = self.internal_dict[0].split(" ")

        a_values = [int(value) for value in a_values_from_dict]

        b_values_from_dict = self.internal_dict[1].split(" ")

        b_values = [int(value) for value in b_values_from_dict]

        a = tuple(a_values)

        b = tuple(b_values)


        #Setting values to initialized variables in __init__

        # a = (x0, y0, z0)
        # b = (x1, y1, z1)

        # x = (a0, b0)
        # y = (a1, b1)
        # y = (a2, b2)

        self.x = (a[0], b[0])
        self.y = (a[1], b[1])
        self.z = (a[2], b[2])

# In the member functions above, you need to determine the return type as well as the arguments for each (if any).


# In the main function, ask the user to enter two vectors, and output the dot and cross product results.

def main():
    #start of program

    main_instance = Vector3D(None,None,None)

    main_instance.internal_dict = main_instance.input()   # asking the user to enter two vectors

    # calling set function to take in the dict with the user intput and set coordinates

    main_instance.set(main_instance.internal_dict)

    dot_prod = main_instance.dot()

    cross_prod = main_instance.cross()

    main_instance.output()

    length_a, length_b = main_instance.length()


    print("Length = ", length_a, "and ", length_b)



#main entry point to the program
if __name__ == "__main__":
    main()


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
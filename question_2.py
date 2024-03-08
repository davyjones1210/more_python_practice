import numpy as np
import math


# Write a class called Vector3D that represents a direction and length in 3D space.



class Vector3D:

    # The class should have three private data members to represent position in x,y,z coordinates.
    def __init__(self, x,y,z) -> None:
        self.x1 = x
        self.y1 = y
        self.z1 = z

        self.internal_dict = {}
        self.get_user_input = ""


        #private data variables here

        pass


# The class should have public member functions that perform the following:
#
# Vector3D() - constructor
#
# cross()    - returns the cross product of itself with another vector

    def cross(self, a, b):

        # returns the cross product of itself with another vector

        cross_product = [a[1] * b[2] - a[2] * b[1],
             a[2] * b[0] - a[0] * b[2],
             a[0] * b[1] - a[1] * b[0]]

        return cross_product



# dot()      - returns the dot product of itself with another vector
    def dot(self, a, b):
        dot_product = sum(x*y for x, y in zip(a, b))    #+ 100
        # print(type(dot_product))

        return dot_product

#
# getX()     - returns the x coordinate

    def getX(self, a):
        self.x1, self.y1, self.z1 = a

        return self.x1

        pass



# getY()     - returns the y coordinate

    def getY(self, a):
        self.x1, self.y1, self.z1 = a

        return self.y1   # +10

#
# getZ()     - returns the z coordinate

    def getZ(self, a):
        self.x1, self.y1, self.z1 = a

        return self.z1  # +10


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



#
# length()   - returns the length of the vector

    def length(self, a):

        return math.sqrt(sum(i ** 2 for i in a))

#
# output()   - prints the vector out to the screen neatly. Eg. “(1, 2, 3)”

    def output(self, a):
        print(a)
#
# set()      - set the coordinates of the vector

    def set(self, internal_dict: dict):


        self.x1, self.y1, self.z1 = a








# In the member functions above, you need to determine the return type as well as the arguments for each (if any).


#
#
# In the main function, ask the user to enter two vectors, and output the dot and cross product results.
#



def main():
    #start of program
    main_instance = Vector3D(None,None,None)

    main_instance.internal_dict = main_instance.input()   # asking the user to enter two vectors

    a_values_from_dict = main_instance.internal_dict[0].split(" ")

    a_values = [int(value) for value in a_values_from_dict]

    b_values_from_dict = main_instance.internal_dict[1].split(" ")

    b_values = [int(value) for value in b_values_from_dict]

    #set(main_instance.internal_dict)

    #b = set()

    a = tuple(a_values)

    b = tuple(b_values)





    # a = (1, 2, 3)
    # b = (4, 5, 6)
    print("a = ", a)
    print("b = ", b)
    print("a type = ", type(a))
    print("b type = ", type(b))
    main_instance.dot(a,b)
    #main_instance.set(b)
    len = main_instance.length(a)
    #print("length: ", len)


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
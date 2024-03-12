import math


# Write a class called Vector3D that represents a direction and length in 3D space.



class Vector3D:

    # The class should have three private data members to represent position in x,y,z coordinates.
    def __init__(self, x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

    # private data variables here

    # The class should have public member functions that perform the following:
    #
    # Vector3D() - constructor
    #
    # cross()    - returns the cross product of itself with another vector

    def cross(self, b):
        a = (self.x, self.y, self.z)

        cross_product = [a[1] * b[2] - a[2] * b[1],
             a[2] * b[0] - a[0] * b[2],
             a[0] * b[1] - a[1] * b[0]]

        return cross_product


    # dot()      - returns the dot product of itself with another vector
    def dot(self, b):
        a = (self.x, self.y, self.z)
        dot_product = sum(x * y for x, y in zip(a, b))  # + 100

        print("The dot product of these vectors is: ", dot_product)

        return dot_product


    # getX()     - returns the x coordinate

    def getX(self):
        return self.x


    # getY()     - returns the y coordinate

    def getY(self):
        return self.y


    # getZ()     - returns the z coordinate

    def getZ(self):
        return self.z


    # input()    - handle inputting the coordinates from the user

    def input(self):

        while True:

            user_input = input("Please enter the coordinates of the first vector: ")

            if user_input == '-1':
                break

            try:
                int_list = [int(i) for i in user_input.split(" ")]
                break
                #print("Printing int list: ", int_list)

            except ValueError:
                print("ValueError: That's not an integer. Please try to input numbers separated by a space")



        return user_input

    # length()   - returns the length of the vector

    def length(self, b):
        a = (self.x, self.y, self.z)
        len_a, len_b = (math.sqrt(sum(i ** 2 for i in a)), math.sqrt(sum(i ** 2 for i in b)))

        return len_a, len_b


    # output()   - prints the vector out to the screen neatly. Eg. “(1, 2, 3)”

    def output(self, first_input, second_input):
        print("The entered vectors are (from within the output function:")

        print("first input: ", first_input)
        print("second input: ", second_input)


    # set()      - set the coordinates of the vector

    def set(self, user_input):

        parsed_user_input = user_input.split(" ")

        user_input_list = [int(value) for value in parsed_user_input]
        user_input_tuple = tuple(user_input_list)

        self.x, self.y, self.z = user_input_tuple

        return user_input_tuple


# In the member functions above, you need to determine the return type as well as the arguments for each (if any).


# In the main function, ask the user to enter two vectors, and output the dot and cross product results.


def main():

    # initializing the two vectors
    first_instance = Vector3D(None, None, None)
    second_instance = Vector3D(None, None, None)

    first_input = first_instance.input()   # asking the user to enter two vectors
    second_input = second_instance.input()   # asking the user to enter two vectors
    #print("First input = ", first_input)

    first_input = first_instance.set(first_input)
    second_input = second_instance.set(second_input)


    dot_prod = first_instance.dot(second_input)
    print("Dot prod: ", dot_prod)

    cross_prod = first_instance.cross(second_input)
    print("Cross prod: ", cross_prod)

    length_a, length_b = first_instance.length(second_input)    # will using first_instance.length(second_instance.input()) also work?

    print("Length = ", length_a, "and ", length_b)

    first_instance.output(first_input, second_input)


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
import math


# Write a class called Vector3D that represents a direction and length in 3D space.



class Vector3D:

    # The class should have three private data members to represent position in x,y,z coordinates.
    def __init__(self, x,y,z) -> None:
        """
            Constructor to initialize the 3 variables representing coordinates of the 3D Vector

                Parameters:
                    The x, y, z coordinates of the 3D vector

                Returns:
                    None
        """
        self.x = x
        self.y = y
        self.z = z



    # cross()    - returns the cross product of itself with another vector

    def cross(self, b):
        """
            Calculates the cross product of the vector in its instance with the vector passed

                Parameters:
                    The x, y, z coordinates of the second 3D vector

                Returns:
                    Calculated cross product of the two vectors
        """
        a = (self.x, self.y, self.z)

        try:
            cross_product = [a[1] * b[2] - a[2] * b[1],
             a[2] * b[0] - a[0] * b[2],
             a[0] * b[1] - a[1] * b[0]]
            print("The cross product of these vectors is: ", cross_product)

            return cross_product
        except IndexError:
            print("IndexError (cross): You did not enter the values in the correct format. Please run the program again")


    # dot()      - returns the dot product of itself with another vector
    def dot(self, b):
        """
            Calculates the dot product of the vector in its instance with the vector passed

                Parameters:
                    The x, y, z coordinates of the second 3D vector

                Returns:
                    Calculated dot product of the two vectors
        """
        a = (self.x, self.y, self.z)
        try:
            dot_product = sum(x * y for x, y in zip(a, b))  # + 100
            print("The dot product of these vectors is: ", dot_product)
            return dot_product
        except TypeError or UnboundLocalError:
            print("TypeError or UnboundLocalError (dot): You did not enter the values in the correct format. Please run the program again")






    # getX()     - returns the x coordinate

    def getX(self):
        """
            Returns the x coordinate

                Parameters:
                    None

                Returns:
                    X coordinate of the instanced vector
        """
        return self.x


    # getY()     - returns the y coordinate

    def getY(self):
        """
            Returns the y coordinate

                Parameters:
                    None

                Returns:
                    Y coordinate of the instanced vector
        """
        return self.y


    # getZ()     - returns the z coordinate

    def getZ(self):
        """
            Returns the z coordinate

                Parameters:
                    None

                Returns:
                    Z coordinate of the instanced vector
        """
        return self.z


    # input()    - handle inputting the coordinates from the user

    def input(self):
        """
            handle inputting the coordinates from the user

                Parameters:
                    None

                Returns:
                    Returns the user input in string format
        """

        while True:

            user_input = input("Please enter the coordinates of the first vector: ")

            if user_input == "-1":
                quit()

            try:
                int_list = [int(i) for i in user_input.split(" ")]
                break


            except ValueError:
                print("ValueError(input): That's not an integer. Please try to input numbers separated by a space")



        return user_input

    # length()   - returns the length of the vector

    def length(self, b):
        """
            Calculates the length of the vector in its instance with the vector passed

                Parameters:
                    The x, y, z coordinates of the second 3D vector

                Returns:
                    Calculated length of the two vectors
        """
        a = (self.x, self.y, self.z)

        try:
            len_a, len_b = (math.sqrt(sum(i ** 2 for i in a)), math.sqrt(sum(i ** 2 for i in b)))

            return len_a, len_b

        except TypeError:
            print("TypeError (Length): You did not enter the values in the correct format. Please run the program again")


    # output()   - prints the vector out to the screen neatly. Eg. “(1, 2, 3)”

    def output(self, first_input, second_input):
        """
            prints the vector out to the screen neatly

                Parameters:
                    First and second vector inputs

                Returns:
                    None
        """
        print("The entered vectors are (from within the output function):")

        print("first input: ", first_input)
        print("second input: ", second_input)


    # set()      - set the coordinates of the vector

    def set(self, user_input):
        """
            set the coordinates of the vector

                Parameters:
                    Takes in the string input from the user and assigns it to initialized variables in constructor

                Returns:
                    Returns a neat integer tuple of the set vector
        """

        parsed_user_input = user_input.split(" ")
        try:
            user_input_list = [int(value) for value in parsed_user_input]
            user_input_tuple = tuple(user_input_list)

            self.x, self.y, self.z = user_input_tuple
        except ValueError:
            print("ValueError (set): You did not enter the values in the correct format. Please run the program again")

        return user_input_tuple


# In the member functions above, you need to determine the return type as well as the arguments for each (if any).


# In the main function, ask the user to enter two vectors, and output the dot and cross product results.


def main():

    # initializing the two vectors
    first_instance = Vector3D(None, None, None)
    second_instance = Vector3D(None, None, None)

    first_input = first_instance.input()   # asking the user to enter two vectors
    second_input = second_instance.input()   # asking the user to enter two vectors


    first_input = first_instance.set(first_input)
    second_input = second_instance.set(second_input)



    dot_prod = first_instance.dot(second_input)

    cross_prod = first_instance.cross(second_input)


    length = first_instance.length(second_input)    # will using first_instance.length(second_instance.input()) also work?
    try:
        length_a = length[0]
        length_b = length[1]
        print("Length = ", length_a, "and ", length_b)
    except Exception:
        print("You did not enter the values in the correct format. Please run the program again")




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
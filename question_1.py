import re
# Write a program that transforms the given ASCII image:

ascii_pic = """##.....##.########.##.....##.
##.....##.##.......##.....##.
##.....##.##.......##.....##.
##.....##.######...##.....##.
##.....##.##........##...##..
##.....##.##.........##.##...
.#######..##..........###....
"""

ascii_encoded_pic = """#2.5#2.1#8.1#2.5#2.1
#2.5#2.1#2.7#2.5#2.1
#2.5#2.1#2.7#2.5#2.1
#2.5#2.1#6.3#2.5#2.1
#2.5#2.1#2.8#2.3#2.2
#2.5#2.1#2.9#2.1#2.3
.1#7.2#2.10#3.4
"""
# class fun with ascii

class FunWithAscii:

    def __init__(self):
        pass




# get ascii image()

    def get_ascii_image(self):
        return ascii_pic



# encode ascii image()

    def encode_ascii_image(self, ascii_pic):
        #print("Printing ascii_pic: ", (ascii_pic).split('\n'))



        encoded_ascii_pic = ""
        # Iterate over the string
        for line in ascii_pic.split('\n'):
            if not line:
                continue
            parsed_string = re.findall('#+|\.+', line)
            #print(parsed_string)
            #Now calculating meta data
            for element in parsed_string:
                encoded_ascii_pic = encoded_ascii_pic + str(element[0]) + str(len(element))

            encoded_ascii_pic = encoded_ascii_pic + "\n"
        #print(repr(encoded_ascii_pic))
        #print(encoded_ascii_pic)
        return encoded_ascii_pic



    """
    And encodes it by replacing the characters with the symbol followed by the count. 
    For example, the above image would transform to:
    
    #2.5#2.1#8.1#2.5#2.1 
    #2.5#2.1#2.7#2.5#2.1
    #2.5#2.1#2.7#2.5#2.1
    #2.5#2.1#6.3#2.5#2.1
    #2.5#2.1#2.8#2.3#2.2
    #2.5#2.1#2.9#2.1#2.3
    .1#7.2#2.10#3.4     
    
    """

# The program should take the ascii_pic,
# encode it to the representation above and
# save it to a file.

# save to file()

    def save_to_file(self, encoded_ascii_pic):
        with open("output.txt", "w") as h:
            h.write(encoded_ascii_pic)


# The program only needs to worry about the period (.) and the hash (#) symbols.



# Next, see if you can read the file back in and
# read from file()

    def read_from_file(self):

        file1 = open("output.txt", "r")
        contents = file1.read()
        file1.close()
        return contents


# print the encoded version back to the screen.
# display encoded version()

    def display_encoded_version(self, contents_of_file_read):
        print("Printing the encoded version back on the screen")
        #print("Tricked ya!")
        print(contents_of_file_read)



# The program should also print out the size of each string:
#
# Source image size: 210
# Encoded image size: 142
# Encoding is 32.38% smaller!


# display size of each string()


    def display_string_size(self, contents_of_file_read):


        percent_change = 100 * (len(ascii_pic) - len(contents_of_file_read)) / len(ascii_pic)
        change_comment = ""
        if percent_change > 0:
            change_comment = "% smaller!"
        elif percent_change < 0:
            change_comment = "% larger!"
        elif percent_change == 0:
            change_comment = "% unchanged!"

        percent_change = round(percent_change, 2)
        string_info = "Source image size: " + str(len(ascii_pic)) + "\n" + "Encoded image size: " + str(len(contents_of_file_read)) + "\n" + "Encoding is " + str(percent_change) + str(change_comment)
        string_info = string_info.strip()

        return string_info

# Bonus: Can you write a function to decode back to the source string!?

# decode to ascii image()

    def decode_to_ascii(self, encoded_ascii_pic):

        char_hash = "#"
        count_hash = 0
        char_dot = "."
        count_dot = 0
        n=2
        decoded_string = ""
        elements_list = []
        # Iterate over the string
        for line in encoded_ascii_pic.split('\n'):
            decoded_string = decoded_string + "\n"
            #print("Printing each line: ")
            # for element in line.split('.'):
            element1 = re.split(r'\d+', line)
            element2 = re.split(r'\D+', line)
            #element = [line[i:i + n] for i in range(0, len(line), n)]
            # print(element1)
            # print(element2)

            for i in range(0, len(element1)-1):
                decoded_string += element1[i]*int(element2[i+1])

            # decoded_string = decoded_string + "\n"



        # print(decoded_string)
        # print(ascii_pic)
        return decoded_string


        #
        #         if element == "#":
        #
        #             # If first element of line
        #             if count_hash == 0 and count_dot == 0:
        #                 decoded_string += element
        #                 count_hash += 1
        #                 continue
        #             # If first time seeing this element after reading dots
        #             if count_hash == 0:
        #                 #decoded_string += str(count_dot)
        #                 decoded_string += element
        #                 count_dot = 0
        #
        #             count_hash += 1
        #             continue
        #
        #         if element.isnumeric():
        #             if count_hash > 0:
        #                 #count_hash = element.isnumeric()
        #                 for _ in range(0, element.isnumeric()):
        #                     decoded_string += char_hash
        #
        #             if count_dot > 0:
        #                 for _ in range(0, element.isnumeric()):
        #                     decoded_string += char_dot
        #
        #
        #
        #
        #
        #         if element == ".":
        #
        #             # If first element of line
        #             if count_hash == 0 and count_dot == 0:
        #                 decoded_string += element
        #                 count_dot += 1
        #
        #             # If first time seeing this element after reading hashes
        #             if count_dot == 0:
        #                 #decoded_string += str(count_hash)
        #                 decoded_string += element
        #                 count_hash = 0
        #
        #             count_dot += 1
        #             continue
        #
        #         print(decoded_string)
        # pass


# if __name__ == "__main__":

test_run = FunWithAscii()
encoded_ascii_pic = test_run.encode_ascii_image(ascii_pic)
test_run.save_to_file(encoded_ascii_pic)
file_read = test_run.read_from_file()

test_run.display_encoded_version(file_read)
string_size_info = test_run.display_string_size(file_read)

decoded_string = test_run.decode_to_ascii(encoded_ascii_pic)
    #print(file_read)
    #save_to_file(encoded_ascii_pic)
from question_1 import FunWithAscii
from unittest.mock import Mock, patch, mock_open
import builtins
import contextlib, io
import unittest

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

# pytest test_question_1.py --cov-report term-missing --cov -v

def test_get_ascii_image():
    first_pass = FunWithAscii()

    test_ascii_image = first_pass.get_ascii_image()

    assert ascii_pic == test_ascii_image

def test_encode_ascii_image():
    second_pass = FunWithAscii()

    assert ascii_encoded_pic == second_pass.encode_ascii_image(ascii_pic)

def test_save_to_file():
    third_pass = FunWithAscii()
    open_mock = mock_open()
    with patch("question_1.open", open_mock, create=True):
        third_pass.save_to_file("test-data")

    open_mock.assert_called_with("output.txt", "w")
    open_mock.return_value.write.assert_called_once_with("test-data")

def test_read_from_file():
    fourth_pass = FunWithAscii()
    sample_file1 = open("output.txt", "r")
    contents = sample_file1.read()
    test_file = fourth_pass.read_from_file()
    assert contents == test_file
    sample_file1.close()

def test_display_string_size():
    fifth_pass = FunWithAscii()
    test_file = fifth_pass.read_from_file()
    read_test_data = fifth_pass.display_string_size(test_file).strip()
    source_data = "Source image size: 210\nEncoded image size: 142\nEncoding is 32.38% smaller!"
    source_data = source_data.strip()
    print("Printing source data: ", len(source_data))
    print(len(read_test_data))
    assert read_test_data == source_data

def test_decode_to_ascii():
    sixth_pass = FunWithAscii()
    test_file = sixth_pass.read_from_file()
    # read_test_data = sixth_pass.display_string_size(test_file).strip()
    decoded_string = sixth_pass.decode_to_ascii(ascii_encoded_pic).strip()
    assert decoded_string == ascii_pic.strip()


def test_display_encoded_version():
    seventh_pass = FunWithAscii()
    test_file = seventh_pass.read_from_file()
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock

    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            seventh_pass.display_encoded_version("5")
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        assert output.startswith("Printing the encoded version back on the screen")

    finally:
        builtins.print = print_original  # ensure print is "unmocked"


def test_if_loop_in_display_string_size():
    eight_pass = FunWithAscii()
    test_file = eight_pass.read_from_file()
    # test_100_chars = ""
    # for i in range(0, 100):
    #     test_100_chars += str(i) + "\n"
    test_file_unchanged = test_file + "99999999999999999999999999999999999999999999999999999900000000000000"
    test_file_larger = test_file + "99999999999999999999999999999999999999999999999999999900000000000000000"
    print(test_file)
    read_test_data_unchanged = eight_pass.display_string_size(test_file_unchanged).strip()
    read_test_data_larger = eight_pass.display_string_size(test_file_larger).strip()
    print("Printed display string size data unchanged: ", read_test_data_unchanged)
    print("Printed display string size data unchanged: ", read_test_data_larger)

    assert "unchanged" in read_test_data_unchanged
    assert "larger" in read_test_data_larger








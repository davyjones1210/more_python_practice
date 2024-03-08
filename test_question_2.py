from question_2 import Vector3D
import numpy as np
from unittest.mock import Mock, patch, mock_open
import builtins
import contextlib, io


a = (1, 2, 3)
b = (4, 5, 6)

# x = (1, 4)
# y = (2, 5)
# z = (3, 6)

# x = (a0, b0)
# y = (a1, b1)
# y = (a2, b2)
# pytest test_question_2.py --cov-report term-missing --cov -v

print("a type: ", type(a))
print("b type: ", type(b))

# pytest test_question_2.py::test_dot -s
def test_cross():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    print("Printing init values: ", first_trial.x, first_trial.y, first_trial.z)

    test_output = first_trial.cross()
    numpy_output = np.cross(a, b)

    print("printing test outputs ", test_output, numpy_output)
    print("Printing test output types ", type(numpy_output), type(test_output))

    assert list(test_output) == numpy_output.tolist()

def test_dot():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_output = first_trial.dot()
    numpy_output = np.dot(a, b)

    np.testing.assert_equal(test_output, numpy_output)  #Testing here

# pytest test_question_2.py::test_getX -s

def test_getX():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_output = first_trial.getX()
    # print("test output: ", test_output)
    test_x = (1, 4)
    # print("test output: ", numpy_output)
    # x1, y1, z1 = test_output

    np.testing.assert_equal(test_output, test_x)


# pytest test_question_2.py::test_getY -s
def test_getY():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_output = first_trial.getY()
    test_y = (2, 5)

    np.testing.assert_equal(test_output, test_y)
# pytest test_question_2.py::test_getZ -s
def test_getZ():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_output = first_trial.getZ()
    test_z = (3, 6)

    np.testing.assert_equal(test_output, test_z)

# pytest test_question_2.py::test_output_works -s
def test_output_works():
    first_trial = Vector3D((1, 4), (2, 5), (3, 6))
    # print(first_trial.output(a))

    # test_file = first_trial.output()
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock

    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            first_trial.output()
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        assert output.startswith("The entered vectors are: ")

    finally:
        builtins.print = print_original  # ensure print is "unmocked"

# pytest test_question_2.py::test_set_vector -s
def test_set_vector():
    second_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_dict = second_trial.input()
    second_trial.set(test_dict)

    print("Test_set_vector: ", test_dict)
    print("Actual vector: (1, 4)")


    if second_trial.x == (1, 4):
        print("Values set: ", second_trial.x)
        assert True
    else:
        print("Values not set")
        assert False

# pytest test_question_2.py::test_length_of_vector -s
def test_length_of_vector():
    second_trial = Vector3D((1, 4), (2, 5), (3, 6))
    test_output = second_trial.length()
    a = (1, 2, 3)
    b = (4, 5, 6)
    # print("Printing test output: ", test_output)
    numpy_output = (np.linalg.norm(a), np.linalg.norm(b))
    # print("Printing numpy output: ", numpy_output)

    #print("Printing Magnitude: ", x)

    np.testing.assert_equal(test_output, numpy_output)  # Testing here

def test_input_works():
    # first_trial = Vector3D(None, None, None)
    # test_dict = first_trial.input()
    # print("printing test dict", test_dict)
    # input1 = (test_dict[1].strip(),)       # hard coding for only 2 inputs
    # input2 = tuple(test_dict[2].strip())
    # print("input1 ", input1)
    # print("input1 type ", input1)
    # print("input2 ", type(input2))
    # print("input2 ", type(input2))

    pass


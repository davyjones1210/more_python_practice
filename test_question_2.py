from question_2 import Vector3D
import numpy as np
from unittest.mock import Mock, patch, mock_open
import builtins
import contextlib, io


a = (1, 2, 3)
b = (4, 5, 6)

print("a type: ", type(a))
print("b type: ", type(b))

def test_cross():
    first_trial = Vector3D(None, None, None)



    test_output = first_trial.cross(a,b)
    numpy_output = np.cross(a, b)

    #print("printing test outputs ", test_output, numpy_output)
    #print("Printing test output types ", type(numpy_output), type(test_output))

    #assert test_output == numpy_output.tolist()

def test_dot():
    first_trial = Vector3D(None, None, None)
    test_output = first_trial.dot(a, b)
    numpy_output = np.dot(a, b)

    np.testing.assert_equal(test_output, numpy_output)  #Testing here

# pytest test_question_2.py --cov-report term-missing --cov -v
def test_getX():
    first_trial = Vector3D(None, None, None)
    test_output = first_trial.getX(a)
    # print("test output: ", test_output)
    numpy_output = np.array(a)
    # print("test output: ", numpy_output)
    # x1, y1, z1 = test_output
    x2, y2, z2 = numpy_output
    #
    np.testing.assert_equal(test_output, x2)

def test_getY():
    first_trial = Vector3D(None, None, None)
    test_output = first_trial.getY(a)
    numpy_output = np.array(a)
    x2, y2, z2 = numpy_output

    np.testing.assert_equal(test_output, y2)

def test_getZ():
    first_trial = Vector3D(None, None, None)
    test_output = first_trial.getZ(a)
    numpy_output = np.array(a)
    x2, y2, z2 = numpy_output

    np.testing.assert_equal(test_output, z2)


def test_output_works():
    first_trial = Vector3D(None, None, None)
    # print(first_trial.output(a))

    # test_file = first_trial.output()
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock

    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            first_trial.output(a)
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        assert output.startswith("(1, 2, 3)")

    finally:
        builtins.print = print_original  # ensure print is "unmocked"

# pytest test_question_2.py::test_set_vector --cov -v
def test_set_vector():
    second_trial = Vector3D(None, None, None)
    print("First trial: ", second_trial.x1)
    print("X: ", second_trial.x1)

    second_trial.set(b)
    print("First trial: ", second_trial.x1)
    print("X: ", second_trial.x1)


    if second_trial.x1 is None:
         print("Values not set")
         assert False
    else:
        print("Values set: ", second_trial.x1)
        assert True

    # try:
    #     first_trial.set(a)
    #     print("Values set: ", first_trial.set(a))
    #     #assert True
    # except Exception:
    #     print("Values not set")
        #assert False
    # pass

def test_length_of_vector():
    first_trial = Vector3D(None, None, None)
    test_output = first_trial.length(a)
    print("Printing test output: ", test_output)
    numpy_output = np.linalg.norm(a)
    #print("Printing Magnitude: ", x)

    np.testing.assert_equal(test_output, numpy_output)  # Testing here

def test_input_works():
    first_trial = Vector3D(None, None, None)
    test_dict = first_trial.input()
    print("printing test dict", test_dict)
    input1 = (test_dict[1].strip(),)       # hard coding for only 2 inputs
    input2 = tuple(test_dict[2].strip())
    print("input1 ", input1)
    print("input1 type ", input1)
    print("input2 ", type(input2))
    print("input2 ", type(input2))

    pass


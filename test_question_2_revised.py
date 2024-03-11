from question_2_revised import Vector3D
import numpy as np
from unittest.mock import Mock, patch, mock_open
import builtins
import contextlib, io


# pytest test_question_2_revised.py::test_cross -s
def test_cross():
    first_trial = Vector3D(1 , 2, 3)
    second_trial = Vector3D(4, 5, 6)

    a = (first_trial.x, first_trial.y, first_trial.z)
    b = (second_trial.x, second_trial.y, second_trial.z)
    test_output = first_trial.cross(b)
    print("Test output: ", a, b)
    numpy_output = np.cross(a, b)

    assert list(test_output) == numpy_output.tolist()

# pytest test_question_2_revised.py::test_dot -s
def test_dot():
    first_trial = Vector3D(1, 2, 3)
    second_trial = Vector3D(4, 5, 6)

    a = (first_trial.x, first_trial.y, first_trial.z)
    b = (second_trial.x, second_trial.y, second_trial.z)
    test_output = first_trial.dot(b)
    print("Test output: ", a, b)
    numpy_output = np.dot(a, b)

    assert test_output == numpy_output

# pytest test_question_2_revised.py::test_getX -s
def test_getX():
    first_trial = Vector3D(1, 2, 3)
    test_output = first_trial.getX()
    assert test_output == 1

# pytest test_question_2_revised.py::test_getY -s
def test_getY():
    first_trial = Vector3D(1, 2, 3)
    test_output = first_trial.getY()
    assert test_output == 2

# pytest test_question_2_revised.py::test_getY -s
def test_getZ():
    first_trial = Vector3D(1, 2, 3)
    test_output = first_trial.getZ()
    assert test_output == 3

# pytest test_question_2_revised.py::test_input_works -s
def test_input_works():
    first_trial = Vector3D(None, None, None)
    first_input = first_trial.input()

    try:
        int_list = [int(i) for i in first_input.split(" ")]
        print("Printing int list: ", int_list)
    except ValueError:
        print("ValueError: That's not an integer")
    pass

import pytest
import mock         #Is there a way to autmatically script installing this package?
from question_2_revised import Vector3D
import numpy as np
from unittest.mock import Mock, patch, mock_open
from io import StringIO
import builtins
import contextlib, io


# pytest test_question_2_revised.py --cov-report term-missing --cov -v
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
# @patch('builtins.input', return_value="yes")
# def test_input_works(mock_input):
#     with patch('sys.stdout', new=StringIO()) as mock_stdout:
#         first_trial = Vector3D(1, 2, 3)
#         first_trial.input()
#         self.assertEqual(mock_stdout.getvalue().strip(), "Quitter!")
#
#     pass




#pytest test_question_2_revised.py --cov-report term-missing --cov -v
# pytest test_question_2_revised.py::test_length -s
def test_length():
    first_trial = Vector3D(None, None, None)
    second_trial = Vector3D(None, None, None)

    first_test_input = first_trial.set('1 2 3')
    second_test_input = second_trial.set('4 5 6')

    length_a, length_b = first_trial.length(second_test_input)
    assert length_a == 3.7416573867739413 and length_b == 8.774964387392123

# pytest test_question_2_revised.py::test_set_works -v
def test_set_works():
    first_trial = Vector3D(1, 2, 3)
    with pytest.raises(Exception):
        first_trial.set('4 5 a')

# pytest test_question_2_revised.py::test_cross_exception_works -v
def test_cross_exception_works():
    first_trial = Vector3D(1, 2, 3)
    second_trial = Vector3D(None, None, None)
    # first_trial.cross((4,))
    with pytest.raises(Exception):
        first_trial.cross((4, 5))


# pytest test_question_2_revised.py::test_dot_works -v
def test_dot_works():
    first_trial = Vector3D(1, 2, 3)
    with pytest.raises(TypeError):
        first_trial.dot((4))

# pytest test_question_2_revised.py::test_length_works -v
def test_length_works():
    first_trial = Vector3D(1, 2, 3)
    with pytest.raises(TypeError):
        first_trial.length((4))

# pytest test_question_2_revised.py::test_output_works -v
def test_output_works():
    first_trial = Vector3D(1, 2, 3)
    second_trial = Vector3D(4, 5, 6)

    first_input = (1, 2, 3)
    second_input = (4, 5, 6)
    # print(first_trial.output(a))

    # test_file = first_trial.output()
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock

    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            first_trial.output(first_input, second_input)
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        assert output.startswith("The entered vectors ")

    finally:
        builtins.print = print_original  # ensure print is "unmocked"

# pytest test_question_2_revised.py --cov-report term-missing --cov -v
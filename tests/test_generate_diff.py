from gendiff.generate_diff import generate_diff
import pytest
import json

@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        pytest.param('file1.json',
                     'file2.json',
                     'correct_result.txt')
    ]
)  
def test_diff(file1, file2, expected):
    result = open(expected, 'r')
    assert generate_diff(file1, file2) == result
from gendiff.generate_diff import generate_diff
import pytest


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        pytest.param('tests/fixtures/file1.json',
                     'tests/fixtures/file2.json',
                     'tests/fixtures/correct_result.txt'),
        pytest.param('tests/fixtures/filepath1.yml',
                     'tests/fixtures/filepath2.yml',
                     'tests/fixtures/correct_result.txt')
    ]
)  
def test_diff(file1, file2, expected):
    result = open(expected, 'r').read()
    print(generate_diff(file1, file2))
    assert generate_diff(file1, file2) == result
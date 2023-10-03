from gendiff.gen_diff import generate_diff
import pytest


@pytest.mark.parametrize(
    "file1, file2, formater, expected",
    [
        pytest.param('tests/fixtures/file1.json',
                     'tests/fixtures/file2.json',
                     'stylish',
                     'tests/fixtures/correct_result.txt'),
        pytest.param('tests/fixtures/filepath1.yml',
                     'tests/fixtures/filepath2.yml',
                     'stylish',
                     'tests/fixtures/correct_result_tree.txt'),
        pytest.param('tests/fixtures/file1.yml',
                     'tests/fixtures/file2.yml',
                     'stylish',
                     'tests/fixtures/correct_result.txt'),
        pytest.param('tests/fixtures/filepath1.yml',
                     'tests/fixtures/filepath2.yml',
                     'plain',
                     'tests/fixtures/correct_result_plain.txt'),
        pytest.param('tests/fixtures/filepath1.json',
                     'tests/fixtures/filepath2.json',
                     'plain',
                     'tests/fixtures/correct_result_plain.txt'),
        pytest.param('tests/fixtures/filepath1.json',
                     'tests/fixtures/filepath2.json',
                     'json',
                     'tests/fixtures/correct_result_json.txt'),
        pytest.param('tests/fixtures/filepath1.json',
                     'tests/fixtures/filepath2.yml',
                     'json',
                     'tests/fixtures/correct_result_json.txt')       
    ]
)
def test_diff(file1, file2, formater, expected):
    result = open(expected, 'r').read()
    assert generate_diff(file1, file2, formater) == result

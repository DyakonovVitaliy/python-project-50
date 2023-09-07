from gendiff.generate_diff import generate_diff

def test_diff():
    result = generate_diff(tests/fixtures/file1.json, tests/fixture/file2.json)
    assert result == str({
    - follow: false
    host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True
    })

    
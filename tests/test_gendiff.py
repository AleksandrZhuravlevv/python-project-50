from gendiff.generate_diff import generate_diff


fl1 = 'tests/fixtures/file1.json'
fl2 = 'tests/fixtures/file2.json'
result1 = 'tests/fixtures/result1.txt'
read_result1 = open(result1, 'r')

fl1_yaml = 'tests/fixtures/file1.yml'
fl2_yaml = 'tests/fixtures/file2.yml'
yaml_result = open('tests/fixtures/result2.txt', 'r')

stylish_nested1 = 'tests/fixtures/nested1.json'
stylish_nested2 = 'tests/fixtures/nested2.json'
stylish_nested_result = open('tests/fixtures/nested_result.txt', 'r')


def test_gendiff_flat_json():
    assert generate_diff(fl1, fl2) == read_result1.read()


def test_gendiff_flat_yaml():
    assert generate_diff(fl1_yaml, fl2_yaml) == yaml_result.read()


def test_stylish_nested():
    assert generate_diff(stylish_nested1, stylish_nested2) == stylish_nested_result.read()

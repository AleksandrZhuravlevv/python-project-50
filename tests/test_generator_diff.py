from gendiff.generator_diff import generate_diff


def test_generate_stylish():
    diff_json_stylish = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", "stylish"
    )
    result_true_stylish = open("tests/fixtures/result_true_stylish.txt").read()

    assert diff_json_stylish == result_true_stylish


def test_generate_plain():
    diff_json_plain = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", "plain"
    )
    result_true_plain = open("tests/fixtures/result_true_plain.txt").read()

    assert diff_json_plain == result_true_plain


def test_generate_json():
    diff_json_json = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", "json"
    )
    result_true_json = open("tests/fixtures/result_true_json.json").read()

    assert diff_json_json == result_true_json

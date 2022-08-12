from pytest import param


def test_clean_filepath():
    arguments = "filepath, filename_only, expected_output"
    params = [
        param(
            "test.py",
            False,
            "test.py",
            id="filename as input"
        ),
        param(
            "/test.js",
            False,
            "test.js",
            id="filename with forward slash"
        ),
        param(
            r"\test.js",
            False,
            "test.js",
            id="filename with backward slash"
        ),
        param(
            r"./test.js",
            False,
            "test.js",
            id="filename with dot slash"
        ),
        param(
            r"root/test.js",
            False,
            "root/test.js",
            id="filepath"
        ),
        param(
            r"./root/test.js",
            False,
            "root/test.js",
            id="filepath with dot slash"
        ),
        param(
            r"\root/test.js",
            False,
            "root/test.js",
            id="filepath with back slash"
        ),
        param(
            r"root/test.js",
            True,
            "test.js",
            id="filename only"
        ),
        param(
            r"./root/test.js",
            True,
            "test.js",
            id="filename only with dot slash"
        ),
        param(
            r"root/sub/test.js",
            True,
            "test.js",
            id="filename only with sub-directory"
        ),
    ]
    return arguments, params

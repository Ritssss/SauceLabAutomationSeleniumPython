def assert_equal(actual, expected, message="Values are not equal"):
    """Assert that two values are equal"""
    assert actual == expected, f"{message}. Expected: {expected}, Actual: {actual}"


def assert_not_equal(actual, expected, message="Values are equal but should not be"):
    """Assert that two values are not equal"""
    assert actual != expected, f"{message}. Expected: {expected}, Actual: {actual}"


def assert_true(condition, message="Condition is not true"):
    """Assert that a condition is true"""
    assert condition, message


def assert_false(condition, message="Condition is not false"):
    """Assert that a condition is false"""
    assert not condition, message


def assert_contains(text, substring, message="Substring not found in text"):
    """Assert that a substring is contained in text"""
    assert substring in text, f"{message}. Text: '{text}', Substring: '{substring}'"


def assert_not_contains(text, substring, message="Substring found in text but should not be"):
    """Assert that a substring is not contained in text"""
    assert substring not in text, f"{message}. Text: '{text}', Substring: '{substring}'"


def assert_element_present(element, message="Element is not present"):
    """Assert that an element is present"""
    assert element is not None, message


def assert_element_text(element, expected_text, message="Element text does not match"):
    """Assert that an element's text matches expected text"""
    actual_text = element.text
    assert actual_text == expected_text, f"{message}. Expected: {expected_text}, Actual: {actual_text}"
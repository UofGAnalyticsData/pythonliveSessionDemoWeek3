from helpfulfuncs import string_funcs

def test_add_ed_ODL():
    test_string = "ODL"
    expected_result = "ODLed"
    result = string_funcs.add_ed(test_string)
    assert result  == expected_result

def test_add_ed_ODLed():
    test_string = "ODLed"
    expected_result = "ODLed"
    result = string_funcs.add_ed(test_string)
    assert result  == expected_result

def test_add_ed_ODLED():
    test_string = "ODLED"
    expected_result = "ODLED"
    result = string_funcs.add_ed(test_string)
    assert result  == expected_result


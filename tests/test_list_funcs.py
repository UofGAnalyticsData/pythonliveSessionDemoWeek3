from helpfulfuncs import list_funcs

def test_is_sorted_sorted_list():
    test_list = [1, 2, 3, 4, 5]
    expected_result = True
    result = list_funcs.is_sorted(test_list)
    assert result == expected_result

def test_is_sorted_unsorted_list():
    test_list = [1, 3, 2, 4, 5]
    expected_result = False
    result = list_funcs.is_sorted(test_list)
    assert result == expected_result

def test_is_sorted_empty_list():
    test_list = []
    expected_result = True
    result = list_funcs.is_sorted(test_list)
    assert result == expected_result

def test_is_sorted_single_element():
    test_list = [7]
    expected_result = True
    result = list_funcs.is_sorted(test_list)
    assert result == expected_result

def test_is_sorted_duplicates():
    test_list = [2, 2, 3, 3, 4, 4]
    expected_result = True
    result = list_funcs.is_sorted(test_list)
    assert result == expected_result

from fuggveny import add_params, number_of_spaces, average


def test_add_params():
    result = add_params(2, 3)
    assert result == 5

def test_add_params_negative():
    result = add_params(-5, -6)
    assert result == -11

def test_number_of_spaces_two():
    result=number_of_spaces("Ez egy szoveg")
    assert result == 2

def test_number_of_spaces_no():
    result=number_of_spaces("Ezegyszoveg")
    assert result == 0

def test_number_of_spaces_blank():
    result=number_of_spaces("")
    assert result == 0

def test_average_1_10():
    result = average([1, 9])
    assert result == 5

def test_average_none():
    result = average([])
    assert result is None

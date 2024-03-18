from app.internal.two_list_sum import two_list_sum, two_list_sum_optimized
from app.models.inputpayload import InputPayload


def test_two_list_sum_true():
    """
    GIVEN a function and input parameter that are known to be successfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is valid
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=10)
    result = two_list_sum(inputpayload)
    assert result == True


def test_two_list_sum_false():
    """
    GIVEN a function and input parameter that are known to be unsuccessfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is wrong
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=300)

    result = two_list_sum(inputpayload)
    assert result == False


def test_two_list_sum_optimized_true():
    """
    GIVEN a function and input parameter that are known to be successfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is valid
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=10)
    result = two_list_sum_optimized(inputpayload)
    assert result == True


def test_two_list_sum_optimized_false():
    """
    GIVEN a function and input parameter that are known to be unsuccessfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is wrong
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=300)

    result = two_list_sum_optimized(inputpayload)
    assert result == False

from app.internal.multiple_subset_sum import subset_sum_recursive
from app.models.inputpayload import InputPayload


def test_subset_sum_recursive_true():
    """
    GIVEN a function and input parameter that are known to be successfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is valid
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=10)
    result = subset_sum_recursive(inputpayload)
    assert result == True


def test_subset_sum_recursive_false():
    """
    GIVEN a function and input parameter that are known to be unsuccessfully calculated
    WHEN the 'subset_sum_recursive' function is being called
    THEN check if the response is wrong
    """

    inputpayload = InputPayload(list_a=[3, 5, 7], list_b=[3, 5, 7], target=300)

    result = subset_sum_recursive(inputpayload)
    assert result == False

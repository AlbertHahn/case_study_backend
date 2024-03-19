from app.internal.two_list_sum import two_list_sum
from app.models.models import TwoListTarget


def test_two_list_sum_true():
    """
    GIVEN a function and input parameter that are known to be successfully calculated
    WHEN the 'two_list_sum' function is being called
    THEN check if the response is valid
    """

    two_list_target = TwoListTarget(list_a=[3, 5, 7], list_b=[3, 5, 7], target=10)
    result = two_list_sum(two_list_target)
    assert result == True


def test_two_list_sum_false():
    """
    GIVEN a function and input parameter that are known to be unsuccessfully calculated
    WHEN the 'two_list_sum' function is being called
    THEN check if the response is wrong
    """

    two_list_target = TwoListTarget(list_a=[3, 5, 7], list_b=[3, 5, 7], target=300)

    result = two_list_sum(two_list_target)
    assert result == False

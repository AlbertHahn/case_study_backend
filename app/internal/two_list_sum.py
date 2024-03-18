from app.models.models import InputPayload

# Recursive calculation of the subset sum problem


def two_list_sum(inputpayload: InputPayload):
    """
    This function has a time complexity of O(n+m)
    """
    list_a = inputpayload.list_a
    set_b = set(inputpayload.list_b)
    target = inputpayload.target

    # Base cases
    if target == 0:
        return True

    for a in list_a:
        if target - a in set_b:
            return True

    return False

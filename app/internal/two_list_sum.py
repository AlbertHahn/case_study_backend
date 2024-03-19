from app.models.models import TwoListTarget


def two_list_sum(twolisttarget: TwoListTarget):
    """
    This function has a time complexity of O(n+m)
    """
    set_a = set(twolisttarget.list_a)
    set_b = set(twolisttarget.list_b)
    target = twolisttarget.target

    # Base cases
    if target == 0:
        return True

    for a in set_a:
        if target - a in set_b:
            return True

    return False

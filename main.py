def disjoints(
        p1: list,
        p2: list,
):
    return


def excesses(
        p1: list,
        p2: list,
):
    return


def average_weight_differences(p1, p2):
    return


def compatibility_distance(
        p1: list,
        p2: list,
        c1: int=1,
        c2: int=1,
        c3: int=1):
    """
    :param p1: parent genome 1
    :param p2: parent genome 2
    :param c1: coefficient 1 (multiple of disjoints)
    :param c2: coefficient 2 (multiple of excesses)
    :param c3: coefficient 3 (multiple of average weight differences)
    :return:
    """
    larger_p = p1 if len(p1) > len(p2) else p2

    dis = disjoints(p1, p2) / len(larger_p) * c1
    exc = excesses(p1, p2) / len(larger_p) * c2
    awd = average_weight_differences(p1, p2) * c3

    return dis + exc + awd

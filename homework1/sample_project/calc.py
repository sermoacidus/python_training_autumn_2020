def check_power_of_2(a: int) -> bool:
    """
    Checking if a given int is a power of 2
    """
    if a == 0:
        return False
    return not (bool(a & (a - 1)))

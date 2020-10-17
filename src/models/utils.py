
def get_account_id(account_id, check_only=False):
    """
    Converts int to str, checks if str has dashes. Returns 10 chars str or raises error
    :check_only - if True, returns None instead of Error

    """

    if isinstance(account_id, int) and len(str(account_id)) == 10:
        return str(account_id)
    if isinstance(account_id, str) and len(account_id.replace("-", "")) == 10:
        return account_id.replace("-", "")
    if check_only:
        return None
    raise ValueError(f"Couldn't recognize account id from {account_id}")


def choose_account_id(account_id, test_account_id):
    """
    Picks actual account id or a test one. Check both of the accounts ids first.
    Raises value if both are incorrect
    """

    if not get_account_id(account_id, True) and not get_account_id(test_account_id, True):
        raise ValueError("Couldn't pick an account id ")
    return get_account_id(account_id, True) or get_account_id(test_account_id, True)


def micros_to_currency(micros):
    return micros / 1000000.0


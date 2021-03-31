
def get_int(msg, minimum_value, default_value=0):
    """
    The user needs to digit an integer number to return an integer value that is greater than minimum value or press Enter to return the default value
    :param msg: str
    :param minimum_value: int
    :param default_value: int
    :return: value: int
    """
    while True:
        try:
            user_input = input(msg)
            if not user_input and default_value is not None:
                return default_value
            value = int(user_input)
            if value < minimum_value:
                print(f'Must be >= {minimum_value}')
            else:
                return value
        except ValueError as err:
            print(err)

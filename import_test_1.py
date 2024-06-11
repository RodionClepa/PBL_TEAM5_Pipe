def split_period(string: str):
    if isinstance(string, str):
        return string.split('.')
    raise Exception("Input must be a string")
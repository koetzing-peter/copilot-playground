def regex_password_checker(password: str) -> bool:
    """
    Check if the password contains at least one special character,
    one uppercase letter, one lowercase letter, one digit, and is
    at least 8 characters long.
    """
    import re
    pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    if pattern.fullmatch(password):
        return True
    return False

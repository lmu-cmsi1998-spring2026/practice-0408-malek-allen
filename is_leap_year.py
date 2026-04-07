def is_leap_year(year: int) -> bool:
    """
    Any given year is a leap year if:
        - It's divisible by 4, but not 100 (unless it's divisible by 400)
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    print(is_leap_year(2000))  # True
    print(is_leap_year(2001))  # False
    print(is_leap_year(2002))  # False
    print(is_leap_year(1900))  # False
    print(is_leap_year(2004))  # True
    print(is_leap_year(2001))  # False
    print(is_leap_year(2024))  # True
    print(is_leap_year(2026))  # False


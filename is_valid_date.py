from days_in_month import days_in_month

def is_valid_date(year: int, month: int, day: int) -> bool:
    if month < 1 or month > 12:
        return False

    max_day = days_in_month(year, month)
    if max_day is None:
        return False

    return 1 <= day <= max_day


if __name__ == "__main__":
    print(is_valid_date(2020, 2, 29))  # True
    print(is_valid_date(2021, 2, 29))  # False
    print(is_valid_date(2021, 4, 31))  # False
    print(is_valid_date(2021, 12, 31)) # True
    print(is_valid_date(2026, 4, 30)) # True
    print(is_valid_date(2021, 13, 1))  # False
    print(is_valid_date(2021, 0, 10))   # False
    print(is_valid_date(2021, 1, 0))    # False
    print(is_valid_date(2020, 13, 29)) #False

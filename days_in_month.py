from is_leap_year import is_leap_year


def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return None


if __name__ == "__main__":
    print(days_in_month(1938, 6)) # 30
    print(days_in_month(3020, 12)) # 31
    print(days_in_month(2, 4)) # 30
    print(days_in_month(2000, 2)) # 29
    print(days_in_month(1900, 2)) # 28
    print(days_in_month(1908, 2)) # 29
    print(days_in_month(1909, 2)) # 28

from sys import argv
from is_valid_date import is_valid_date

#day counter method
def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    current_year = year1
    current_month = month1
    current_day = day1
    current_day_count = 0

    while (current_year, current_month, current_day) != (year2, month2, day2):
        current_day_count += 1
        current_day += 1

        if not is_valid_date(current_year, current_month, current_day):
            current_day = 1
            current_month += 1

            if not is_valid_date(current_year, current_month, current_day):
                current_month = 1
                current_year += 1

    return current_day_count #answer


if __name__ == "__main__":
    if len(argv) != 7:
        print("Usage: python day_counter.py <year1> <month1> <day1> <year2> <month2> <day2>")
    else:
        year1, month1, day1, year2, month2, day2 = map(int, argv[1:])

        if (year1, month1, day1) > (year2, month2, day2):
            print(f'The number of days is: {day_counter(year2, month2, day2, year1, month1, day1)}')
        else:
            print(f'The number of days is: {day_counter(year1, month1, day1, year2, month2, day2)}')

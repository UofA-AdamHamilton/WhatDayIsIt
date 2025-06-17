"""
implementation of John Horton Conway's Doomsday algorithm.
"""

day_dictionary = {0: 'Sunday',
                  1: 'Monday',
                  2: 'Tuesday',
                  3: 'Wednesday',
                  4: 'Thursday',
                  5: 'Friday',
                  6: 'Saturday'}

abbreviation_list = [['january', 'jan'],
                     ['february', 'feb'],
                     ['march', 'mar'],
                     ['april', 'apr'],
                     ['may', 'may'],
                     ['june', 'jun'],
                     ['july', 'jul'],
                     ['august', 'aug'],
                     ['september', 'sept'],
                     ['october', 'oct'],
                     ['november', 'nov'],
                     ['december', 'dec']]


def doomsday_year(year: int, verbose: bool = False):
    """
    :param verbose: Boolean that prints out our intermediate workings out
    :param year: integer that represents the year in question in
    :return: day of the week as an integer mod 7
    """
    # 2024 Doomsday is a Thursday (4)
    # count the number of leap years from 2024
    years_since_last_leap_year = year % 4
    last_leap_year = year - years_since_last_leap_year
    leap_years_since_2024 = (2024 - last_leap_year) // 4
    day_of_week_key = (leap_years_since_2024 * 2 + years_since_last_leap_year + 4) % 7

    if verbose:
        print('years since last leap year')
        print(years_since_last_leap_year)
        print('last_leap_year')
        print(last_leap_year)
        print('leap_years_since_2024')
        print(leap_years_since_2024)
        print('day_of_week_key')
        print(day_dictionary[day_of_week_key], 'for year ', year)
        print(' ')
    pass


def month_number(month_string: str, abbreviations=abbreviation_list):
    """
    :param abbreviations:
    :param month_string:
    :param string:
    :return:
    """
    if abbreviations is None:
        abbreviations = abbreviation_list
    for i in range(len(abbreviations)):
        if month_string.lower() in abbreviations[i]:
            return i
    raise Exception('cannot recognise month')


def doomsday_day(day: int, month: int | str, doomsday):
    """
    Given the day and the mon
    :param day:
    :param month:
    :param doomsday:
    :return:
    """
    if isinstance(month, str):
        print('strign')
    elif isinstance(month, int):
        print(month)
    elif isinstance(month, float):
        print(int(month))
    else:
        raise Exception(' input month is not in acceptable format')
    pass


if __name__ == '__main__':
    print(doomsday_year(2021, verbose=True))
    print(doomsday_year(2023, verbose=True))
    print(doomsday_year(2000, verbose=True))
    print(doomsday_year(2042, verbose=True))

    print(doomsday_day(3, 'april', 3))
    print(doomsday_day(3, 4, 3))
    print(doomsday_day(3, 4.0, 3))

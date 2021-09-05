# Author: Oscar Wellner, 21144192
# Date: 2021-09-02
# About:    This Python script will ask the User his name, age, and month of birth and returns his name, age and the year
#           when the User will reach a specific age.

from datetime import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'Oktober', 'November', 'December']
AGE_TO_CALCULATE = 100


def get_age(message):
    # Returns the age value from the inputted value, if possible.
    value = input(message)

    if not value.isdigit:
        print(
            f"The inputted value: '{value}' is not a digit. Please try again...")

        return get_age(message)

    value = int(value)

    if value <= 0:
        print(f"No person can be of age: '{value}'. Please, try again...")

        return get_age(message)

    return value


def get_month():
    # Returns the numeric value of the inputted month ( 0 - 11 ).
    month = input('In what month is your birthday? ')

    if month.capitalize() not in MONTHS:
        print(
            f"Inputted value: '{month}' is not a valid month. Please, try again...")

        return get_month()

    return MONTHS.index(month.capitalize())


def calc_year(age, birthday_month):
    # Returns the year in which the age to calculate is reached depending on the provided age.
    current_date = datetime.now()

    years_to_go = AGE_TO_CALCULATE - age

    if current_date.month < birthday_month:
        years_to_go -= 1

    return datetime(current_date.year + years_to_go,
                    current_date.month, current_date.day).year


def main():
    name = input('What is your name? ')
    age = get_age('How old are you? ')
    month_of_birth_int = get_month()
    calculated_year = calc_year(age, month_of_birth_int)

    print(f"\nHello {name}. You are currently {age} years-old.")
    print(
        f"You'll be {AGE_TO_CALCULATE} years-old in the year: {calculated_year}.")


if __name__ == '__main__':
    main()

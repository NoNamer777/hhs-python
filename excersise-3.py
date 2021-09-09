# Author: Oscar Wellner, 21144192
# Date: 2021-09-09
# About:    This Python script will take list a and does the following actions:
#               - Prints all numbers lower than the LOWER_THAN number,
#               - Prints the average from all numbers in a 2 point decimal number,
#               - Prints a new list of all numbers above the calculated average.

LOWER_THAN = 5
A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def print_lower_than():
    # Takes the values in our list that are lower than the LOWER_THAN value and prints them.
    lower_than = []

    for i in A:
        if (i < LOWER_THAN):
            lower_than.append(i)

        if (i > LOWER_THAN):
            break

    print(f'\nThe following number are lower than {LOWER_THAN}: {lower_than}')


def print_average():
    # Calculates, prints, and returns the average value of our list.
    average = sum(A) / len(A)

    print(f'\nThe average for the numbers in the list is: {average:.2f}')

    return average


def print_above_average(average):
    # Creates a new list which will hold all the numbers of our list which are higher than the average of that list.
    above_average = []

    for i in A:
        if (i > average):
            above_average.append(i)

    print(f'\nThe numbers in our list that are above average are: {above_average}')


def main():
    print_lower_than()
    average = print_average()
    print_above_average(average)

    print()


if __name__ == '__main__':
    main()

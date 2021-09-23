# Author: Oscar Wellner, 21144192
# Date: 2021-09-09
# About:    This Python script will ask the User for a number and creates a dictionary from it
#           that is of size n with the following layout { n: n*n, ... }.

def get_number():
    # Determines how many Fibonacci numbers to produce.
    # Catches instances where the user still provides other values than integers.
    amount = input('\nHow large do you want your dictionary to be? (0..) ')

    if not amount.isdigit():
        print(f'The inputted value: {amount} is not a digit. Please try again...')

        return get_number()

    return int(amount)


def create_dict(size):
    # Creates a dictionary following the specifications that are at the top.
    result = dict()

    for n in range(size):
        result[n + 1] = (n + 1) * (n + 1)

    print(f'Created the following dictionary: {result}')


def main():
    number = get_number()
    create_dict(number)


if __name__ == '__main__':
    main()

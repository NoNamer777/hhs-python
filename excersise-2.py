# Author: Oscar Wellner, 21144192
# Date: 2021-09-08
# About:    This Python script will ask the User how many Fibonnaci number must be made.
#           Those numbers will be printed after they've been calculated.

def get_amount_numbers():
    # Determines how many Fibonnaci numbers to produce.
    # Catches instances where the user still provides other values than integers.
    amount = input('\nHow many Fibonnaci numbers must be created? (0..) ')

    if (not amount.isdigit()):
        print(f'The inputted value: {amount} is not a digit. Please try again...')

        return get_amount_numbers()

    return int(amount)


def create_fibonnaci_list(size):
    # Creates the list of Fibonnaci numbers until the list is of the provided size.
    # Also shrinks the size of the list if the user wanted a smaller list.
    a = b = 1
    resulting_list = [a, b]

    while len(resulting_list) < size:
        result_sum = a + b

        resulting_list.append(result_sum)

        a = b
        b = result_sum
    else:
        while len(resulting_list) > size:
            resulting_list.pop()

    return resulting_list


def main():
    amount_of_numbers = get_amount_numbers()
    fibonnaci_numbers = create_fibonnaci_list(amount_of_numbers)

    print(f'Here are your Fibonnaci numbers: {fibonnaci_numbers}\n')


if __name__ == '__main__':
    main()

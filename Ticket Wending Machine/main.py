import numbers


def ask():
    print("Welcome to the ticket vending machine.")
    while True:
        print('[P] - Perfume\n[M] - Medicines\n[C] - Cosmetics')
        try:
            my_product = input('Choose your product: ').upper()
            ['P', 'M', 'C'].index(my_product)
        except ValueError:
            print("That is not a valid option")
        else:
            break

    numbers.decorator(my_product)


def start():

    while True:
        ask()
        try:
            another_ticket = input('Do you want another ticket? [Y] [N]').upper()
            ['Y', 'N'].index(another_ticket)
        except ValueError:
            print('Not a valid option')
        else:
            if another_ticket == 'N':
                print('Thank you for visiting!!!')
                break


start()

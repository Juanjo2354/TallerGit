from operations import add, minus, mult, div, power, module


def game():
    score = 0
    while True:
        print(
            '======== Menu ========'
            '\n1. Add'
            '\n2. Minus'
            '\n3. Multiplication'
            '\n4. Division'
            '\n5. Power'
            '\n6. Module'
            '\n0. Exit'
            )
        option = int(input('\nChoice an option: '))

        if option == 0:
            break

        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = add(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')

        if option == 2:
            result = minus(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')

        if option == 3:
            result = mult(num_1, num_2)
        if result == answer:
            score += 2
            print('Correct!!')
        else:
            print('Incorrect')

        if option == 4:
            result = div(num_1, num_2)
        if result == answer:
            score += 2
            print('Correct!!')
        else:
            print('Incorrect')

        if option == 5:
            result = power(num_1, num_2)
        if result == answer:
            score += 4
            print('Correct!!')
        else:
            print('Incorrect')

        if option == 6:
            result = module(num_1, num_2)
        if result == answer:
            score += 4
            print('Correct!!')
        else:
            print('Incorrect')

    print(
        f'======== Game Over ========'
        f'\nYou score is {score}'
        '\nKeep going!'
        )


game()

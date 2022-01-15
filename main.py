"""
Crappy keersommen
"""
import random


def main(max_tafel):
    """
    Main
    :param max_tafel:
        String
    :return:
        None
    """
    sommen = []
    column = 0
    row = 0
    while True:
        som = '{:2} x {:2} = '.format(
            random.randrange(1, 11), random.randrange(1, max_tafel + 1))
        if som not in sommen:
            sommen.append(som)
        if len(sommen) == 10*max_tafel:
            break


    for dit in sommen:
        print('{}'.format(dit), end="    ")
        column += 1

        if column == 4:
            print('')
            column = 0
            row += 1

        if row == 5:
            print('')
            row = 0


if __name__ == '__main__':
    main(20)

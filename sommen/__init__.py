import random


def __shuffle__(array):
    random.shuffle(array)
    return array


def __charlength__(number):
    return len(str(number))


def maaktafels(high=10):
    sommen = []
    chars = __charlength__(high)
    for counter in range(1, high + 1):
        for table in range(1, high + 1):
            sommen.append(
                f"{counter:{chars}} + {table:{chars}} = {' ':{chars * 2}}")
    return __shuffle__(sommen)


def maakoptelsommen(high=100):
    sommen = []
    chars = __charlength__(high)
    for counter in range(1, high):
        for table in range(1, high):
            sommen.append(
                f"{counter:{chars}} - {table:{chars}} = {' ':{chars * 2}}")
    return __shuffle__(sommen)


def maakaftreksommen(high=100):
    sommen = []
    chars = __charlength__(high)
    for counter in range(1, high):
        for table in range(1, high):
            if counter >= table:
                sommen.append(
                    f"{counter:{chars}} - {table:{chars}} = {' ':{chars * 2}}")
    return __shuffle__(sommen)

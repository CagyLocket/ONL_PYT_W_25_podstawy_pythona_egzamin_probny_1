names = ["Andrzej", "Henryk", "Wiktoria", "Alicja", "Cezary", "Barbara", "Natalia"]


def name_sorter(names):
    """Sort names and separate male and female names.

    :param list names: list of names
    :rtype: dict
    :return: dict with female and male names.
    """
    female = sorted([x for x in names if x[-1] == 'a'])
    male = sorted([x for x in names if x[-1] != 'a'])

    dict_names = {
        'female': [],
        'male': []
    }

    dict_names['female'].append(female)
    dict_names['male'].append(male)

    return dict_names


if __name__ == '__main__':
    print(name_sorter(names))








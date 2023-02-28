import random


def roll(dices, dice_type=6, modifier=0):
    """Roll dices and add a modifier to a final result

    :param int dices: number of dices
    :param int dice_type: dice type, default is 6
    :param int modifier: modifier value
    :rtype: int
    :return: value of dice roll modified by a modifier value
    """
    possible_dices = [3, 4, 6, 8, 10, 12, 100]

    if dice_type not in possible_dices:
        raise Exception("No such dice!")
    else:
        result = sum(random.randint(1, dice_type) for _ in range(dices)) + modifier
        return result


if __name__ == '__main__':
    print(roll(2))
    print(roll(2, 10, 20))
    print(roll(3, 6, -3))
    print(roll(2, 1, 20))


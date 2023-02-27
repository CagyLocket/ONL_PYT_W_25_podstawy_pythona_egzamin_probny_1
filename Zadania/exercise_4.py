def div(int_a, int_b):
    """Fetch 2 int numbers as starting and closing points for a range and gives a list of numbers that are divided
    by 2 but not by 3.

    :param int_a: int as starting point of a range of numbers
    :param int_b: int as closing point of a range of numbers
    :return: list of numbers that are divided by 2 but not by 3
    """
    output_list = []
    for i in range(int_a, int_b+1):
        if i % 2 == 0 and i % 3 != 0:
            output_list.append(i)
    return output_list


print(div(1, 20))




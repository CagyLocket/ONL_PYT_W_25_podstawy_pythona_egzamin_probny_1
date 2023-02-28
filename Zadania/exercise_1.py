def shorten(input_string):
    """Splits a long string by space and joins capitalized first letters from each string item together.

    :param str input_string: some text ex. 'Don't repeat yourself'
    :rtype: str
    :return: shortened text as abbreviation from capitalized first letters of each string item"""

    output_string = ''.join([x[:1].upper() for x in input_string.split(' ')])

    return output_string


if __name__ == '__main__':
    shortened = shorten("Don't repeat yourself")
    print(shortened)

    shortened = shorten("Read the fine manual")
    print(shortened)

    shortened = shorten("All terrain armoured transport")
    print(shortened)




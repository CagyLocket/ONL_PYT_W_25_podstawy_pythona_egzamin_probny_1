def check_palindrome(input_string):
    """Fetch a long text string and check if it is a palindrome.

    :param str input_string: ex. "Kobyła ma mały bok"
    :rtype: bool
    :return: True if the string is a palindrome, False if it is not.
    """
    expression = input_string.upper().replace(" ", "")
    if expression == expression[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_palindrome('Kajak'))
    print(check_palindrome('Kajak w kajak'))
    print(check_palindrome('radar'))
    print(check_palindrome('Kajak 54 kajak'))
    print(check_palindrome('Kobyła ma mały bok'))


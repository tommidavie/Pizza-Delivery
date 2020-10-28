def validate_index(m, min, max):

    """
    The function gathers the user input (which will be an integer when returned) and tests it
    comprehensively. The function will repeat (loop) until the user has entered an appropriate answer.

    :param m: str
    :param min: int
    :param max: int
    :return: int
    """

    while True:
        try:
            change = int(input(m))
        except ValueError:
            print("Your entry must be a number. Please try again.")
            continue
        if change <= min:
            print("Your entry is too small, it must be above 0. Please try again.")
        elif change > max:
            print("Your entry is too big, or you have entered more than one number. \n"
                  "It must be {} or below. Please try again.".format(max))
        else:
            return change


def validate_integer(m, min, max):
    """
    The function gathers the user input (which will be an integer when returned) and tests it
    comprehensively. The function will repeat (loop) until the user has entered an appropriate answer.

    :param m: str
    :param min: int
    :param max: int
    :return: int
    """

    while True:
        try:
            change = int(input(m))
        except ValueError:
            print("Your entry must be a number. Please try again.")
            continue
        if change <= min:
            print("Your entry is too small, it must be above 0. Please try again.")
        elif change > max:
            print("Your entry is too big, it must not be any more than 5. Please try again.")
        else:
            return change


def validate_string(m, min, max):

    """
    The function gathers the user input (which is a string when returned) and tests it
    comprehensively. The function will repeat (loop) until the user has entered an appropriate answer.

    :param m: str
    :param min: int
    :param max: int
    :return: str
    """

    while True:

        user_input = input(m).upper()

        if len(user_input) < min:
            print("Your answer is too short. Please ensure you have typed in an appropriate response.")
        elif len(user_input) > max:
            print("Your answer is too long. Please ensure you have typed in an appropriate response.")
        else:
            return user_input


if __name__ == "__main__":
    #change = validate_integer("Please enter your number: ", 0, 5)
    #print(change)
    my_str= validate_string("Please input anything: -> ", 1, 5)
    print(my_str)
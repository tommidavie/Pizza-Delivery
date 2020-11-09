def validate_index(m, min, max):
    """
    Validate the user's index input.

    This checks to see if the user's input is above the
    maximum value or below the minimum value.
    These values are set in the main program.
    It also ensures the user has entered an
    integer (and not a string).
    The user's input is only returned when it has
    met all of these requirements.

    :param m: str
    :param min: int
    :param max: int
    :return: int (the customer's choice of index)
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # The user has entered a string
        try:
            change = int(input(m))
        except ValueError:
            # Error message
            # Inform the user they must enter a number
            # Loop continues
            print("Your entry must be a number. \n"
                  "Please try again.")
            continue
        # The customer has entered a value
        # Below the minimum value
        if change <= min:
            # Error message
            # Loop continues
            print("Your entry is too small, it must be above 0. \n"
                  "Please try again.")
        # The customer has entered a value
        # Above the maximum value
        elif change > max:
            # Error message
            # Loop continues
            print("Your entry is too big, or you have entered more than one number. \n"
                  "It must be {} or below. Please try again.".format(max))
        # The customer has met all of these requirements
        # Their input is returns and the loop ends
        else:
            return change


def validate_integer(m, min, max):
    """
    Validate the user's index input.

    This checks to see if the pizza quantity
    the customer would like ito order
    s above the maximum value or below the value.
    These values are 0 and 5 (suggested
    by the marking schedule).
    It also ensures the user has entered an
    integer (and not a string).
    The user's input is only returned when it has
    met all of these requirements.

    :param m: str
    :param min: int
    :param max: int
    :return: int (the customer's choice of integer)
    (this could be a pizza quantity)
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # The user has entered a string
        try:
            change = int(input(m))
        except ValueError:
            # Error message
            # Inform the user they must enter a number
            # Loop continues
            print("Your entry must be a number. Please try again.")
            continue
        # The customer has entered a value
        # Below the minimum value of 0
        if change <= min:
            print("Your entry is too small, it must be above 0. Please try again.")
        # The customer has entered a value
        # Above the set maximum value of 5
        elif change > max:
            # Error message
            # Loop continues
            print("Your entry is too big. \n"
                  "It must not be any more than 5. Please try again.")
        # The customer has met all of these requirements
        # Their input is returns and the loop ends
        else:
            return change


def validate_string(m, min, max):
    """
    Validate the user's string input.

    This checks to see if the user input
    is between or equal to the maximum value
    and minimum value.
    These values are set in the main program
    and are unique to every string input.
    It also ensures the user has entered a
    string (and not an integer).
    The user's input is only returned when it has
    met all of these requirements.

    :param m: str
    :param min: int
    :param max: int
    :return: str
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # Defines all of the user's input as
        # an uppercase string
        user_input = input(m).upper()
        # Replaces all spaces in the user's input
        # with an enclosed space
        user_input = user_input.replace(" ", "")
        # The customer has entered a value
        # Below the minimum value
        if len(user_input) < min:
            # Error message
            # The loop continues
            print("Your answer is too short. \n"
                  "Please ensure you have entered an appropriate response.")
        # The customer has entered a value
        # Above the maximum value
        elif len(user_input) > max:
            # Error message
            # The loop continues
            print("Your answer is too long. \n"
                  "Please ensure you have entered an appropriate response.")
        # The customer has met all of these requirements
        # Their input is returns and the loop ends
        else:
            return user_input


def validate_names_address(m, min, max):
    """
    Validate the user's name and address.

    This checks to see if the user's name and address
    is between or equal to the maximum value
    and minimum value.
    These values are set in the main program.
    It also ensures the user has entered a
    string (and not an integer).
    The name/address is only returned when it has
    met all of these requirements.

    :param m: str
    :param min: int
    :param max: int
    :return: str (the user's name
    or address)
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # Defines the user's input as
        # an uppercase string
        user_input = input(m).upper()
        # The customer has entered a value
        # Below the minimum value
        if len(user_input) < min:
            # Error message
            # Loop continues
            print("Your answer is too short. \n"
                  "Please ensure you have entered an appropriate response.")
        # The customer has entered a value
        # Above the maximum value
        elif len(user_input) > max:
            # Error message
            # Loop continues
            print("Your answer is too long. \n"
                  "Please ensure you have entered an appropriate response.")
        # The customer has met all of these requirements
        # Their input is returns and the loop ends
        else:
            return user_input


def validate_y_and_n(m, min, max):
    """
    Validate the user's yes and no responses.

    This checks to see if the user has entered
    a value defined in the char list below.
    It also ensures the user has entered a
    string (and not an integer).
    The user's response is only returned if they
    have entered a letter from the char list.

    :param m: str
    :param min: int
    :param max: int
    :return: str ('Y' 'y' or 'N' 'n')
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # Defines the user's input as
        # an uppercase string
        user_input = input(m).upper()
        # Replaces all spaces in the user's input
        # with an enclosed space
        user_input = user_input.replace(" ", "")
        # The user enters a letter from the
        # appropriate char list
        if user_input in ["Y", "y", "N", "n"]:
            # Their input is returned
            # Loop ends
            return user_input
        # The user enters an input not defined in the char list
        # Error message
        # Loop continues
        else:
            print("You have not entered an appropriate answer. \n"
                  "Please enter a 'y' for 'yes' or an 'n' for 'no'.")


def validate_u_and_d(m, min, max):
    """
    Validate the user's choice of delivery.

    This checks to see if the user has entered
    a value defined in the char list below.
    It also ensures the user has entered a
    string (and not an integer).
    The user's response is only returned if they
    have entered a letter from the char list.

    :param m: str
    :param min: int
    :param max: int
    :return: str ('U' 'u' or 'D' 'd')
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # Defines the user's input as
        # an uppercase string
        user_input = input(m).upper()
        # Replaces all spaces in the user's input
        # with an enclosed space
        user_input = user_input.replace(" ", "")
        # The user enters a letter from the
        # appropriate char list
        if user_input in ["U", "u", "D", "d"]:
            # Their input is returned
            # Loop ends
            return user_input
        # The user enters an input not defined in the char list
        # Error message
        # Loop continues
        else:
            print("You have not entered an appropriate answer.\n"
                  "You must enter either 'U' for Uber Eats or 'D' for Deliver Easy.")


def validate_p_and_d(m, min, max):
    """
    Validate the user's pick-up/delivery choice

    This checks to see if the user has entered
    a value defined in the char list below.
    It also ensures the user has entered a
    string (and not an integer).
    The user's response is only returned if they
    have entered a letter from the char list.

    :param m: str
    :param min: int
    :param max: int
    :return: str ('P' 'p' or 'D' 'd')
    """
    # Begins a validation loop
    # This loop will continue until the user enters
    # an appropriate answer
    while True:
        # Defines the user's input as
        # an uppercase string
        user_input = input(m).upper()
        # Replaces all spaces in the user's input
        # with an enclosed space
        user_input = user_input.replace(" ", "")
        # The user enters a letter from the
        # appropriate char list
        if user_input in ["P", "p", "D", "d"]:
            # Their input is returned
            # Loop ends
            return user_input
        # The user enters an input not defined in the char list
        # Error message
        # Loop continues
        else:
            print("You have not entered an appropriate answer.\n"
                  "You must enter either 'P' for pick-up or 'D' for Delivery.")


# Testing condition used before I integrate the
# validations into my main file
if __name__ == "__main__":
    #change = validate_integer("Please enter your number: ", 0, 5)
    #print(change)
    my_str = validate_string("Please input anything: -> ", 1, 5)
    print(my_str)

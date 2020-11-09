"""This is a pizza delivery program."""

# This imports validations functions I have created in a separate file
from validations import validate_index
from validations import validate_integer
from validations import validate_string
from validations import validate_y_and_n
from validations import validate_u_and_d
from validations import validate_p_and_d
from validations import validate_names_address


def print_pizza_menu(p):
    """Print the pizza list with indexes.

    This gathers and prints the pizza flavours
    and their corresponding prices and indexes.

    :param p: List (with pizzas prices and names)
    List is a multidimensional list of [ [int, str] ]
    :return: None
    """
    print("PIZZA MENU:")
    print(100 * "-")
    output = "{:5} {:27}  {:1}".format("", "FLAVOUR:", "PRICE:")
    print(output)
    print(100 * "-")
    # A loop of fixed length
    for i in range(0, len(p)):
        # Prints the pizza list with index numbers, pizza names and prices
        # The indexes are printed as 'i+1' so the numbers
        # print from 1 instead of 0
        output = "{:3} : {:27} ${:1}0".format(i+1, p[i][0], p[i][1])
        print(output)


def scan_customer_list(c, name):
    """Scan the customer list for like values.

    This searches the customer's list/order for
    a duplicate pizza. It also allows the customer
    to update their list/order if two identical
    pizza flavours are found.

    :param c: List (with pizza names which have
    been selected by the customer and their prices)
    List is a multidimensional list of [ [int, str] ]
    :param name: Str (Pizza Flavour the customer
    has entered)
    :return: Bool
    """
    # A loop of fixed length
    for i in range(0, len(c)):
        # Scan the list to see if the pizza flavour the customer has entered
        # matches one already in their list
        if name == c[i][1]:
            # Inform the user they already have this
            # pizza flavour in their list
            # Ask the user if they would like to update this pizza
            message = "You already have this pizza flavour in your list. \n"\
                      "Would you like to update it? \n" \
                      "Press 'y' for yes and 'n' for no: "
            update = validate_y_and_n(message, 1, 1)
            # The user selects to update their list
            if update in ["Y", "y"]:
                # Requests the new quantity of
                # pizzas the user would like to order
                updated_choice = validate_integer("Please enter the new quantity of \n"
                                                  "{} pizzas you would like: "
                                                  .format(c[i][1]), 0, 5)
                print("You now have {} {} pizzas"
                      .format(updated_choice, c[i][1]))
                # Replace the User's old pizza
                # quantity with their updated choice
                c[i][0] = updated_choice
                # End of the conditional statement
                return True
            # The user selects to make no updates
            elif update in ["N", "n"]:
                # No changes are made to the customer's order
                print("Your {} pizzas have not been updated"
                      .format(c[i][1]))
                # End of the conditional statement
                return True
            # The user enters an inappropriate answer
            else:
                print("Please enter either 'y' for yes or 'n' for no")
    # The function is terminated
    return None


def customer_order(p, r):
    """Ask the customer for their pizza order.

    This asks the customer for the pizza flavours and
    quantities they would like to order. It sends this information
    to the review function where it can be formatted and printed.

    :param p: List (with name and prices of the pizzas)
    List is a multidimensional list of [ [int, str] ]
    :param r: List (with pizza names and prices which
    have been selected by the customer)
    List is a multidimensional list of [ [int, str] ]
    :return: None
    """
    print_pizza_menu(p)
    print(100*"-")
    # The index/pizza the user would like to order
    index_number = validate_index("Please chose the index number \n"
                                  "of the pizza you would like to order: ", 0, len(p))
    # Defines the index number (i_no) as one less than
    # the user's index input (to ensure indexes begin at 1, not 0)
    i_no = index_number - 1
    # Defines the 'name' variable as the
    # pizza flavour of the index the user has selected
    name = p[i_no][0]
    # Passes the 'name' variable into the
    # 'scan_customer_list' function
    # Scans to see if the customer already has
    # this value in their list
    check = scan_customer_list(r, name)
    # A duplicate is found and the
    # 'scan_customer_list' function is called
    if check:
        print(100*"-")
    # No duplicates are found in the 'customer_list'
    else:
        # The quantity of pizzas the user would like to order
        amount = validate_integer("How many {} pizzas would you like to order: "
                                  .format(p[i_no][0]), 0, 5)
        update1 = "{} {} pizzas have now been added to your order"\
            .format(amount, p[i_no][0])
        print(update1)
        # Cost of one pizza
        pizza_cost = p[i_no][1]
        # Identifying the quantity, flavour and cost of a singular pizza
        temp_pizzas = [amount, p[i_no][0], pizza_cost]
        # Inserting pizza information into the customer list
        # (found in the main menu)
        r.append(temp_pizzas)


def review_customer_order(r, d):
    """Print the current customer order status.

    This formats and prints the cost, quantity
    and flavour of pizzas in the customer's order,
    factoring GST and delivery charge.
    Every time a new pizza is added/taken away these values update.

    :param r: List (with pizza names and prices
    which have been selected by the customer)
    List is a multidimensional list of [ [int, str] ]
    :param d: Int (delivery charge)
    :return: None
    """
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:5} {:<9}  {:<51}  {:<45}"\
        .format("", "Qty", "Flavour", "Cost")
    print(output)
    # Defines the total quantity, costs and GST's of the pizzas
    # as $0 before the loop begins
    total_cost = 0
    total_cost_2 = 0
    gst = 0
    total_quantity = 0
    # A loop of fixed length
    for i in range(0, len(r)):
        # Multiplying the quantity and price of a singular pizza,
        # resulting in it's cost
        cost = r[i][0]*r[i][2]
        # Adding the pizza cost to the total cost every time the
        # loop is repeated/a new pizza(s) is added
        total_cost += r[i][0]*r[i][2]
        # Calculating the GST and updating it every time the
        # loop in repeated/a new pizza(s) is added
        gst = total_cost*0.15
        # Total cost is equal to the total price,
        # plus GST and delivery charge
        total_cost_2 = total_cost + gst + d
        # Adding a pizza quantity to the total quantity,
        # every time the function is repeated/a new pizza(s) is added
        total_quantity += r[i][0]
        # Printing the customer's order in receipt format
        output = "{:3} : {:<8} : {:<25} @ a price of ${:<10} : ${}0"\
            .format(i+1, r[i][0], r[i][1], r[i][2], cost)
        print(output)
    print(100*"-")
    # Print concluding information
    total_1 = "{:>76} {:<10}".format("Total Pizzas:", total_quantity)
    print(total_1)
    total_2 = "{:>76} ${:<10.2f}".format("Total Cost:", total_cost_2)
    print(total_2)
    total_3 = "{:>76} ${:<10.2f}".format("GST:", gst)
    print(total_3)
    total_4 = "{:>76} ${:<10.2f}".format("Delivery Charge:", d)
    print(total_4)


def sub_menu_function(s, c):
    """Print a sub menu when the user selects to update their order.

    This provides users with options to change the quantity of
    or a remove pizzas from their order. It will then save these
    changes and redirect the user to the main menu.
    :param s: List (containing all of the update options
    e.g 'Change' and 'Remove')
    :param c: List (with pizza names and prices
    which have been selected by the customer)
    List is a multidimensional list of [ [int, str] ]
    :return: Bool
    """
    print("UPDATE MENU:")
    print(100*"-")
    # Start a loop which will terminate when
    # the user is finished updating their order
    run = True
    while run is True:
        # A loop of fixed length
        for i in range(0, len(s)):
            output = "{:<2} : {:<2}".format(s[i][0], s[i][1])
            print(output)
        # Ask the user how they would like to update their order
        option = validate_string("Which option would you like to select: ", 1, 1)
        # The user chooses to change their order
        if option == "C":
            # The index number the user would like to change
            index = validate_index("Which index number would you like to edit: ", 0, len(c))
            # The new quantity of pizzas the customer would like to order
            new_quantity = validate_integer("Please enter the new total quantity of {} pizzas: "
                                            .format(c[index-1][1]), 0, 5)
            # The pizza quantity replaces the old pizza quantity
            c[index-1][0] = new_quantity
            # Confirmation message
            print("Your order has been updated, you now have {} {} pizzas."
                  .format(c[index-1][0], c[index-1][1]))
            print(100*"-")
            # The user chooses to remove a pizza from their order
        elif option == "R":
            # The index number the user would like to remove
            index = validate_index("Which index number would you like to remove: ", 0, len(c))
            # Confirmation for the user
            choice = validate_y_and_n("Are you sure you would like to remove this flavour from the list? \n"
                                      "Please enter 'y' for yes and 'n' for no: ", 1, 1)
            # The user chooses to remove a pizza
            if choice in ["Y", "y"]:
                # The pizza is removed from the customer list
                c.pop(index-1)
                print("Your order has been updated :)")
                # End of the conditional statement
                run = False
            # The user chooses to remove no pizzas
            elif choice in ["N", "n"]:
                # No changes are made
                print("Your order has not been updated. \n"
                      "You have been directed back to the main menu :)")
                # End of the conditional statement
                run = False
            # The user enters an inappropriate answer
            else:
                print("Please enter either 'y' for 'yes' or 'n' for 'no'. \n"
                      "Your answer cannot be an integer.")
        # The user chooses to return to the main menu
        elif option == "M":
            # End of the conditional statement
            run = False
        # The user enters an inappropriate answer
        else:
            print("Please enter a single letter listed above. \n"
                  "Your answer is not appropriate.")


def cancel_order(c, d):
    """
    Cancel the user's order upon request.

    This clears all of the user's information and their
    entire pizza order upon request. It sends the user to
    the beginning of a new order where they are asked for their
    customer information once more.
    :param c: List (with pizza names and prices
    which have been selected by the customer)
    List is a multidimensional list of [ [int, str] ]
    :param d: List (the customer's information)
    List is a multidimensional list of [ [int, str] ]
    and [ [str, str] ]
    :return: Bool
    """
    # Start a loop which will terminate when the user has
    # finished updating their order
    run = True
    while run is True:
        # Confirmation for the customer
        answer = validate_y_and_n("Are you sure you would like to cancel your order?\n"
                                  "Press 'y' for 'yes' and 'n' for 'no': ", 1, 1)
        # The user confirms their order cancellation
        if answer in ["Y", "y"]:
            # The customer's pizza list is cleared
            c.clear()
            # The customer's details are cleared
            d.clear()
            print("Your order has been canceled :)")
            # End of the conditional statement
            return True
        # The user does not confirm their order cancellation
        elif answer in ["N", "n"]:
            # Confirmation message
            # No further changes are made
            print("Your order has not been canceled. \n"
                  "You have been directed back to the main menu :)")
            # End of the conditional statement
            return False
        # The user enters an inappropriate answer
        else:
            print("Please enter either 'y' for 'yes' or 'n' for 'no'")


def customer_information(i):
    """Ask the user for their information.

    This provides users with delivery and pick-up options, requesting
    particular information specific to their choices. It stores and
    inserts this information into the customer details list.
    :param i: List (containing all of the customer's
    personal information)
    List is a multidimensional list of [ [str, str]
    and [str, int] ]
    :return: Int (Delivery Charge)
    """
    print(100*"-")
    print("WELCOME TO PIZZAROO, THIS IS THE SHOP FOR YOU!")
    print(100*"-")
    # Get rid of this loop
    run = True
    while run is True:
        # Ask the user whether they would like to receive
        # their order through delivery or pick it up
        service = validate_p_and_d("Would you like to pick up \n"
                                   "your order or receive it through delivery? \n"
                                   "Press 'P' for pick up order and 'D' for delivery: ", 1, 1)
        # The user selects to pick up their order
        if service in ["P", "p"]:
            name = validate_names_address("Please enter your full name: ", 2, 50)
            phone = validate_string("Please enter your phone number: ", 5, 20)
            card = validate_string("Please enter your card number. (MUST be 16 characters): ", 16, 16)
            print(100*"-")
            # Identifies the user's full name, phone number and card number
            # (and their titles)
            temp_information_1 = [("Full Name", name),
                                  ("Phone Number", phone), ("Card Number", card)]
            # Sends the user's information to the 'print_customer_information'
            # function so it can be printed accordingly
            i.extend(temp_information_1)
            # Return no delivery charge fee as the user
            # has requested to pick up their order
            # End of conditional statement
            return 0
        # The user selects to receive their order through delivery
        elif service in ["D", "d"]:
            # Set the delivery charge to 3
            delivery_charge = 3
            name = validate_names_address("Please enter your full name: ", 2, 50)
            address_line_1 = validate_names_address("Please enter the first line of your Address. \n"
                                                    "i.e: '13 Matai Road' : ", 3, 70)
            address_line_2 = validate_names_address("Please enter the second line of your Address, (OPTIONAL) \n"
                                                    "e.g: 'Apt 2A, Level 3': ", 0, 70)
            phone = validate_string("Please enter your phone number: ", 5, 15)
            card = validate_string("Please enter your card number. (MUST be 16 characters): ", 16, 16)
            # Ask the user for their preferred delivery service
            delivery_service = validate_u_and_d("Which delivery service would you like to use? \n"
                                                "Press 'D' for Deliver Easy or 'U' for Uber Eats: ", 1, 1)
            # The user selects Uber Eats delivery service
            if delivery_service in ["U", "u"]:
                delivery_service = "UBER EATS"
            # The user selects Deliver Easy delivery service
            elif delivery_service in ["D", "d"]:
                delivery_service = "DELIVER EASY"
            # The user enters an inappropriate answer
            else:
                print("Please enter either 'U' for Uber Eats or 'D' for Deliver Easy.")
            print(100*"-")
            # Identifies the user's full name, home address, phone number,
            # card number and delivery service (and their titles)
            temp_information_2 = [("Full Name", name),
                                  ("Address Line One", address_line_1),
                                  ("Address Line Two", address_line_2),
                                  ("Phone Number", phone), ("Card Number", card),
                                  ("Delivery Service", delivery_service)]
            # Sends the user's information to the 'print_customer_information'
            # function so it can be printed accordingly
            i.extend(temp_information_2)
            # Sends the delivery charge to the 'review_customer_order' function
            # (so it can be printed and calculated in the total cost)
            # End of conditional statement
            return delivery_charge


def print_customer_information(c):
    """
    Print the customer information.

    :param c: list
    (containing all of the customer's personal information)
    List is a multidimensional list of [ [str, str]
    and [str, int] ]
    :return: None
    """
    print("MY INFORMATION")
    print(100*"-")
    # A loop of fixed length
    for i in range(0, len(c)):
        # Printing the user's information
        # and their corresponding titles in columns
        output = "{:<20} : {:<20}".format(c[i][0], c[i][1])
        print(output)
    print(100 * "-")


def main():
    """
    Run the main menu in a loop until the user quits the program.

    This stores the empty customer details and pizza lists. It also
    defines the delivery fee, whilst storing the main pizza menu and
    the update sub-menu. Continues to print the main menu and provides
    alternate pathways for the user.
    :return: None
    """

    # The Pizzaroo Pizza Menu
    # Pizzaroo pizza flavours and prices
    pizza_menu = [
        ["Simply Cheese", 18.50],
        ["Taco Fiesta", 18.50],
        ["Avocado Veg", 18.50],
        ["Bacon and Aioli", 18.50],
        ["New Yorker", 18.50],
        ["Baffalo Chicken", 18.50],
        ["Garlic Shrimp Supreme", 18.50],
        ["Mega Meat Lovers", 21.50],
        ["Big New Yorker", 21.50],
        ["Fried Buffalo Chicken", 21.50],
        ["Seafood Supreme", 21.50],
        ["Triple Bacon Cheeseburger", 21.50],
        ["Vegan Veg Korma", 21.50]
    ]

    # The user's information
    # Empty so the user can personalise their information
    customer_details = []

    # The user's pizza order
    # Empty so the user can personalise their pizza order
    customer_pizzas = []

    # Delivery charge is defined as 0
    # When defined otherwise in separate functions
    # the program adds to the figure 0
    # Ensures this value can be passed between
    # functions when required
    delivery_charge = 0

    # The update order sub menu
    # Identifies the update options and their corresponding letters
    sub_menu = [
        ("C", "Change Pizza Quantity"),
        ("R", "Remove a Pizza"),
        ("M", "Main Menu"),
    ]

    # The main menu
    # Lists all of the alternate pathways the user can take and
    # their corresponding letters
    my_menu = [("V", "View Pizza Menu"),
               ("O", "Order A Pizza"),
               ("R", "Review My Pizza Order"),
               ("U", "Update My Order"),
               ("C", "Cancel My Order"),
               ("F", "Finalise My Order"),
               ("Q", "Quit Program")
               ]

    # Name/Title of Pizza Program
    print(100*"-")
    print("PIZZAROO")
    print(100*"-")

    # A new order is beginning which loops every time an order is
    # cancelled or finalised
    start_new_order = True
    # Main menu loop
    # Printed every time a function is completed/the user is
    # redirected to the main menu
    run = True
    while run is True:
        # When a new order begins
        if start_new_order == True:
            # Ask for all of the user's necessary details
            # Insert this information to the 'customer_details' list
            delivery_charge = customer_information(customer_details)
            # Print the user's information stored in the
            # 'customer_details' list
            print_customer_information(customer_details)
            # start_new_order loop ends
            # Loop repeats customer information every time an order is
            # cleared/cancelled/finalised/a new order has begun
            start_new_order = False
        # A loop of fixed length
        for i in range(0, len(my_menu)):
            # Prints the main menu in two separate columns
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        # Requests the user to select an option from the main menu
        option = validate_string("Please choose an option: --> ", 1, 1)
        # The user selects to view the pizza menu
        if option == "V":
            print(100*"-")
            # The Pizzaroo pizza menu is printed
            print_pizza_menu(pizza_menu)
            print(100*"-")
        # The user selects to order a pizza
        elif option == "O":
            print(100*"-")
            # The user can order a pizza from the Pizzaroo menu
            customer_order(pizza_menu, customer_pizzas)
            print(100*"-")
        # The user selects to review their pizza order
        elif option == "R":
            # The user has no pizzas in their order/list yet
            if len(customer_pizzas) == 0:
                print(100*"-")
                # Informs the user they have no pizzas in their order
                # and to visit the 'O' option in the main menu
                # Immediately directs the user back to the main menu
                print("You have nothing in your order yet. \n"
                      "Please navigate to the 'Order a Pizza' option in the main menu.")
                print(100 * "-")
            # The user has pizzas in their order/list
            else:
                print(100*"-")
                # The user's pizza order is printed and they
                # can review their choices
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
        # The user selects to update their pizza order
        elif option == "U":
            # The user has no pizzas in their order/list yet
            if len(customer_pizzas) == 0:
                print(100 * "-")
                # Informs the user they have no pizzas in their list/order
                # Tells the user to visit the 'O' option in the main menu
                # Immediately directs the user back to the main menu
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            # The user has pizzas in their order/list
            else:
                print(100 * "-")
                # The user's pizza order is printed and they
                # can review their choices
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
                # The user is asked to update their order
                # (change/remove pizzas)
                sub_menu_function(sub_menu, customer_pizzas)
                print(100 * "-")
        # The user selects to cancel their order
        elif option == "C":
            # The user has no pizzas in their order/list yet
            if len(customer_pizzas) == 0:
                print(100 * "-")
                # Informs the user they have no pizzas in their list/order
                # Tells the user to visit the 'O' option in the main menu
                # Immediately directs the user back to the main menu
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            # The user has pizzas in their order/list
            else:
                print(100*"-")
                # The user's pizza order and
                # customer information is printed
                print_customer_information(customer_details)
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
                # The user's information and pizza order and
                # information is cleared
                # The 'start_new_order' loop repeats
                # The user is asked to enter their information
                # for their new order
                start_new_order = cancel_order(customer_pizzas, customer_details)
                print(100*"-")
        # The user selects to finalise their order
        elif option == "F":
            # The user has no pizzas in their order/list yet
            if len(customer_pizzas) == 0:
                print(100 * "-")
                # Informs the user they have no pizzas in their list/order
                # Tells the user to visit the 'O' option in the main menu
                # Immediately directs the user back to the main menu
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            # The user has pizzas in their order/list
            else:
                print(100*"-")
                # The user's information and pizza order is printed
                print_customer_information(customer_details)
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
                # The user is asked to finalise their order
                final = validate_y_and_n("This is the current status of your order. \n"
                                         "Are you happy to confirm it? \n"
                                         "Enter 'y' for 'yes' and 'n' for 'no': ", 1, 1)
                # The user confirms their order
                if final in ["Y", "y"]:
                    # Confirmation messages
                    print("Thank you for shopping with Pizzaroo!!")
                    print("Enjoy your pizzas :)")
                    # The user's pizza order and information is cleared
                    customer_pizzas.clear()
                    customer_details.clear()
                    # The 'start_new_order' loop repeats
                    # The user is asked to enter their
                    # information for their new order
                    start_new_order = customer_information(customer_details)
                # The user does not confirm their order
                elif final in ["N", "n"]:
                    # Confirmation message
                    # No further changes are made
                    print("Your order has not been completed.")
                # The user enters an inappropriate answer
                else:
                    print("Please enter either 'y' for yes or 'n' for no")
        # The user selects to quit the program
        elif option == "Q":
            print(100*"-")
            # Confirmation message
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
            # The loop is terminated
            # The user permanently leaves the program
            run = False
        # The user enters an inappropriate answer
        else:
            print("Please enter a single letter listed above. \n"
                  "Your answer is not appropriate.")
            print(100*"-")


main()


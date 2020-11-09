"""This is a program which enables customers to order pizzas"""

# This imports validations functions I have created in a separate file
from validations import validate_index
from validations import validate_integer
from validations import validate_string
from validations import validate_p_and_d
from validations import validate_u_and_d


def print_pizza_menu(p):
    """
    Print the pizza list with indexes
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
        # The indexes are printed as 'i+1' so the numbers print from 1 instead of 0
        output = "{:3} : {:27} ${:1}0".format(i+1, p[i][0], p[i][1])
        print(output)


def scan_customer_list(c):
    """
    Scan the customer list for alike values
    :param c: List (with pizza names which have been selected by the customer and their prices)
    :return: Int (The quantity of pizzas the customer wants to add)
    """
    # A loop of fixed length
    for i in range(0, len(c)):
        if c == c[i][0]:
            number_of_choice = validate_integer("Please enter the new quantity of pizzas you would like: ", 0, 5)
            print("This value has been added to a pizza already in your list")
            print("You have entered {} with {} pieces".format(c[1][0], number_of_choice))
            c[i][1] += number_of_choice
        return True
    return False


def customer_order(p, r):
    """
    Ask the customer for their pizza order. Ask for pizza flavour and quantity.
    :param p: List (with name and prices of the pizzas)
    :param r: List (with pizza names which have been selected by the customer and their prices)
    :return: Str, Int (the cost and flavours of pizzas)
    """
    print_pizza_menu(p)
    print(100*"-")
    # Asks the customer for the index/pizza they would like to order
    index_number = validate_index("Please chose the index number of the pizza you would like to order: ", 0, len(p))
    # Defines the index number (i_no) as one minus the customer's index input (as indexes begin at 1, not 0)
    i_no = index_number - 1
    # Asks for the quantity of pizzas the customer would like to order
    amount = validate_integer("How many {} pizzas would you like to order: ".format(p[i_no][0]), 0, 5)
    update = "{} {} pizzas have now been added to your order".format(amount, p[i_no][0])
    print(update)
    # Cost of one pizza
    pizza_cost = p[i_no][1]
    # The quantity, flavour and cost of a singular pizza
    temp_pizzas = [amount, p[i_no][0], pizza_cost]
    # Inserting pizza information into the customer list
    r.append(temp_pizzas)


def review_customer_order(r, d):
    """
    Print the current/updated customer order
    :param r: List (with pizza names which have been selected by the customer and their prices)
    :return: None
    """
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:5} {:<9}  {:<51}  {:<45}".format("", "Qty", "Flavour", "Cost")
    print(output)
    # Defines the total quantity and costs of the pizzas as $0 before the loop begins
    total_cost = 0
    total_quantity = 0
    complete_cost = 0
    # A loop of fixed length
    for i in range(0, len(r)):
        # Multiplying the quantity and price of a singular pizza, resulting in it's total price
        cost = r[i][0] * r[i][2]
        # Adding a cost to the total cost, every time the loop in repeated/a new pizza(s) is added
        total_cost += r[i][0]*r[i][2]
        complete_cost = total_cost + d
        # Adding a pizza quantity to the total quantity, every time the function is repeated/a new pizza(s) is added
        total_quantity += r[i][0]
        output = "{:3} : {:<8} : {:<25} @ a price of ${:<10} : ${}0".format(i+1, r[i][0], r[i][1], r[i][2], cost)
        print(output)
    print(100*"-")
    # Print concluding information
    total_1 = "{:>78} {:<10}".format("Total Pizzas:", total_quantity)
    print(total_1)
    total_2 = "{:>76} ${:<10.2f}".format("Total Cost:", complete_cost)
    print(total_2)
    total_3 = "{:>76} ${:<10.2f}".format("Delivery Charge:", d)
    print(total_3)


def sub_menu_function(s, c):
    """
    Print a sub menu when the user selects to update their current order.
    Change or a remove a pizza from the user's order.
    Send the user back to the main menu.
    :param s: List (
    :param c: List (with pizza names which have been selected by the customer and their prices)
    :return:
    """
    print("UPDATE MENU:")
    print(100*"-")
    run = True
    # Start a loop which will terminate when the user does not want to continue any more
    while run is True:
        for i in range(0, len(s)):
            output = "{:<2} : {:<2}".format(s[i][0], s[i][1])
            print(output)
        option = validate_string("Which option would you like to select: ", 1, 1)
        if option == "C":
            index = validate_index("Which index number would you like to edit: ", 0, len(c))
            new_quantity = validate_integer("Please enter the new total quantity of {} pizzas: ".format(c[index-1][1]), 0, 5)
            c[index-1][0] = new_quantity
            print("Your order has been updated, you now have {} {} pizzas.".format(c[index-1][0], c[index-1][1]))
            print(100*"-")
        elif option == "R":
            message1 = "Which index number would you like to edit: "
            index = validate_integer(message1, 0, len(c))
            message2 = "Are you sure you would like to remove this flavour from the list? \n" \
                       "Enter 'y' for yes and 'n' for no: "
            choice = validate_integer(message2, 1, 1)
            if choice in ["Y", "y"]:
                c.pop(index-1)
                print("Your order has been updated :)")
                run = False
            elif choice in ["N", "n"]:
                print("Your order has not been updated, you have been directed back to the main menu :)")
                run = False
            else:
                print("Please enter either 'y' for 'yes' or 'n' for 'no'. Your answer cannot be an integer.")
                continue
        elif option == "M":
            run = False
        else:
            print("This is not a valid option. Please try again :)")


def cancel_order(c):
    run = True
    while run is True:
        answer = validate_string("Are you sure you would like to cancel your order? \n"
                                 "Press 'y' for 'yes' and 'n' for 'no': ", 1, 1)
        if answer in ["Y", "y"]:
            c.clear()
            print("Your order has been canceled :)")
            return True
        elif answer in ["N", "n"]:
            print("Your order has not been canceled, you have been directed back to the main menu :)")
            return False
        else:
            print("Please enter either 'y' for 'yes' or 'n' for 'no'")
            print(100 * "-")
            continue


def customer_information(i):
    print(100*"-")
    print("WELCOME TO PIZZAROO, THIS IS THE SHOP FOR YOU!")
    print(100*"-")
    run = True
    while run is True:
        service = validate_p_and_d("Would you like to pick up your order or receive it through delivery? \n"
                                  "Press 'P' for pick up order and 'D' for delivery: ", 1, 1)
        if service in ["P", "p"]:
            name = validate_string("Please enter your full name: ", 2, 50)
            phone = validate_string("Please enter your phone number: ", 5, 15)
            card = validate_string("Please enter your card number: ", 16, 16)
            print(100*"-")
            temp_information_1 = [("Full Name", name), ("Phone Number", phone), ("Card Number", card)]
            i.extend(temp_information_1)
            return 0
        elif service in ["D", "d"]:
            delivery_charge = 3
            name = validate_string("Please enter your full name: ", 2, 50)
            address_line_1 = validate_string("Please enter the first line of your Address, i.e: '13 Hataitai Road' : ",
                                             3, 70)
            address_line_2 = validate_string("Please enter the second line of your Address, (OPTIONAL) \n"
                                             "e.g: 'Apt 2A, Level 3': ", 0, 70)
            phone = validate_string("Please enter your phone number: ", 5, 15)
            card = validate_string("Please enter your card number: ", 16, 16)
            delivery_service = validate_u_and_d("Which delivery service would you like to use? \n"
                                                "Press 'D' for Deliver Easy or 'U' for Uber Eats: ", 1, 1)
            if delivery_service in ["U", "u"]:
                delivery_service = "UBER EATS"
            elif delivery_service in ["D", "d"]:
                delivery_service = "DELIVER EASY"
            else:
                print("Please enter either 'U' for Uber Eats or 'D' for Deliver Easy.")
                continue
            print(100*"-")
            temp_information_2 = [("Full Name", name), ("Address Line One", address_line_1), ("Address Line Two", address_line_2),
                                  ("Phone Number", phone), ("Card Number", card), ("Delivery Service", delivery_service)]
            i.extend(temp_information_2)
            return delivery_charge


def print_customer_information(c):
    print("MY INFORMATION")
    print(100*"-")
    for i in range(0, len(c)):
        output = "{:<20} : {:<20}".format(c[i][0], c[i][1])
        print(output)
    print(100 * "-")


def main():

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

    customer_details = []

    customer_pizzas = []

    delivery_charge = 0

    # test_order = [
    #    [4, 'Bacon and Aioli', 18.5, 74.0],
    #    [3, 'Taco Fiesta', 18.5, 55.5],
    #    [5, 'Fried Buffalo Chicken', 21.5, 107.5]
    #  ]
    # customer_pizzas = test_order

    sub_menu = [
        ("C", "Change Order Quantity"),
        ("R", "Remove a Pizza"),
        ("M", "Main Menu"),
    ]

    my_menu = [("V", "View Pizza Menu"),
               ("P", "Place An Order"),
               ("R", "Review My Pizza Order"),
               ("U", "Update My Order"),
               ("C", "Cancel My Order"),
               ("Q", "Quit Program")
               ]

    print(100 * ("-"))
    print("PIZZAROO")
    print(100 * ("-"))

    start_new_order = True
    run = True
    while run is True:
        if start_new_order == True:
            delivery_charge = customer_information(customer_details)
            print_customer_information(customer_details)
            start_new_order = False
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = validate_string("Please choose an option: --> ", 1, 1)
        if option == "V":
            print(100*"-")
            print_pizza_menu(pizza_menu)
            print(100*"-")
        elif option == "P":
            print(100*"-")
            customer_order(pizza_menu, customer_pizzas)
            print(100*"-")
        elif option == "R":
            if len(customer_pizzas) == 0:
                print(100*"-")
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            else:
                print(100*"-")
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
        elif option == "U":
            if len(customer_pizzas) == 0:
                print(100 * "-")
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            else:
                print(100 * "-")
                review_customer_order(customer_pizzas, delivery_charge)
                print(100*"-")
                sub_menu_function(sub_menu, customer_pizzas)
                print(100 * "-")
        elif option == "C":
            print(100*"-")
            review_customer_order(customer_pizzas, delivery_charge)
            print(100*"-")
            start_new_order = cancel_order(customer_pizzas)
            print(100*"-")
        elif option == "Q":
            run = False
            print(100*"-")
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
        else:
            print("Please enter a single letter listed above. Your answer is not appropriate.")
            print(100*"-")


main()
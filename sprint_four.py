"""This is a pizza delivery program."""
from validations import validate_index
from validations import validate_integer
from validations import validate_string


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
    for i in range(0, len(p)):
        output = "{:3} : {:27} ${:1}0".format(i+1, p[i][0], p[i][1])
        print(output)


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
    index_number = validate_index("Please chose the index number of the \n"
                                  "pizza you would like to order: ", 0, len(p))
    i_no = index_number - 1
    amount = validate_integer("How many {} pizzas would you like to order: "
                              .format(p[i_no][0]), 0, 5)
    cost = amount * p[i_no][1]
    update = "{} {} pizzas have now been added to your order"\
        .format(amount, p[i_no][0])
    print(update)
    statement = "@ ${} each".format(p[i_no][1])
    temp_pizzas = [amount,  p[i_no][0], statement, cost]
    r.append(temp_pizzas)


def review_customer_order(r):
    """Print the current customer order status.

    This formats and prints the cost, quantity
    and flavour of pizzas in the customer's order,
    factoring GST and delivery charge.
    Every time a new pizza is added/taken away these values update.

    :param r: List (with pizza names and prices
    which have been selected by the customer)
    List is a multidimensional list of [ [int, str] ]
    :return: None
    """
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:<6}  {:<42}  {:<55}".format("Qty", "Flavour", "Cost")
    print(output)
    total_cost = 0
    total_quantity = 0
    for i in range(0, len(r)):
        total_cost += r[i][3]
        total_quantity += r[i][0]
        output = "{:<5} : {:<25} {:<15} : ${}0"\
            .format(r[i][0], r[i][1], r[i][2], r[i][3])
        print(output)
    output1 = "{:>63} ${:<10.2f}".format("Total Cost:", total_cost)
    print(output1)
    output2 = "{:>67} {:<10}".format("Total Quantity:", total_quantity)
    print(output2)


def main():
    """
    Run the main menu in a loop until the user quits the program.

    This stores the empty customer details and pizza lists. It also
    defines the delivery fee, whilst storing the main pizza menu and
    the update sub-menu. Continues to print the main menu and provides
    alternate pathways for the user.
    :return: None
    """
    pizza_menu = [
        ["Simply Cheese", 18.50],
        ["Taco Fiesta", 18.50],
        ["Avocado Veg", 18.50],
        ["Bacon and Aioli", 18.50],
        ["Double Bacon Cheeseburger", 18.50],
        ["Vegan Supreme", 18.50],
        ["Seafood Deluxe", 18.50],
        ["Creamy Chicken Mayo", 18.50]
    ]

    customer_pizzas = []

    my_menu = [("V", "View Pizza Menu"),
               ("P", "Place An Order"),
               ("R", "Review My Pizza Order"),
               ("Q", "Quit Program")
               ]

    print(100 * ("-"))
    print("PIZZAROO")
    print(100 * ("-"))

    run = True
    while run is True:
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
            print(100*"-")
            review_customer_order(customer_pizzas)
            print(100*"-")
        elif option == "Q":
            run = False
            print(100*"-")
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
        else:
            print("This is not a valid option. Please try again :)")


main()

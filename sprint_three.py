def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_pizza_menu(p):
    print("PIZZA MENU:")
    print(100 * "-")
    for i in range(0, len(p)):
        output ="{:1} : {:10}  {:10}".format(i+1, p[i][0], p[i][1])
        print(output)


def customer_order(p, r):
    print_pizza_menu(p)
    print(100*"-")
    index_number = get_integer("Please chose the index number of the pizza you would like to order: ")
    i_no = index_number - 1
    amount = get_integer("How many {} pizzas would you like to order: ".format(p[i_no][0]))
    update = "{} {} pizzas have now been added to your order".format(amount, p[i_no][0])
    print(update)
    updated_list = [amount,  p[i_no][0]]
    r.append(updated_list)


def review_customer_order(r):
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:10} : {:30}".format("Quantity", "Type")
    print(output)
    for i in range(0, len(r)):
        output = "{:10} : {:30}".format(r[i][0], r[i][1])
        print(output)


def checkout(r, m):
    print(100 * "-")
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:10} : {:30}".format("Quantity", "Type")
    print(output)
    for i in range(0, len(r)):
        output = "{:10} : {:30}".format(r[i][0], r[i][1])
        print(output)
        print(100 * "-")

    run = True
    while run is True:
        confirmation = get_string("Does this complete your order? Press 'y' for yes and 'n' for no: ")
        if confirmation == "y":
            print(100 * "-")
            print("Thank you for shopping with Pizzaroo!")
            print(100 * "-")
            run = False
        elif confirmation == "n":
            print("Please return to the 'Order' section in our menu")
            print(100 * "-")
            run = False

        else:
            print("That is not a valid option. Please try again :)")



def main():

    pizza_menu = [
        ["Simply Cheese", "$18.50"],
        ["Taco Fiesta", "$18.50"],
        ["Avocado Veg", "$18.50"],
        ["Bacon and Aioli", "$18.50"],
        ["Double Bacon Cheeseburger", "$18.50"],
        ["Vegan Supreme", "$18.50"],
        ["Seafood Deluxe", "$18.50"],
        ["Creamy Chicken Mayo", "$18.50"]
    ]

    customer_pizzas = []

    my_menu = [("P", "Pizza Menu"),
               ("O", "Order"),
               ("R", "Review Pizza Order"),
               ("C", "Checkout"),
               ("Q", "Quit")
               ]

    print(100 * ("-"))
    print("PIZZAROO")
    print(100 * ("-"))

    run = True
    while run is True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Please choose an option: --> ")
        if option == "P":
            print(100*"-")
            print_pizza_menu(pizza_menu)
            print(100*"-")
        elif option == "O":
            print(100*"-")
            customer_order(pizza_menu, customer_pizzas)
            print(100*"-")
        elif option == "R":
            print(100*"-")
            review_customer_order(customer_pizzas)
            print(100*"-")
        elif option == "C":
            checkout(customer_pizzas, my_menu)
        elif option == "Q":
            run = False
            print(100*"-")
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
        else:
            print("This is not a valid option. Please try again :)")
main()
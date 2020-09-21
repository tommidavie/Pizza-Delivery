from validations import validate_index
from validations import validate_integer


def get_string(m):
    my_string = input(m).upper()
    return my_string


def print_pizza_menu(p):
    print("PIZZA MENU:")
    print(100 * "-")
    output = "{:5} {:27}  {:1}".format("", "FLAVOUR:", "PRICE:")
    print(output)
    print(100 * "-")
    for i in range(0, len(p)):
        output = "{:3} : {:27} ${:1}0".format(i+1, p[i][0], p[i][1])
        print(output)


def customer_order(p, r):
    print_pizza_menu(p)
    print(100*"-")
    index_number = validate_index("Please chose the index number of the pizza you would like to order: ", 0, len(p))
    i_no = index_number - 1
    amount = validate_integer("How many {} pizzas would you like to order: ".format(p[i_no][0]), 0, 5)
    cost = amount * p[i_no][1]
    update = "{} {} pizzas have now been added to your order".format(amount, p[i_no][0])
    print(update)
    statement = "@ ${} each".format(p[i_no][1])
    temp_pizzas = [amount,  p[i_no][0], statement, cost]
    r.append(temp_pizzas)


def review_customer_order(r):
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:<6}  {:<42}  {:<55}".format("Qty", "Flavour", "Cost")
    print(output)
    total_cost = 0
    for i in range(0, len(r)):
        total_cost += r[i][3]
        output = "{:<5} : {:<25} {:<15} : ${}0".format(r[i][0], r[i][1], r[i][2], r[i][3])
        print(output)
    output = "{:>63} ${:<10.2f}".format("Total Cost:",total_cost)
    print(output)


def main():

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
        option = get_string("Please choose an option: --> ")
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
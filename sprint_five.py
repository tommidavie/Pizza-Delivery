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


def scan_customer_list(c):
    for i in range(0, len(c)):
        if c == c[i][0]:
            number_of_choice = validate_integer\
                ("Please enter the new quantity of pizzas you would like: ", 0, 5)
            print("This value has been added to a pizza already in your list")
            print("You have entered {} with {} pieces"
                  .format(c[1][0], number_of_choice))
            c[i][1] += number_of_choice
        return True
    return False


def customer_order(p, r):
    print_pizza_menu(p)
    print(100*"-")
    index_number = validate_index\
        ("Please chose the index number of the pizza you would like to order: "
         , 0, len(p))
    i_no = index_number - 1
    amount = validate_integer\
        ("How many {} pizzas would you like to order: "
         .format(p[i_no][0]), 0, 5)
    update = "{} {} pizzas have now been added to your order"\
        .format(amount, p[i_no][0])
    print(update)
    # cost of one pizza
    pizza_cost = p[i_no][1]
    temp_pizzas = [amount,  p[i_no][0], pizza_cost]
    r.append(temp_pizzas)


def review_customer_order(r):
    print("CURRENT ORDER STATUS")
    print(100*"-")
    output = "{:5} {:<9}  {:<51}  {:<45}"\
        .format("", "Qty", "Flavour", "Cost")
    print(output)
    total_cost = 0
    total_quantity = 0
    for i in range(0, len(r)):
        cost = r[i][0] * r[i][2]
        total_cost += r[i][0]*r[i][2]
        total_quantity += r[i][0]
        output = "{:3} : {:<8} : {:<25} @ a price of ${:<10} : ${}0".\
            format(i+1, r[i][0], r[i][1], r[i][2], cost)
        print(output)
    print(100*"-")
    total_1 = "{:>78} {:<10}".format("Total Pizzas:", total_quantity)
    print(total_1)
    total_2 = "{:>76} ${:<10.2f}".format("Total Cost:", total_cost)
    print(total_2)


def sub_menu_function(s, c):
    print("UPDATE MENU:")
    print(100*"-")
    for i in range(0, len(s)):
        output = "{:<2} : {:<2}".format(s[i][0], s[i][1])
        print(output)
    option = get_string("Which option would you like to select: ")
    if option == "C":
        index = validate_index\
            ("Which index number would you like to edit?: ", 0, len(c))
        new_quantity = validate_integer\
            ("Please enter the new total quantity of {} pizzas: "
                                        .format(c[index-1][1]), 0, 5)
        c[index-1][0] = new_quantity
    elif option == "R":
        index = validate_index\
            ("Which index number would you like to edit?: ", 0, len(c))
        choice = get_string\
            ("Are you sure you would like to remove this flavour from the list? \n"
             "Enter 'y' for yes and 'n' for no: ")
        if choice == 'Y':
            c.pop(index-1)
            return None
        if choice == 'N':
            return None
        else:
            print("Please enter either 'y' yes or 'n' no")
    elif option == "M":
        return None
    else:
        print("This is not a valid option. Please try again :)")


def main():

    pizza_menu = [
        ["Simply Cheese", 18.50],
        ["Taco Fiesta", 18.50],
        ["Avocado Veg", 18.50],
        ["Bacon and Aioli", 18.50],
        ["Big New Yorker", 21.50],
        ["Fried Buffalo Chicken", 21.50],
        ["Vegan Veg Korma", 21.50],
    ]

    customer_pizzas = []

    #test_order =[
        #[4, 'Bacon and Aioli', 18.5, 74.0],
        #[3, 'Taco Fiesta', 18.5, 55.5],
        #[5, 'Fried Buffalo Chicken', 21.5, 107.5]
     #]
    #customer_pizzas = test_order

    sub_menu = [
        ("C", "Change Order Quantity"),
        ("R", "Remove a Pizza"),
        ("M", "Main Menu"),
    ]

    my_menu = [("V", "View Pizza Menu"),
               ("P", "Place An Order"),
               ("R", "Review My Pizza Order"),
               ("U", "Update My Order"),
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
            if len(customer_pizzas) == 0:
                print(100*"-")
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            else:
                print(100*"-")
                review_customer_order(customer_pizzas)
                print(100*"-")
        elif option == "U":
            if len(customer_pizzas) == 0:
                print(100 * "-")
                print("You have nothing in your order yet - please navigate to the \n"
                      "'Place An Order' option in the main menu.")
                print(100 * "-")
            else:
                print(100 * "-")
                review_customer_order(customer_pizzas)
                print(100*"-")
                sub_menu_function(sub_menu, customer_pizzas)
                print(100 * "-")
        elif option == "Q":
            run = False
            print(100*"-")
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
        else:
            print("This is not a valid option. Please try again :)")
            print(100*"-")


main()
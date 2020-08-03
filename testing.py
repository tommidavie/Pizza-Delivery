def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string

def print_pizza_menu(p):
    for i in range(0, len(p)):
        output = "{:10} : {:10}".format(p[i][0], p[i][1])
        print(output)


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


    my_menu = [("R", "Review Pizza Menu"),
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
        if option == "R":
            print(100*"-")
            print("PIZZA MENU:")
            print(100*"-")
            print_pizza_menu(pizza_menu)
            print(100*"-")
        elif option == "Q":
            run = False
            print(100*"-")
            print("Thank you for shopping with Pizzaroo!")
            print(100*"-")
        else:
            print("This is not a valid option. Please try again :)")
main()


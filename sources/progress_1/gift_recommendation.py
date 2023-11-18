def opt():
    while True:
        print("choose option")
        print("1. Get gift recommendation")
        print("2. Enter the desired gift")
        # add 3rd function "getting a gift card message for random"
        print("3. Get a gift card message")
        print("4. Quit")
        option = int(input("enter the number of your option --> "))

        if option == 1:
            output_gift()
        elif option == 2:
            input_gift()
        elif option == 3:
            output_msg()
        elif option == 4:
            break
        else:
            print("Wrong input. Please input 1~4.")

def  output_gift():
    pass

def input_gift():
    pass

def output_msg():
    pass

opt()
    
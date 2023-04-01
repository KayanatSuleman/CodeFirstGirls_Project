def shop():
    customers_available_money = 100.00
    items_dict = {'Balenciaga Trainers': 785.00, 'Northface Jacket': 320.00, 'Gucci Handbag': 850.00}

    print("Welcome, Check out the designer items I have and their prices:")
    for item, price in items_dict.items():
        print(f"{item}: £{price}")

    while True:
        designer_item = input("Enter the designer item you would like to purchase or type 'exit' to leave the shop: ")

        if designer_item == 'exit':
            print("Thank you for shopping with us!")
            break

        if designer_item not in items_dict:
            print("Invalid item choice, please try again.")
            continue

        if items_dict[designer_item] > customers_available_money:
            print(f"You cannot afford {designer_item}, please enter a new item or type 'exit' to leave.")
            continue

        customers_available_money -= items_dict[designer_item]
        print(f"Here's your {designer_item}!")
shop()
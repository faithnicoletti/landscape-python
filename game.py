all_tools = {
    "teeth": {
        "earnings": 1,
        "purchase_fee": 0
    },
    "scissors": {
        "earnings": 5,
        "purchase_fee": 5
    },
    "push lawnmower": {
        "earnings": 50,
        "purchase_fee": 25
    },
    "battery-powered lawnmower": {
        "earnings": 100,
        "purchase_fee": 250
    },
    "team of starving students": {
        "earnings": 250,
        "purchase_fee": 500
    }
}

earnings = 0
purchased_tools = set()

while True:
    choice = input("Choose to cut grass or purchase a tool (type 'quit' to exit): ")

    if choice == "quit":
        print("Thanks for playing!")
        break

    if choice == "purchase":
        print("Available tools for purchase:")
        for tool, info in all_tools.items():
            if tool not in purchased_tools:
                print(f"{tool}: ${info['purchase_fee']}")

        purchase_choice = input("What tool do you want to purchase?: ")
        if purchase_choice in all_tools:
            if purchase_choice not in purchased_tools:
                if earnings >= all_tools[purchase_choice]["purchase_fee"]:
                    earnings -= all_tools[purchase_choice]["purchase_fee"]
                    purchased_tools.add(purchase_choice)
                    print(f"You purchased {purchase_choice} for ${all_tools[purchase_choice]['purchase_fee']}.")
                    print("Total earnings: $" + str(earnings))
                else:
                    print(f"You need ${all_tools[purchase_choice]['purchase_fee']} to purchase {purchase_choice}.")
            else:
                print(f"You have already purchased {purchase_choice}.")
        else:
            print("Tool not valid.")

    elif choice == "cut grass":
        print("Available tools:")
        available_tools = [tool for tool in all_tools if tool in purchased_tools or tool == "teeth"]
        for tool in available_tools:
            print(f"{tool}: Earn ${all_tools[tool]['earnings']} to cut grass")

        tool_choice = input("Choose a tool to cut grass: ")
        if tool_choice in all_tools and tool_choice in available_tools:
            earnings += all_tools[tool_choice]["earnings"]
            print(f"You used {tool_choice} to cut grass and earned ${all_tools[tool_choice]['earnings']}.")
            print("Total earnings: $" + str(earnings))
        else:
            print("Invalid tool choice.")

    else:
        print("Invalid choice.")

    if "team of starving students" in purchased_tools and earnings >= 1000:
        print("You have won the game!!!")
        break

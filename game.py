tools = {
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
        "purchase_fee": 500
    }
}

earnings = 0
purchased_tools = set()

while True:
    choice = input("Choose your tool (or type 'quit' to exit): ")

    if choice == "quit":
        print("Thanks for playing!")
        break

    if choice in tools:
        if choice not in purchased_tools:
            if earnings >= tools[choice]["purchase_fee"]:
                earnings -= tools[choice]["purchase_fee"]
                purchased_tools.add(choice)
                print(f"You purchased {choice} for ${tools[choice]['purchase_fee']}.")
                print("Total earnings: $" + str(earnings))
            else:
                print(f"You need ${tools[choice]['purchase_fee']} to purchase {choice}.")

    if choice in tools:

        earnings += tools[choice]["earnings"]
        print(f"You used {choice} to cut grass and earned ${tools[choice]['earnings']}.")
        print("Total earnings: $" + str(earnings))
    else:
        print("Not valid.")

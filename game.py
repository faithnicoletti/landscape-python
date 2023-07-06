earnings = 0

tools = {
    "teeth": {
        "earnings": 1,
        "purchase_fee": 0
    }
}

while True:
    choice = input("Choose your tool (or type 'quit' to exit): ")

    if choice == "quit":
        print("Thanks for playing!")
        break

    if choice in tools:
        if tools[choice]["purchase_fee"] == 0 or earnings >= tools[choice]["purchase_fee"]:
            earnings += tools[choice]["earnings"]
            print(f"You used {choice} to cut grass and earned ${tools[choice]['earnings']}.")
            print("Total earnings: $" + str(earnings))
        else:
            print(f"You need ${tools[choice]['purchase_fee']} to purchase {choice}.")
    else:
        print("Not a valid choice.") 
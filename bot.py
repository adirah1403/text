def show_menu():
    menu = {
        "1": {"item": "Pizza", "price": 8},
        "2": {"item": "Burger", "price": 5},
        "3": {"item": "Pasta", "price": 7},
        "4": {"item": "Salad", "price": 4}
    }
    print("\n--- MENU ---")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - ${value['price']}")
    return menu

def chatbot():
    print("🤖 Welcome to Foodie's Paradise Restaurant!")
    print("How can I assist you today?")
    print("1. Show Menu\n2. Order Food\n3. Book a Table\n4. Ask a Question\n5. Exit")

    menu = show_menu()  # Preload menu once

    while True:
        choice = input("\nEnter your option (1-5): ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            show_menu()
            order = input("Enter the item number you want to order: ")
            try:
                quantity = int(input("Enter quantity: "))
                if order in menu:
                    item = menu[order]["item"]
                    total = menu[order]["price"] * quantity
                    print(f"You have ordered {quantity} x {item}. Total = ${total}")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid quantity.")

        elif choice == "3":
            name = input("Enter your name: ")
            people = input("Number of people: ")
            time = input("Booking time (e.g., 7:00 PM): ")
            print(f"Thank you {name}, your table for {people} at {time} has been booked!")

        elif choice == "4":
            question = input("Ask your question: ").lower()
            if "timing" in question or "open" in question:
                print("We are open from 10 AM to 10 PM every day!")
            elif "location" in question or "address" in question:
                print("We are located at 123 Main Street, Foodie City.")
            elif "payment" in question or "pay" in question:
                print("We accept cash, credit/debit cards, and UPI payments.")
            elif "delivery" in question or "home delivery" in question:
                print("Yes, we offer free home delivery within a 5 km radius!")
            elif "contact" in question or "phone" in question:
                print("You can reach us at +1-234-567-8901.")
            elif "special" in question or "recommend" in question:
                print("Our chef recommends the Spicy Chicken Pizza and Creamy Alfredo Pasta.")
            elif "reservation" in question or "book" in question:
                print("You can book a table via this chatbot or call us directly for special arrangements.")
            else:
                print("Sorry, I can't answer that yet. Please call us for more information.")

        elif choice == "5":
            print("Thank you for visiting Foodie's Paradise! Have a great day! 🍽️")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Run the chatbot
chatbot()

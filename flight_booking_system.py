import random

# Sample Flight Data
flights = {
    1: {"from": "Chennai", "to": "Delhi", "price": 5000, "seats": 5},
    2: {"from": "Chennai", "to": "Mumbai", "price": 4500, "seats": 3},
    3: {"from": "Delhi", "to": "Bangalore", "price": 6000, "seats": 4}
}

bookings = []

def show_flights():
    print("\nAvailable Flights:")
    for flight_id, details in flights.items():
        print(f"{flight_id}. {details['from']} → {details['to']} | ₹{details['price']} | Seats: {details['seats']}")

def book_ticket():
    show_flights()
    try:
        choice = int(input("\nEnter Flight Number to Book: "))
        if choice in flights:
            if flights[choice]["seats"] > 0:
                name = input("Enter Passenger Name: ")
                ticket_id = random.randint(10000, 99999)

                flights[choice]["seats"] -= 1

                booking = {
                    "ticket_id": ticket_id,
                    "name": name,
                    "from": flights[choice]["from"],
                    "to": flights[choice]["to"],
                    "price": flights[choice]["price"]
                }

                bookings.append(booking)

                print("\n🎫 Booking Successful!")
                print_receipt(booking)
            else:
                print("❌ Sorry, no seats available.")
        else:
            print("❌ Invalid Flight Number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def print_receipt(booking):
    print("\n----- Flight Ticket Receipt -----")
    print(f"Ticket ID : {booking['ticket_id']}")
    print(f"Passenger : {booking['name']}")
    print(f"Route     : {booking['from']} → {booking['to']}")
    print(f"Amount    : ₹{booking['price']}")
    print("----------------------------------")

def main():
    while True:
        print("\n===== Flight Booking System =====")
        print("1. View Flights")
        print("2. Book Ticket")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_flights()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thank you for using the system ✈️")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

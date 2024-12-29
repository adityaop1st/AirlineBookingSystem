from booking_service import create_booking, create_payment,create_customer
from login_service import login
from flight_search_service import search_flight, get_flight_detail, get_seat_details
from entity import Customer, Payment, Flight, Booking
from datetime import date

def customer_login():
    print("Login Details")
    print("===============================================================================")
    user_id = input("User Name: defalut - aditya ::") or "aditya"
    #"aditya"
    password1 = input("Enter password: - defalut *****:: ") or "test"
    #"test"
    isSucessful = login(user_id, password1)
    return isSucessful

def create_customer_from(name, email, phone,seat):
    return Customer(name,email,phone,seat)

def proceed_with_payment(seat):
    amount = seat.price
    print("Total Payment:", amount)
    should_continue = input("Please confirm with payment through UPI, Values [Yes, No] default - Yes:: " ) or "Yes"
    if should_continue != "Yes":
        raise Exception("Bookinig aborted, please try again")
    payment = Payment(amount, date.today(), "UPI")
    return payment


def get_flight(flight_details):
    return Flight(flight_details[6], flight_details[1], flight_details[2], flight_details[3], flight_details[4],flight_details[5])


def book_a_ticket(customer, payment, flight):
    create_customer(customer)
    create_payment(payment)
    booking = Booking(date.today(), "CONFIRM", customer, payment, flight)
    booking = create_booking(booking)
    return booking


def print_a_ticket(booking):
    booking.printTicket()


def book_a_flight(flight_code):
    data = get_flight_detail(flight_code)
    flight_details = data[0]

    available_seat = data[1]
    if len(available_seat) == 0:
        raise Exception("Sorry, all seats are booked")

    print("Available seats")
    flight = ", ".join(str(element) for element in flight_details)
    print(flight)
    for f in available_seat:
        seat = ", ".join(str(element) for element in f)
        print(seat)
    print("===============================================================================")
    seat_id = input("Please choose seat default - SG-62-A-001:: ") or "SG-62-A-001"
    seat = get_seat_details(seat_id)

    name = input("Enter name default - Aditya::") or "Aditya"
    email = input("Enter Email default - aditya@gmail,com ::") or "aditya@gmail,com"
    phone = input("Enter Phone Number default - 989833333::") or "989833333"

    flight = get_flight(flight_details)
    customer = create_customer_from(name, email,phone, seat)
    payment = proceed_with_payment(seat)
    booking = book_a_ticket(customer, payment, flight)
    print_a_ticket(booking)

def choose_a_flight(available_flights):
    if(len(available_flights) == 0):
        raise Exception("No Flight Available")
    else:
        print("AVAILABLE FLIGHTS")
        print("Airline", "," "Flight No","," "arrival", ",", "Departure", ",", "arrival Time", ",", "Departure time")
        print("===============================================================================")
        for f in available_flights:
            flight = ", ".join(str(element) for element in f)
            print(flight)
        print("===============================================================================")
        flight_code = input("Choose flight to book - SG-2961:: ") or "SG-2961"
        return flight_code

def search_flight_data():
    print("Search Flight details")
    print("=========================")
    arrival = input("Arrival - PNQ : ") or "PNQ"
    departure = input("Departure - ADI: ") or "ADI"
    date = input("Enter traval Date -2024/12/26:") or "2024/12/26"

    available_flights = search_flight(arrival, departure, date)
    return available_flights

def main():
    isSucessful = customer_login()
    if (isSucessful):
        print("Login successful")
        available_flights = search_flight_data()
        flight_code = choose_a_flight(available_flights)
        book_a_flight(flight_code)
    else:
        raise Exception('Access denied')

if __name__ == "__main__":
    main()
class Customer:
    def __init__(self, customer_name, email, phone, seat):
        self.customer_id=0
        self.customer_name=customer_name
        self.email=email
        self.phone=phone
        self.seat = seat


class Flight:
    def __init__(self, Flight_id, Flight_number, Departure, arrival, Departure_time, arrival_time):
        self.Flight_id=Flight_id
        self.Flight_number=Flight_number
        self.arrival=arrival
        self.Departure=Departure
        self.Departure_time=Departure_time
        self.arrival_time = arrival_time
class Seat:
    def __init__(self, seat_id, seat_number,seat_class, price ):
        self.seat_id=seat_id
        self.seat_number=seat_number
        self.seat_class=seat_class
        self.price=price

class Payment:
    def __init__(self, amount, payment_date, payment_method):
        self.payment_id=0
        self.amount=amount
        self.payment_date=payment_date
        self.payment_method=payment_method

class Booking:
    def __init__(self, booking_date, booking_status, customer, payment, flight):
        self.booking_id=0
        self.booking_date=booking_date
        self. booking_status=booking_status
        self.customer=customer
        self.payment=payment
        self.flight=flight

    def printTicket(self):
        print("===============================Your Boarding Pass================================================")
        print("Welcome onboard ", self.customer.customer_name, "Your Ticket, Booking Id: :",  self.booking_id)
        print("Name: :",  self.customer.customer_name, "Email: ", self.customer.email, "Phone", self.customer.phone)
        print("Your flight details: :",  self.flight.Flight_number, "Seat Number: ", self.customer.seat.seat_number)
        print("your flight will depart from ",  self.flight.Departure, " At ", self.flight.Departure_time)
        print("Your will reach your destination  ", self.flight.arrival, " at ", self.flight.arrival_time)
        print("===============================================================================")



from connection_manager import connect
from entity import Seat, Flight, Airline

def create_flights(data):
    available_flights = []
    for d in data:
        f=create_flight(d)
        available_flights.append(f)
    return available_flights

def create_flight(d):
    a = Airline(d[0], d[1], d[3])
    f=Flight(a, d[3], d[4], d[5], d[6], d[7], d[8])
    return f

def create_seats(data, flight):
    for d in data:
        seat = Seat(d[0], d[1], d[2], d[3])
        flight.addSeat(seat)

def search_flight(departure, arrival, date):
    query = """SELECT A.airline_id, A.NAME, a.country, F.Flight_id, F.Flight_number, F.Departure, F.arrival, TIME(F.Departure_time), TIME(F.arrival_time)
                FROM FLIGHT F, AIRLINE A
                WHERE F.airline_id=A.airline_id 
                AND F.Departure= %s AND F.arrival = %s AND DATE(F.Departure_time)= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = ( departure, arrival, date)
    cursor.execute(query, criteria)
    data=cursor.fetchall()
    available_flights = create_flights(data)
    return available_flights


def get_flight_detail(flight_number):
    query = """SELECT A.airline_id, A.NAME, a.country, F.Flight_id, F.Flight_number, F.Departure, F.arrival, TIME(F.Departure_time), TIME(F.arrival_time)
                FROM FLIGHT F, AIRLINE A
                WHERE F.airline_id=A.airline_id 
                AND F.Flight_id= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (flight_number,)
    cursor.execute(query, criteria)
    flight_details=cursor.fetchone()
    flight = create_flight(flight_details)

    seat_query = """SELECT seat_id, seat_number, class, price from seat WHERE Flight_id= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (flight_number,)
    cursor.execute(seat_query, criteria)
    available_seats=cursor.fetchall()
    create_seats(available_seats, flight)
    return flight


def get_seat_details(seat_number):
    seat_query = """SELECT seat_id, seat_number, class, price from seat WHERE seat_id= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (seat_number,)
    cursor.execute(seat_query, criteria)
    selected_seat=cursor.fetchone()
    seat = Seat(selected_seat[0], selected_seat[1], selected_seat[2], selected_seat[3])
    return seat

flight_id='SG-2962'
flight = get_flight_detail(flight_id)
print(flight.__dict__)
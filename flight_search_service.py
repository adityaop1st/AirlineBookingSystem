from connection_manager import connect
from entity import Seat

def search_flight(departure, arival, date):
    query = """SELECT A.NAME, F.Flight_number, F.Departure, F.Arival, TIME(F.Departure_time), TIME(F.Arival_time)
                FROM FLIGHT F, AIRLINE A
                WHERE F.airline_id=A.airline_id 
                AND F.Departure= %s AND F.Arival = %s AND DATE(F.Departure_time)= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = ( departure, arival, date)
    cursor.execute(query, criteria)
    data=cursor.fetchall()
    return data

def get_flight_detail(flight_number):
    query = """SELECT A.NAME, F.Flight_number, F.Departure, F.Arival, TIME(F.Departure_time), TIME(F.Arival_time), F.flight_id, A.airline_id
                FROM FLIGHT F, AIRLINE A
                WHERE F.airline_id=A.airline_id 
                AND F.Flight_number= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (flight_number,)
    cursor.execute(query, criteria)
    flight_details=cursor.fetchone()

    seat_query = """SELECT seat_id, seat_number, class, price from seat WHERE Flight_id= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (flight_number,)
    cursor.execute(seat_query, criteria)
    available_seats=cursor.fetchall()
    return (flight_details, available_seats)


def get_seat_details(seat_number):
    seat_query = """SELECT seat_id, seat_number, class, price from seat WHERE seat_id= %s"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (seat_number,)
    cursor.execute(seat_query, criteria)
    selected_seat=cursor.fetchone()
    seat = Seat(selected_seat[0], selected_seat[1], selected_seat[2], selected_seat[3])
    return seat

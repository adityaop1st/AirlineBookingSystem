from connection_manager import connect
# from entity import Customer, Seat, Payment, Booking
# from datetime import date
# import random

def create_customer(customer):
    query = """INSERT INTO customer (customer_name, email, phone, seat_id) values (%s, %s, %s, %s) """
    connection = connect()
    cursor = connection.cursor()
    criteria = (customer.customer_name, customer.email, customer.phone, customer.seat.seat_id)
    cursor.execute(query, criteria)
    new_id = cursor.lastrowid
    customer.customer_id = new_id
    connection.commit()
    return customer


def create_payment(payment):
    query = """INSERT INTO payment (amount, payment_date, payment_method) values(%s,%s,%s)"""
    connection = connect()
    cursor = connection.cursor()
    criteria = (payment.amount,payment.payment_date,payment.payment_method)
    cursor.execute(query, criteria)
    new_id = cursor.lastrowid
    payment.payment_id = new_id
    connection.commit()
    return payment

def create_booking(booking):
    query = """INSERT INTO booking(booking_date, booking_status, customer_id, payment_id, Flight_id) values (%s, %s, %s, %s, %s)"""
    connection = connect()
    cursor = connection.cursor()
    criteria = ( booking.booking_date, booking.booking_status, booking.customer.customer_id, booking.payment.payment_id, booking.flight.Flight_id)
    cursor.execute(query, criteria)
    new_id = cursor.lastrowid
    booking.booking_id = new_id
    connection.commit()
    return booking

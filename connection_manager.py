import mysql.connector as sql_connector

def connect():
   connection = sql_connector.connect(
       host="localhost",
       user="root",
       passwd="Aditya@2008",
       database="flight_booking_system"
   )
   return connection

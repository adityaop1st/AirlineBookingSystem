from connection_manager import connect
import random

def create(name, email, phone, seat):
    query = """"INSERT INTO customer value(%s,%s,%s,%s, %s)"""

    connection = connect()
    cursor = connection.cursor()
    criteria = (random.random(), name,email,phone, seat)
    cursor.execute(query, criteria)
    data=cursor.fetchall()
    print(data)

    return data


from connection_manager import  connect

def login(user_name, password):

    query = """SELECT * FROM ACCOUNT WHERE USER_NAME = %s AND PASSWORD = %s"""
    connection = connect()
    cursor = connection.cursor()

    criteria = ( user_name, password)
    cursor.execute(query, criteria)
    data=cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

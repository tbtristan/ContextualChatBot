import mysql.connector
from mysql.connector import Error

class User:

  def __init__(self, username):
    data = self.__extractData(username)

    self.username               = data[0]
    self.evolution              = data[1]
    self.last_interaction_date  = data[2]
    self.creation_date          = data[3]
    self.fav_food               = data[4]
    self.hated_food             = data[5]
    self.persistent_sentiment   = data[6]
    self.hunger                 = data[7]
    self.playfulness            = data[8]


  def __create_server_connection(self, host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


  def __create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


  def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


  def __read_query(self, connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


  def __extractData(self, username) -> tuple:
    connection    = self.__create_db_connection("localhost", "root", "kmelvin562!", "user_states")
		
		# returns a tuple of size 1 with member 1 or 0
		# 1 = user exists in DB , 0 = user DNE in DB
    query_exists  =  """SELECT username FROM user_states WHERE EXISTS(SELECT username FROM user_states WHERE username='{}');""".format(username)

  ## Extracts profile data from existing row
    if self.__read_query(connection, query_exists)[0] == 1:
      return self.__extractProfile(connection, username)
 
  ## Creates profile data and extracts it
    query_insert    = """ INSERT INTO user_states(username) VALUES({})""".format(username)
    self.__execute_query(connection, query_insert)
    return self.__extractProfile(connection, username)
  

  def __extractProfile(self, connection, username) -> tuple:
    query_data    = """SELECT * FROM user_states WHERE username = '{}';""".format(username)
    results = self.__read_query(connection, query_data)
    print(results[0])
    return results[0]
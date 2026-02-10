# Simple PostgreSQL database connection
import psycopg2
from psycopg2 import OperationalError

def create_pg_connection(host, database, user, password, port=5432):
	"""Create a database connection to a PostgreSQL database with credentials."""
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=database,
			user=user,
			password=password,
			port=port
		)
		print(f"Connected to PostgreSQL database: {database} at {host}:{port}")
	except OperationalError as e:
		print(f"Error connecting to PostgreSQL database: {e}")
	return conn

if __name__ == "__main__":
	# Example credentials (replace with your actual credentials)
	HOST = "localhost"
	DATABASE = "your_db"
	USER = "your_user"
	PASSWORD = "your_password"
	PORT = 5432

	connection = create_pg_connection(HOST, DATABASE, USER, PASSWORD, PORT)
	if connection:
		connection.close()
		print("Connection closed.")

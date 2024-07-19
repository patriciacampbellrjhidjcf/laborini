import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabasename"
)

# Check if the connection was successful
if mydb.is_connected():
  print("Connected to the database")
else:
  print("Failed to connect to the database")

# Create a SQLite3 database and table
# import the sqlite3 library
import csv
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands

with conn as connection:
	c = conn.cursor()
	# import csv file
	employees = csv.reader(open("employees.csv", "rU"))
	
	# create a table named employees
	# c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	# insert data into tables
	## c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

	# Searching
	# for row in c.execute("SELECT firstname, lastname from employees"):
	# 	print(row)
	
	# fetchall() retrieves all records from query
	rows = c.execute("SELECT city, state from population")

	# outputs the rows to the screen, row by row
	for r in rows:
		print(r[0], r[1])

	# Error handling
	try:
		cities = [('WOahah', 'WH', 231321), ('JAbaHUT', 'JH', 1233333), ('OMKoook', 'OK', 48923432)]
		c.executemany('INSERT INTO populations VALUES(?, ?, ?)', cities)
	except:
		print("Something went wrong, oops!")


# commit changes
conn.commit()

# close the database connection
conn.close()
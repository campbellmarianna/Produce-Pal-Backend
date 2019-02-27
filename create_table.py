import sqlite3

#inatilaize database
connection = sqlite3.connect('data.db')

#Cursor allows us to select things
cursor = connection.cursor()

#Create table using a sting as a sql command and pass through the schema
create_table = "CREATE TABLE IF NOT EXISTS markets ( Name text, location text)"
cursor.execute(create_table)

# Insert one market
market = ('Ferry Building Farmers Market', 'One Ferry Building #50, San Francisco, CA 94111')
insert_query_M = "INSERT INTO markets VALUES (?, ?)"
cursor.execute(insert_query_M, market)

##INsert many Markets
markets = [
    ('Alamany', 'Alamany Blvd, SF'),
    ('NOPA', 'Baker St, SF'),
    ('SFSU', '100 Holloway Drive, SF')
]

cursor.executemany(insert_query_M, markets)

create_table_U = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_U)


# user Test data:
users = {
    (1, 'alien', 'asdf'),
    (2, 'mar', 'jkl;'),
    (3, 'skippy', 'jackass')

}

# User insert query
insert_query_U = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query_U, users)

# select_query = "SELECT * FROM markets"
# for row in cursor.execute(select_query):
#     print(row)

# commit to the database
connection.commit()
# Close filter
connection.close()

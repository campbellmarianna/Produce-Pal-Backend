import sqlite3

#inatilaize database
connection = sqlite3.connect('data.db')

#Cursor allows us to select things
cursor = connection.cursor()

#Create table using a sting as a sql command and pass through the schema
create_table = "CREATE TABLE IF NOT EXISTS markets (id INTIGER NOT NULL PRIMARY KEY, Name text, location text)"
cursor.execute(create_table)

# Eventually the create table will be:
# create_table = "CREATE TABLE markets(_id int, Market_name text, Address text, lat_long numeric, day_time text, website text, venders_id int )"


# Insert one market
market = (1, 'Ferry Building Farmers Market', 'One Ferry Building #50, San Francisco, CA 94111')
insert_query = "INSERT INTO markets VALUES (?, ?, ?)"
cursor.execute(insert_query, market)


##INsert many Markets
markets = [
    (2, 'Alamany', 'Alamany Blvd, SF'),
    (3, 'NOPA', 'Baker St, SF'),
    (4, 'SFSU', '100 Holloway Drive, SF')
]

cursor.executemany(insert_query, markets)

select_query = "SELECT * FROM markets"
for row in cursor.execute(select_query):
    print(row)

# commit to the database
connection.commit()
# Close filter
connection.close()

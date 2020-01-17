
#   This module builds the database and inserts the initial data from the configuration file.
#   When run, it will be given a configuration file as an argument.
#   For example: python3 initiate.py config.txt
#   If the database file already exists remove it.
import sqlite3


# will create a connection to a file base database stored in 'mydb.db' file
# if the file does not exist, it will be created
conn = sqlite3.connect('moncafe.db')
conn.text_factory = bytes

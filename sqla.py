# create a sqllite database and table

# import sqllite3 library
import sqlite3

#create database if it doesnt exist
conn = sqlite3.connect("new.db")

#get a cursor object to execute sql commands
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

#CLOSE DB CONNECTION 

conn.close()
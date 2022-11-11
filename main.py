#!/usr/bin/env python

import mysql.connector
from dotenv import load_dotenv
import os

# load variables from .env file
load_dotenv()
# I like to declare global variable on top of the file as best practice
connection = None


def create(name):
    print("CREATE")

    cursor = connection.cursor()
    sql = "INSERT INTO customers (name) VALUES (%s)"
    cursor.execute(sql, (name,))
    cursor.close()

    connection.commit()


def read(name):
    print("READ:\t", end="")

    cursor = connection.cursor()
    sql = "SELECT * FROM customers WHERE name = %s"
    cursor.execute(sql, (name,))

    items = cursor.fetchall()

    cursor.close()
    print(items)


def update(name, revenue):
    print("UPDATE")

    cursor = connection.cursor()
    sql = "UPDATE customers SET revenue = %s WHERE name = %s"
    cursor.execute(sql, (revenue, name,))
    cursor.close()

    connection.commit()


def delete(name):
    print("DELETE")

    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE name = %s"
    cursor.execute(sql, (name,))
    cursor.close()

    connection.commit()


def main():
    global connection

    # connect to the db
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
        )

        # create and/or open database and table
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS test;")
        cursor.execute("USE test;")
        cursor.execute("CREATE TABLE IF NOT EXISTS customers ( name VARCHAR(20) NOT NULL, revenue DECIMAL );")
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        exit(1)


    # ask for inputs
    name = input("Customer name: ")
    revenue = input("Customer revenue: ")
    print("")

    # use CRUD methods
    read(name)
    create(name)
    read(name)
    update(name, revenue)
    read(name)
    delete(name)
    read(name)

    connection.close()

if __name__ == "__main__":
    main()

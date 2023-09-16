# from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]


# def get_all_customers():
#     return CUSTOMERS

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
            FROM Customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])

            # see the notes below for an explanation on this line of code.
            customers.append(customer.__dict__)

    return customers


# Function with a single parameter
# def get_single_customer(id):
#     # Variable to hold the found customer, if it exists
#     requested_customer = None

#     # Iterate the CUSTOMERS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for customer in CUSTOMERS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'],)

        return customer.__dict__


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


# def delete_customer(id):
#     # Initial -1 value for customer index, in case one isn't found
#     customer_index = -1

#     # Iterate the CUSTOMERS list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, customer in enumerate(CUSTOMERS):
#         if customer["id"] == id:
#             # Found the customer. Store the current index.
#             customer_index = index

#     # If the customer was found, use pop(int) to remove it from list
#     if customer_index >= 0:
#         CUSTOMERS.pop(customer_index)

def delete_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))


# def update_customer(id, new_customer):
#     # Iterate the CUSTOMERS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, customer in enumerate(CUSTOMERS):
#         if customer["id"] == id:
#             # Found the customer. Update the value.
#             CUSTOMERS[index] = new_customer
#             break

def update_customer(id, new_customer):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Customer
            SET
                name = ?,
                address = ?,
                email = ?,
                password = ?
        WHERE id = ?
        """, (new_customer['name'], new_customer['address'],
              new_customer['email'], new_customer['password'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

# TODO: you will get an error about the address on customer. Look through the customer model and requests to see if you can solve the issue.


def get_customer_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return customers

from .animal_requests import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animal_by_location, get_animal_by_status
from .location_request import get_all_locations, get_single_location, create_location, delete_location, update_location
from .employee_request import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee, get_employee_by_location
from .customer_request import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer, get_customer_by_email
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

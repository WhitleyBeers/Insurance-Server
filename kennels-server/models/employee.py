class Employee():

    def __init__(self, id, name, address, location_id=""):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.location = None

     #   new_employee = Employee(1, "Jenna Solis")

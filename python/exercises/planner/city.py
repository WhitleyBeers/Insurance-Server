class City:

    def __init__(self, established):
        self.city = ""
        self.mayor = ""
        self.established = established
        self.buildings = ""


nashville_tn = City(1806)
nashville_tn.city = "Nashville"
nashville_tn.mayor = "John Cooper"
nashville_tn.buildings = ["Batman", "Bridgestone", "Hilton", "Courthouse"]

print(f'Current Building List {nashville_tn.buildings}')

new_building = input("Enter A New Building: ")

nashville_tn.buildings.append(new_building)

print(f'Updated building list {nashville_tn.buildings}')

print(f'{nashville_tn.city} was established in {nashville_tn.established}, the mayor is {nashville_tn.mayor}! in addition these are some of the most popular buildings.  {" , ".join(nashville_tn.buildings)}! ')

import datetime

allBuildings = []


class Building:

    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = "DeAndre Hill"
        self.date_constructed = ""
        self.owner = ""
        allBuildings.append(self)

    def purchased(self, owner):
        self.owner = owner

    def contruct(self):
        self.date_constructed = datetime.datetime.now()


first_buy = Building("2099 8th ave", 15)
first_buy.purchased = ("12/23/2019")
first_buy.owned_by = ("Lucy May")
first_buy.contruct()

second_buy = Building("35th polk ave", 10)
second_buy.purchased = ("7/03/2022")
second_buy.owned_by = ("Charles Long")
second_buy.contruct()

third_buy = Building("185 division dr", 8)
third_buy.purchased = ("9/08/2012")
third_buy.owned_by = ("Gilbert Burns")
third_buy.contruct()

fourth_buy = Building("12th ave s", 18)
fourth_buy.purchased = ("1/15/2020")
fourth_buy.owned_by = ("Tracy Puns")
fourth_buy.contruct()

fifth_buy = Building("6th and MLK", 22)
fifth_buy.purchased = ("7/19/2016")
fifth_buy.owned_by = ("Bobby Portis")
fifth_buy.contruct()

print(f'{first_buy.address} was purchased by {first_buy.owned_by} on {first_buy.purchased} at {first_buy.date_constructed} and has {first_buy.stories} stories')

print(f'{second_buy.address} was purchased by {second_buy.owned_by} on {second_buy.purchased} at {second_buy.date_constructed} and has {second_buy.stories} stories')

print(f'{third_buy.address} was purchased by {third_buy.owned_by} on {third_buy.purchased} at {third_buy.date_constructed} and has {third_buy.stories} stories')

print(f'{fourth_buy.address} was purchased by {fourth_buy.owned_by} on {fourth_buy.purchased} at {fourth_buy.date_constructed} and has {fourth_buy.stories} stories')

print(f'{fifth_buy.address} was purchased by {fifth_buy.owned_by} on {fifth_buy.purchased} at {fifth_buy.date_constructed} and has {fifth_buy.stories} stories')

class Pizza:

    def __init__(self):
        self.type = ""
        self.size = ""
        self.crust = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)


chicken_bbq = Pizza()
chicken_bbq.size = 12
chicken_bbq.crust = "pan"
chicken_bbq.add_topping("chicken")
chicken_bbq.add_topping("bbq sauce")

pepperoni_pizza = Pizza()
pepperoni_pizza.size = 16
pepperoni_pizza.crust = "stuffed"
pepperoni_pizza.add_topping("pepperoni")
pepperoni_pizza.add_topping("ham")


print(
    f'I would like a {chicken_bbq.size}-inch, {chicken_bbq.crust} pizza with {" and ".join(chicken_bbq.toppings)}')
print(f'I would like a {pepperoni_pizza.size}-inch, {pepperoni_pizza.crust} crust pizza with {" and ".join(pepperoni_pizza.toppings)}')

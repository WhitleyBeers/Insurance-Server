from animals import Penguin, PaintedDog
from habitats import Aquarium

# Create a penguin and dog
bob = Penguin("Bob")
ralph = PaintedDog("Ralph")

seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)
seaworld.add_swimmer_type_check(ralph)

for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')

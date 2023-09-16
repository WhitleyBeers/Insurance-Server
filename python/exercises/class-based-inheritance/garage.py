class Vehicle:

    def __init__(self, color, doors, kind, horn):
        self.color = color
        self.doors = doors
        self.kind = kind
        self.horn = horn

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f'Your vehicle hit a {direction}')

    def stop(self):
        print('Your whip just stopped!')


class Chevy(Vehicle):

    def __init__(self, color, doors, kind, horn):
        super().__init__(color, doors, kind, horn)

    def drive(self):
        print(f"The {self.color} car speeds past. RRrrrrrummbbble!")

    def stop(self):
        print(f"the {self.kind} car came to a quick stop")


class Dodge(Vehicle):

    def __init__(self, color, doors, kind, horn):
        super().__init__(color, doors, kind, horn)

    def turn(self, direction):
        print(f'Your {self.color} Dodge hit a {direction}')

    def drive(self):
        print(f"the dodge sped off, VROOOOOOOM")


class Ford(Vehicle):

    def __init__(self, color, doors, kind, horn):
        super().__init__(color, doors, kind, horn)

    def drive(self):
        print(f"The {self.color} Ford burnt away, RRRUUUmmmblleeeeee")

    def stop(self):
        print(
            f'The {self.color} Ford rolls to a stop after speeding a mile down the runway.')


class Nissan(Vehicle):

    def __init__(self, color, doors, kind, horn):
        super().__init__(color, doors, kind, horn)

    def drive(self):
        print(f"The {self.color} out Nissan ran a stop light, HmmmmmmmHmmmmmmm")

    def turn(self, direction):
        print(f'The Nissan almost crashed turning {direction}.')


class BMW(Vehicle):

    def __init__(self, color, doors, kind, horn):
        super().__init__(color, doors, kind, horn)

    def drive(self):
        print(
            f"Did you see how fast that {self.color} car went, Vvvvvvvvrrooooommmm")

    def turn(self, direction):
        print(
            f'The {self.color} BMW turned {direction} without using their blinker.')


corvette = Chevy("white", 2, "sports", "honkkkkk")
hellcat = Dodge("black", 4, "muscle", "honkkkkk")
mustang = Ford("purple", 2, "muscle", "beep beeeeep")
altima = Nissan("black", 4, "mid-size", "beepppp")
m3 = BMW("siver", 4, "sports", "honk honk")

corvette.drive()
hellcat.drive()
mustang.drive()
altima.drive()
m3.drive()

corvette.stop()
hellcat.stop()
mustang.stop()
altima.stop()
m3.stop()

corvette.turn('left')
hellcat.turn('right')
mustang.turn('left')
altima.turn('right')
m3.turn('left')

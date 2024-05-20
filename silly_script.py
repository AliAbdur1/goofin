bullshit = 4 + 2
print(bullshit)
goofstring = "skjdbfkjsbdfkjbskajfbkjsndaf"
def getstringnum(string):
    startval = 0
    for i in string:
        startval += 1
        print(startval)
    return startval
getstringnum(str(bullshit))

class Man:
    def __init__(self, name, color, height, weight):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight

    @classmethod
    # classmethods need the cls in the perameters
    def training(cls, person, weightlost):
        person.weight -= weightlost
        print(f"after training, {person.name} now weighs {person.weight} pounds")
        return person

dude1 = Man("Samuel","black","5'9",179)
dude2 = Man("Bobby", "white", "6'6", 237)
print(dude1.name)
dude1 = Man.training(dude1, 67)
dude2 = Man.training(dude2, 56)
        
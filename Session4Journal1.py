
class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length        # float
        self.leg_length = leg_length        # float
        self.num_eyes = num_eyes            # int
        self.has_tail = has_tail            # bool
        self.is_furry = is_furry            # bool

    #print and describe the physical characteristics
    def describe(self):
        print("Animal Characteristics:")
        print(f"Length of arms: {self.arm_length} units")
        print(f"Length of legs: {self.leg_length} units")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Does it have a tail? {'Yes' if self.has_tail else 'No'}")
        print(f"Is it furry? {'Yes' if self.is_furry else 'No'}")

# Create an instance of the FavoriteAnimal class
my_favorite_animal = FavoriteAnimal(arm_length=1.8, leg_length=1.3, num_eyes=2, has_tail=False, is_furry=True)

# Call the describe function to print the characteristics of the animal
my_favorite_animal.describe()

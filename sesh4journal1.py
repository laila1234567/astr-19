class Capybara:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    
    def describe(self):
        print("Capybara Physical Characteristics:")
        print(f"Arm Length: {self.arm_length} meters")
        print(f"Leg Length: {self.leg_length} meters")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has a Tail: {self.has_tail}")
        print(f"Is Furry: {self.is_furry}")

#Creating an instance of Capybara class
capybara = Capybara(0.4, 0.5, 2, True, True)

#Calling the describe method
capybara.describe()

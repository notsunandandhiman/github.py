class Dog:
    # Class variable
    species = "Canis lupus familiaris"  # All dogs belong to this species

    def __init__(self, breed, name):
        # Instance variables
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print()  # For better readability


# Creating instances of Dog for two different breeds
dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("Bulldog", "Max")

# Displaying details of the dogs
dog1.display_details()
dog2.display_details()
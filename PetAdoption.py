import random as rd

# Preferences
PREFERENCES = {
    "Dog": ("Bones", "Walk"),
    "Cat": ("Fish", "Nap")
}

# Base class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print()
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        if self.species in PREFERENCES:
            print(f"Preferences: {PREFERENCES[self.species]}")

# Dog subclass
class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

# Cat subclass
class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

# Adoption system
class Adoption:
    def __init__(self):
        self.pets = {}

    def add_pet(self, pet):
        pet_id = rd.randint(1, 1000)
        while pet_id in self.pets:
            pet_id = rd.randint(1, 1000)
        self.pets[pet_id] = pet
        print(f"Pet added with ID: {pet_id}")

    def adopt_pet(self, pet_id):
        if pet_id in self.pets:
            pet = self.pets.pop(pet_id)
            print(f"Congratulations! You have adopted {pet.name}")
        else:
            print("Pet ID not found. Please try again")

    def view_pets(self):
        if not self.pets:
            print("No pets available for adoption")
            return
        print("Available Pets:")
        for pet_id, pet in self.pets.items():
            print(f"ID: {pet_id}")
            pet.display_info()

adoption = Adoption()
while True:
    print()
    print("--- Welcome to Pet Adoption System ---")
    print("1. Add a Pet")
    print("2. Adopt a Pet")
    print("3. View Pets")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        species = input("Enter pet species (Dog/Cat): ").title()
        print(species)
        name = input("Enter pet name: ")
        try:
            age = int(input("Enter pet age: "))
        except ValueError:
            print("Invalid age. Must be a number.")
            continue
        breed = input("Enter pet breed: ")
        color = input("Enter pet color: ")

        if species == "Dog":
            pet = Dog(name, age, breed, color)
        elif species == "Cat":
            pet = Cat(name, age, breed, color)
        else:
            print("Invalid species. Please enter Dog or Cat.")
            continue

        adoption.add_pet(pet)

    elif choice == 2:
        try:
            pet_id = int(input("Enter pet ID to adopt: "))
        except ValueError:
            print("Invalid ID. Must be a number.")
            continue
        adoption.adopt_pet(pet_id)

    elif choice == 3:
        adoption.view_pets()

    elif choice == 4:
        print("Thank you for using the Pet Adoption System!")
        break

    else:
        print("Invalid choice. Please try again.")


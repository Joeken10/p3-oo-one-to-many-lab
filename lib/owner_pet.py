class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    
    def __repr__(self):
        return f"Pet name: {self.name}, type: {self.pet_type}, owner: {self.owner.name if self.owner else 'No Owner'}"

    
class Owner:
    def __init__(self, name):
        self.name = name if name else "Unknown Owner" 

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


# Creating multiple Owners
owner1 = Owner("John")
owner2 = Owner("Jim")
owner3 = Owner("Ben")

# Creating Pets
dog = Pet("Buddy", "dog")
cat = Pet("Whiskers", "cat")
rodent = Pet("Jim Jr.", "rodent")
bird = Pet("Lucky", "bird")
reptile = Pet("Jerry", "reptile")
exotic = Pet("Clifford", "exotic")


owner1.add_pet(dog)      
owner1.add_pet(bird)     

owner2.add_pet(cat)      
owner2.add_pet(rodent)   

owner3.add_pet(reptile)  
owner3.add_pet(exotic)   


print(f"Sorted pets of {owner1.name}: {owner1.get_sorted_pets()}")
print(f"Sorted pets of {owner2.name}: {owner2.get_sorted_pets()}")
print(f"Sorted pets of {owner3.name}: {owner3.get_sorted_pets()}")

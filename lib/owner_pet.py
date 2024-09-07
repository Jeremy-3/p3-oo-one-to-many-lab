class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self,name,pet_type,owner = "John"):
        self.name = name
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet is not classified under PET_TYPES")
        self.pet_type = pet_type
        Pet.all.append(self) 






class Owner:
    def __init__(self,name):
        self.name = name
        self._pets = []
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise Exception("pet has not been added")
        pet.owner = self    
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p :p.name)
            
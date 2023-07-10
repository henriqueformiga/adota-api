class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'breed': self.breed
        }

    @staticmethod
    def from_dict(data):
        name = data['name']
        age = data['age']
        breed = data['breed']
        return Pet(name, age, breed)

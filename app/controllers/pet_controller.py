from flask import Blueprint, request, current_app, jsonify
from app.models.Pet import Pet

pet_controller = Blueprint('pet', __name__)

@pet_controller.route('/pets', methods=['POST'])
def create_pet():
    data = request.json
    pet = Pet(data['name'], data['age'], data['breed'])
    current_app.db.pets.insert_one(pet.to_dict())
    return jsonify({'message': 'Pet created successfully'}), 201

@pet_controller.route('/pets', methods=['GET'])
def get_all_pets():
    pets_data = current_app.db.pets.find()
    pets = [Pet.from_dict(pet) for pet in pets_data]
    return jsonify({'pets': [pet.to_dict() for pet in pets]})

@pet_controller.route('/pets/<pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet_data = current_app.db.pets.find_one({'_id': pet_id})
    if pet_data:
        pet = Pet.from_dict(pet_data)
        return jsonify(pet.to_dict())
    return jsonify({'error': 'Pet not found'}), 404

@pet_controller.route('/pets/<pet_id>', methods=['PUT'])
def update_pet(pet_id):
    data = request.json
    pet_data = current_app.db.pets.find_one({'_id': pet_id})
    if pet_data:
        pet = Pet.from_dict(pet_data)
        pet.name = data['name']
        pet.age = data['age']
        pet.breed = data['breed']
        current_app.db.pets.update_one({'_id': pet_id}, {'$set': pet.to_dict()})
        return jsonify({'message': 'Pet updated successfully'})
    return jsonify({'error': 'Pet not found'}), 404

@pet_controller.route('/pets/<pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    result = current_app.db.pets.delete_one({'_id': pet_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Pet deleted successfully'})
    return jsonify({'error': 'Pet not found'}), 404

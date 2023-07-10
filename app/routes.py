from app.controllers.pet_controller import pet_controller
from app.controllers.auth_controller import auth_controller


def register_auth_routes(app):
    app.register_blueprint(auth_controller, url_prefix='/api/auth')
    app.register_blueprint(pet_controller, url_prefix='/api/pets')
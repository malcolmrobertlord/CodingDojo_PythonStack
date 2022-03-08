from flask_app import app
from flask_app.controllers import friend_controller, pet_controller


if __name__ == "__main__":
    app.run(debug=True)


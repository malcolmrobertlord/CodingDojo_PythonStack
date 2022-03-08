from flask_app import app
from flask_app.controllers import team_controller
from flask_app.controllers import owner_controller
from flask_app.controllers import user_controller


if __name__ == "__main__":
    app.run(debug=True)
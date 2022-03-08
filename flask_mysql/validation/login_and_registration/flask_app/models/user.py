from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
bcypt = Bcrypt(app)

class User:
    db = "login_registration_db"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_user(user):
        is_valid=True
        if len(user['fname']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(User.one_email(user)) == 1:
            flash("Email is already registered")
            is_valid = False
        if (user['password1'] != user['password2']):
            flash("Passwords do not match")
            is_valid = False
        return is_valid
    
    
    #class method to check if email exists
    @classmethod
    def one_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("login_registration_db").query_db(query, data)
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        if len(users) < 1:
            print (False)
            return False
        # print (users)
        return cls(results[0])
    
    
    #class method to check if email exists alternate
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration_db").query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    
    #saves user into db
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        results = connectToMySQL("login_registration_db").query_db(query, data)
        return results
    
    
    #get user information based on id
    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("login_registration_db").query_db(query, data)
        return cls(results[0])
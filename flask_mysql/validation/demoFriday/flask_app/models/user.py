from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
bcypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    # Method to validate user registration
    @staticmethod
    def validate_user(user):
        is_Valid = True
        if len(user['first_name']) < 1:
            flash("Your first name must have one character")
            is_Valid = False
        if len(user['last_name']) < 1:
            flash("Your last name must have one character")
            is_Valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("That's not a valid email address")
            is_Valid = False
        if len(user['password']) < 8:
            flash("Your password must have 8 characters or more")
            is_Valid = False
        if (user['password'] != user['confirm_password']):
            flash("Passwords do not match")
            is_Valid = False
        return is_Valid
    
    
    #Method to save user into db
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        results = connectToMySQL("sportsdb").query_db(query, data)
        return results
    
    
    #get user information based on id
    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("sportsdb").query_db(query, data)
        return cls(results[0])
    
    #class method to check if email exists (grab user by email)
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
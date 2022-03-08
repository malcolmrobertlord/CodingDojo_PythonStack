from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash


class Show:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    
    # Method to validate a show
    @staticmethod
    def validate_show(show):
        is_Valid = True
        if len(show['title']) < 3:
            flash("You must have a title with at least 3 characters")
            is_Valid = False
        if len(show['network']) < 3:
            flash("You must have a network with at least 3 characters")
            is_Valid = False
        if len(show['description']) < 3:
            flash("You must have a description with at least 3 characters")
            is_Valid = False
        return is_Valid
    

    # Method to get all shows
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL("tv_show_db").query_db(query)
        # Create an empty list to append our instances of shows
        all_shows = []
        # Iterate over the db results and create instances of shows with cls.
        for shows in results:
            all_shows.append(Show(shows))
        # print(all_shows)
        return all_shows
    
    # Method to add show
    @classmethod
    def save_show(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, created_at, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), %(user_id)s);"
        results = connectToMySQL("tv_show_db").query_db(query, data)
        return results
    
    #method to display show information
    @classmethod
    def one_show(cls,data):
        query = "SELECT * FROM shows WHERE id = %(show_id)s;"
        results = connectToMySQL("tv_show_db").query_db(query, data)
        return cls(results[0])
    
    #method to edit show
    @classmethod
    def edit_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL("tv_show_db").query_db(query, data)
        return results
    
    # method to delete show
    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        results = connectToMySQL("tv_show_db").query_db(query, data)
        return results
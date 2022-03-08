# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    db = "friends_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of friends
        all_friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            all_friends.append( Friend(friend) )
        print(all_friends)
        return all_friends

    @classmethod
    def one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("friends_schema").query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, age, created_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW());"
        results = connectToMySQL("friends_schema").query_db(query, data)
        return results

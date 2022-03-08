from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of friends
        all_dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojos in results:
            all_dojos.append( Dojo(dojos) )
        print(all_dojos)
        return all_dojos

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW());"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results
    
    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(results[0])
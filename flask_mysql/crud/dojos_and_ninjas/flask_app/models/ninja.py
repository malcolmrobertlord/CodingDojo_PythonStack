from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of friends
        all_ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninjas in results:
            all_ninjas.append( Ninja(ninjas) )
        print(all_ninjas)
        return all_ninjas

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), %(dojo_id)s);"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results

    @classmethod
    def one_dojo_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo_ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninjas in results:
            dojo_ninjas.append( Ninja(ninjas) )
        print(dojo_ninjas)
        return dojo_ninjas
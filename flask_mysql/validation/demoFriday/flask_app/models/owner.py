from flask_app.config.mysqlconnection import connectToMySQL

class Owner:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    # Make an Owner
    @classmethod
    def save_owner(cls, data):
        query = "INSERT INTO owners (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        new_id = connectToMySQL("sportsdb").query_db(query,data)
        return new_id
    
    
    # Get all owners
    @classmethod
    def all_owners(cls):
        query = "SELECT * FROM owners;"
        results = connectToMySQL("sportsdb").query_db(query)
        all_owners = []
        for owner in results:
            all_owners.append(cls(owner))
        return all_owners
    
    # view one owner
    @classmethod
    def one_owner(cls):
        query = "SELECT * FROM owners WHERE id = %(id)s;"
        results = connectToMySQL("sportsdb").query_db(query, data)
        return cls(results[0])

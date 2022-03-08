from flask_app.config.mysqlconnection import connectToMySQL

class Team:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.sport = data['sport']
        self.champs = data['champs']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    # get all teams
    @classmethod
    def all_teams(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL("sportsdb").query_db(query)
        all_teams = []
        for teams in results:
            all_teams.append(cls(teams))
        return all_teams


    # Get one team
    
    
    
    # save creating team
    
    @classmethod
    def save_team(cls, data):
        query = "INSERT INTO teams (name, location, sport, champs, created_at) VALUES (%(name)s, %(location)s, %(sport)s,%(champs)s, NOW());"
        new_id = connectToMySQL("sportsdb").query_db(query, data)
        return new_id
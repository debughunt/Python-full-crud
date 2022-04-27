from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojos:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def new_dojo(cls , data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES (%(name)s,NOW(),NOW());"
        dojo_id = connectToMySQL(cls.db).query_db( query, data)
        return dojo_id   

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojos_friends(cls, data):
        print("inside dojos function")
        print(data)
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
                "id" : data["ninjas.id"],
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "age" : data["age"],
                "created_at" : data["ninjas.created_at"],
                "updated_at" : data["ninjas.updated_at"]
            }
            ninja_instance = ninjas.Ninjas(ninja_data)
            dojo.ninjas.append(ninja_instance)
        return dojo

from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app.models.model_ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.all_ninjas=[]

    @classmethod
    def get_all_dojos(cls):
        query = '''
                SELECT * FROM dojos
                '''
        obj_dojos=[]
        dojos_from_db = connectToMySQL("dojos_and_ninjas").query_db(query)
        for dojo in dojos_from_db:
            obj_dojos.append(cls(dojo))
        return obj_dojos

    @classmethod
    def create_dojo(cls,data):
        print(data)
        query = '''
                    INSERT INTO dojos (name) 
                    VALUES (%(name)s)
                '''
        dojo_created = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return dojo_created

    @classmethod
    def get_all_ninjas_dojo(cls,data):
        query = '''
                SELECT ninjas.id, first_name,last_name,age,ninjas.created_at,ninjas.update_at,ninjas.dojo_id FROM dojos
                JOIN ninjas ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;
                '''
        response_query = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        ninjas = []
        for ninja in response_query:
            ninja_obj = Ninja(ninja)
            ninjas.append(ninja_obj)
        return ninjas 
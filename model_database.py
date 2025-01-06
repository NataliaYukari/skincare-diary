from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure, DuplicateKeyError, OperationFailure
from model_authentication import Authentication



class Database:
    def __init__(self):
        url = "mongodb+srv://nataliakawashisa:bananinha@ifpr.tffr4.mongodb.net/?retryWrites=true&w=majority&appName=IFPR"
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.database = self.client["skincare_diary"]
        self.authentication = Authentication()
        self.activeUser = None

    def create_user(self, user_data):
            collection = self.database["Users"]

            query = {
                "name": user_data.username,
                "password": user_data.password,
                "email": user_data.email,
                "birthday": user_data.birthday,
                "skinType": user_data.skinType,
                "sensibility": user_data.sensitivity
            }

            unique_index = "name"

            try:
                collection.create_index(unique_index, unique= True)

            except OperationFailure as error:
                print(f"CLASSDATABASE - Falha ao criar o índice único: {error}")

            try:
                action = collection.insert_one(query)
                return True, {"title": "Cadastrado", "description": ""}
            
            except DuplicateKeyError:
                print("CLASSDATABASE - chave duplicada")
                return False, {"title": "cadastrar", 
                               "description": "O usuário já existe"}
        
    def validate_login(self, login, password):
        return self.authentication.validate_login(login, password)

    def get_user_data(self, username):
        collection = self.database["Users"]

        try:
            self.activeUser = collection.find_one({"name": username})
            return self.activeUser

        except Exception as error:
            print("CLASSDATABASE - erro ao procurar dados do usuário")


    def save_routine(self, routine):
        collection = self.database["Routines"]

        query = {
            "user_id": self.activeUser["_id"],
            "cleanser": routine.cleanser,
            "treatmentAM": routine.treatmentAM,
            "moisturizerAM": routine.moisturizerAM,
            "sunscreen": routine.sunscreen,
            "treatmentPM": routine.treatmentPM,
            "moisturizerPM": routine.moisturizerPM
        }

        try:
            action = collection.insert_one(query)
            print("CLASSDATABASE - rotina salva")
            return True
        
        except OperationFailure as error:
            print("CLASSDATABaSE - falha ao salvar rotina")
            return False
            
    def get_routine(self, username):
        collection = self.database["Routines"]

        try:
            routine = collection.find_one({"name": username})
            print("CLASSDATABASE - rotina encontrada")
            return routine
        
        except Exception as error:
            print("CLASSDATABASE - rotina não encontrada")
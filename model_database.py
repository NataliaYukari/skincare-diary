from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure, DuplicateKeyError, OperationFailure
from model_authentication import Authentication
import gridfs



class Database:
    def __init__(self):
        url = "mongodb+srv://nataliakawashisa:bananinha@ifpr.tffr4.mongodb.net/?retryWrites=true&w=majority&appName=IFPR"
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.database = self.client["skincare_diary"]
        self.authentication = Authentication()
        self.activeUser = None

    def create_user(self, userData):
            collection = self.database["Users"]

            query = {
                "name": userData.username,
                "password": userData.password,
                "email": userData.email,
                "birthday": userData.birthday,
                "skinType": userData.skinType,
                "sensibility": userData.sensitivity
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
        collection = self.database["Users"]

        routineSubdocument = {
            "cleanser": routine.cleanser,
            "treatmentAM": routine.treatmentAM,
            "moisturizerAM": routine.moisturizerAM,
            "sunscreen": routine.sunscreen,
            "treatmentPM": routine.treatmentPM,
            "moisturizerPM": routine.moisturizerPM
        }

        try:
            action = collection.update_one(
                {"_id": self.activeUser["_id"]},
                {"$set": {"routine": routineSubdocument}}    
            )
            print("CLASSDATABASE - rotina salva")
            return True
        
        except OperationFailure as error:
            print("CLASSDATABASE - falha ao salvar rotina")
            return False
            
    def read_routine(self, username):
        collection = self.database["Users"]

        try:
            result = collection.find_one(
                {"name": username},
                {"_id": 0, "routine": 1}
            )

            if result and "routine" in result:
                print("CLASSDATABASE - rotina encontrada")
                return result["routine"]
            else:
                print("CLASSDATABASE - rotina não encontrada")
        
        except Exception as error:
            print("CLASSDATABASE - rotina não encontrada: ", error)

    def create_entry(self, entryData, user):
        collection = self.database["Entries"]
        fs = gridfs.GridFS(self.database, collection= "Entries")

        query = {
            "date": entryData.date
        }

        if entryData.description:
            query["description"] = entryData.description

        if entryData.image:
            try:
                with open(entryData.image, "rb") as imageFile:
                    fileId = fs.put(imageFile, filename = entryData.image.split("/")[-1])
                    query["image_id"] = fileId
                    print(f"CLASSDATABASE - imagem salva no gridFS com ID: {fileId}")

            except Exception as e:
                print("CLASSDATABASE - Erro ao salvar imagem:", e)

        try:
            action = collection.insert_one(query)
            entryId = action.inserted_id
            self.add_entry_to_diary(entryId, user)
            print("CLASSDATABASE - entrada salva")
            return True, {"title": "Sucesso!", "description": "Entrada salva"}
        
        except OperationFailure as error:
            print("CLASSDATABASE - falha ao salvar entrada") 
            return False, {"title": "Falha ao salvar", "description": error}

    def add_entry_to_diary(self, entryId, user):
        collection = self.database["Users"]

        try:
            action = collection.update_one(
                {"_id": user["_id"]},
                {"$push": {"diary": entryId}}
            )
            print("CLASSDATABASE - entrada salva no diário")
        
        except OperationFailure as error:
            print(f"CLASSDATABASE - erro ao salvar entrada no diário: {error}")



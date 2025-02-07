import base64
from bson import ObjectId
import gridfs
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import DuplicateKeyError, OperationFailure
from models.model_authentication import Authentication


class Database:
    """Handles database queries"""

    
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
                return False, error

            try:
                action = collection.insert_one(query)
                return True, None
            
            except DuplicateKeyError as error:
                print("CLASSDATABASE - chave duplicada")
                return False, error
        
    def validate_login(self, login, password):
        isValid, message = self.authentication.validate_login(login, password)

        if isValid:
            self.activeUser = login

        return isValid, message

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
            result = collection.update_one(
                {"_id": self.activeUser["_id"]},
                {"$set": {"routine": routineSubdocument}}    
            )
            print("CLASSDATABASE - rotina salva")
            return True
        
        except OperationFailure as error:
            print("CLASSDATABASE - falha ao salvar rotina")
            return False
            
    def read_routine(self, user):
        collection = self.database["Users"]

        try:
            result = collection.find_one(
                {"name": user},
                {"_id": 0, "routine": 1}
            )

            if result and "routine" in result:
                print("CLASSDATABASE - rotina encontrada")
                return result["routine"]
            else:
                print("CLASSDATABASE - rotina não encontrada")
        
        except Exception as error:
            print("CLASSDATABASE - rotina não encontrada: ", error)

    def create_entry(self, entryData, userName):
        collection = self.database["Entries"]
        fs = gridfs.GridFS(self.database)

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

            except Exception as error:
                print("CLASSDATABASE - Erro ao salvar imagem:", error)

        try:
            result = collection.insert_one(query)
            entryId = result.inserted_id
            self.add_entry_to_diary(entryId, userName)
            print("CLASSDATABASE - entrada salva no banco de entradas")
            return True, None
        
        except OperationFailure as error:
            print("CLASSDATABASE - falha ao salvar entrada") 
            return False, error

    def add_entry_to_diary(self, entryId, user):
        collection = self.database["Users"]

        try:
            action = collection.update_one(
                {"name": user},
                {"$push": {"diary": entryId}}
            )
            print("CLASSDATABASE - entrada salva no diário do usuário")
        
        except OperationFailure as error:
            print(f"CLASSDATABASE - erro ao salvar entrada no diário: {error}")

    def get_diary(self, userName):
        users_collection = self.database["Users"]
        entries_collection = self.database["Entries"]

        try:
            user = users_collection.find_one({"name": userName})

            if user:
                diary = user.get("diary")

                if diary and isinstance(diary, list):
                    entries = list(entries_collection.find(
                        {"_id": {"$in": diary}}
                    )) 
                    print("CLASSDATABASE - Entradas do diário recuperadas")
                    return entries
                else:
                    print("CLASSDATABASE - Nenhuma entrada encontrada")
            else:
                print("CLASSDATABASE - Atributo diário não possui uma lista válida")

        except OperationFailure as error:
            print(f"CLASSDATABASE - Entradas do diário não puderam ser recuperadas: {error}")

    def get_entry(self, entryId):
        entries_collection = self.database["Entries"]

        try:
            entryData = entries_collection.find_one({"_id": entryId})
            print("CLASSDATABASE - Entrada encontrada")
            
            if "image_id" in entryData:
                    imageId = entryData["image_id"]
                    imageBase64 = self.get_entry_image(imageId)
            else:
                imageBase64 = None

            return entryData, imageBase64
        
        except Exception as error:
            print(f"CLASSDATABASE - Erro ao procurar entrada: {error}")

    def get_entry_image(self, imageId):
        fs = gridfs.GridFS(self.database)

        try:
            fileData = fs.get(imageId)
            binaryData = fileData.read()
            imageBase64 = base64.b64encode(binaryData).decode('utf-8')

            print(f"CLASSDATABASE - Imagem recuperada")
            return imageBase64
        
        except Exception as error:
            print(f"CLASSDATASE - Erro ao recuperar imagem: {error}")
            
    def delete_entry(self, entry):
        entries_collection = self.database["Entries"]

        try:
            filter = {"_id": ObjectId(entry)}
            result = entries_collection.delete_one(filter)
            print(f"CLASSDATABASE - Entrada deletada")

            return True, None

        except Exception as error:
            print(f"CLASSDATABASE - Erro ao deletar entrada: {error}")

            return False, error
        
    def update_entry(self, entryId, newEntryData):
        entries_collection = self.database["Entries"]
        fs = gridfs.GridFS(self.database)

        query = {
            "date": newEntryData.date
        }

        if newEntryData.description:
            query["description"] = newEntryData.description

        if newEntryData.image:
            try:
                with open(newEntryData.image, "rb") as imageFile:
                    fileId = fs.put(imageFile, filename = newEntryData.image.split("/")[-1])
                    query["image_id"] = fileId
                    print(f"CLASSDATABASE - imagem atualizada no gridFS com ID: {fileId}")

            except Exception as error:
                print("CLASSDATABASE - Erro ao atualizar imagem:", error)

        try:
            action = entries_collection.update_one(
                {"_id": ObjectId(entryId)},
                {"$set": query}
            )

            print("CLASSDATABASE - entrada atualizada no banco de entradas")
            return True, None
        
        except OperationFailure as error:
            print("CLASSDATABASE - falha ao atualizar entrada") 
            return False, error
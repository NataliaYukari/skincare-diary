from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure, DuplicateKeyError, OperationFailure



class Authentication:
    """Validates the user's login"""

    
    def __init__(self):
        url = "mongodb+srv://nataliakawashisa:bananinha@ifpr.tffr4.mongodb.net/?retryWrites=true&w=majority&appName=IFPR"
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.database = self.client["skincare_diary"]

    def validate_login(self, login, password):
        users_collection = self.database["Users"]

        try:
            user = users_collection.find_one({"name": login})

            if user:
                if user["password"] == password:
                    print("CLASSAUTHENTICATION: login válido")
                    return True, ""
                else:
                    print("CLASSAUThENTICATION: senha inválida")
                    return False, "senha inválida"
            else:
                print("CLASSAUTHENTICATION: login inválido")
                return False, "login inválido"
            
        except ConnectionFailure as error:
            print("CLASSAUTHENTICATION: erro de conexão ao BD - ", error)
            return False, "erro de conexão"

        except Exception as error:
            print("CLASSAUTHENTICATION: erro - ", error)
            return False, "erro de conexão"
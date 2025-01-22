from model_database import Database
from routine import Routine
from datetime import datetime, timedelta
import base64
from PIL import Image
from io import BytesIO


class Model:
    def __init__(self, database):
        self.database = database
        self.activeUser = None

    def create_user(self, userData):
        action, message = self.database.create_user(userData)

        return action, message
    
    def validate_login(self, login, password):
        isValid, message = self.database.validate_login(login, password)

        if isValid:
            self.activeUser = login

        return isValid, message
        
    def generate_routine(self, skinWorries):
        result = self.database.get_user_data(self.activeUser)   

        cleanser = self.generate_cleanser(skinWorries, result)
        treatmentAM = self.generate_AM_treatment(skinWorries, result)
        moisturizerAM = self.generate_AM_moisturizer(skinWorries, result)
        sunscreen = self.generate_sun_protection(skinWorries, result)
        treatmentPM = self.generate_PM_treatment(skinWorries, result)
        moisturizerPM = self.generate_PM_moisturizer(skinWorries, result)

        routine = Routine(cleanser, treatmentAM, moisturizerAM, sunscreen, 
                          treatmentPM, moisturizerPM)
        
        action = self.database.save_routine(routine)
        
        if action:
            return routine
        
    def get_routine(self):
        result = self.database.read_routine(self.activeUser)
        
        if result:
            routine = Routine(
                cleanser = result["cleanser"],
                treatmentAM = result["treatmentAM"],
                moisturizerAM = result["moisturizerAM"],
                sunscreen = result["sunscreen"],
                treatmentPM = result["treatmentPM"],
                moisturizerPM = result["moisturizerPM"]
            )
            return routine

    def generate_cleanser(self, skinWorries, result):
        ageOver45 = self.get_age(result) >= 45
        isSensitive = result["sensibility"]
        skinTypeIsNormalOrDry = result["skinType"] in ["Seca", "Normal"]
        hasIrritation = skinWorries.irritation

        if ageOver45 or isSensitive or skinTypeIsNormalOrDry or hasIrritation:
            cleanser = "Sabonete facial com ácido hialurônico e glicerina"
        else:
            cleanser = "Sabonete facial com ácido salicílico e niacinamida" 
        
        return cleanser
        
    def generate_AM_treatment(self, skinWorries, result):
        isSensitive = result["sensibility"]
        hasIrritation = skinWorries.irritation
        isDehydrated = skinWorries.dehydration
        skinTypeIsDry = result["skinType"] in ["Seca"]

        if isSensitive or hasIrritation or isDehydrated or skinTypeIsDry:
            treatment = "Sérum de ácido hialurônico + niacinamida"
        else:
            treatment = "Sérum de vitamina C + ácido ferúlico"

        return treatment
        
    def generate_AM_moisturizer(self, skinWorries, result):
        isSensitive = result["sensibility"]
        hasIrritation = skinWorries.irritation
        skinTypeisDry = result["skinType"] in ["Seca"]
        isDehydrated = skinWorries.dehydration

        if isSensitive or hasIrritation:
            moisturizer = ("Loção de ácido hialurônico com extrato de "
                        + "centella asiatica e aveia")
        elif skinTypeisDry or isDehydrated:
            moisturizer = "Creme com ácido hialurônico, vitamina B5 e ceramidas"
        else:
            moisturizer = "Sérum snail mucin e aloe vera"

        return moisturizer
    
    def generate_sun_protection(self, skinWorries, result):
        isSensitive = result["sensibility"]
        ageOver45 = self.get_age(result) >= 45
        hasIrritation = skinWorries.irritation

        if isSensitive or ageOver45 or hasIrritation:
            sunscreen = "Gel hidratante FPS 50 PA++++"
        else:
            sunscreen = "Fluído matte FPS 50 PA++++"
        
        return sunscreen
    
    def generate_PM_treatment(self, skinWorries, result):
        isSensitive = result["sensibility"]
        hasAcne = skinWorries.acne
        ageOver30 = self.get_age(result) >= 30

        if isSensitive:
            treatment = "Sérum de vitamina E + squalano"
        elif hasAcne:
            treatment = "Sérum de ácido glicólico"
        elif ageOver30:
            treatment = "Sérum de retinol"
        else:
            treatment = "Sérum de alfa-arbutin e gluconolactona"

        return treatment

    def generate_PM_moisturizer(self, skinWorries, result):
        isSensitive = result["sensibility"]
        skinTypeIsDry = result["skinType"] in ["Seca"]
        isDehydrated = skinWorries.dehydration
        skinTypeIsOily = result["skinType"] in ["Oleosa"]
        hasAcne = skinWorries.acne
        hasPores = skinWorries.pores
        hasExcessOil = skinWorries.oil

        if isSensitive or skinTypeIsDry or isDehydrated:
            moisturizer = "Creme de pantenol com ceramidas"
        elif skinTypeIsOily or hasAcne or hasPores or hasExcessOil:
            moisturizer = "Sérum com mix de ácidos hialurônicos"
        else:
            moisturizer = "Loção de ácido hialurônico e ceramidas"

        return moisturizer

    def get_age(self, result):
        """Calcula a idade do usuário"""
        birthday = datetime.strptime(result["birthday"], "%d/%m/%Y").date()
        today = datetime.now().date()
        age = (
               today.year - birthday.year 
               - ((today.month, today.day) < (birthday.month, birthday.day))
              )

        return age

    def create_entry(self, entryData):
        action, message = self.database.create_entry(entryData)

        return action, message
            
    def get_diary(self):
        return self.database.get_diary()       

    def get_entry(self, entryId):
        entryData, imageBase64 = self.database.get_entry(entryId)
        imagePath = f"data:image/jpeg;base64,{imageBase64}"

        return entryData, imagePath


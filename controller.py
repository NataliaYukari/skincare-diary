from view import *
from model import *

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def go_to_register_screen(self):
        self.view.register_screen()

    def validate_user_data(self, userData):
        if not userData.username or not userData.password or not userData.email or not userData.birthday or not userData.skinType:
            message = "cadastrar"
            errorDescription = "Preencha todos os campos"
            self.view.fail_alert_modal(message, errorDescription)
            return
        
        self.create_user(userData)

    def create_user(self, userData):
        try:
            action, message = self.model.create_user(userData)
            
            if action:
                self.view.success_alert_modal(message["title"], message["description"])
            else:
                self.view.fail_alert_modal(message["title"], message["description"])
            
        except Exception as e:
            message = "cadastrar"
            self.view.fail_alert_modal(message, e)

    def validate_login(self, login, password):
        isValid, message = self.model.validate_login(login, password)

        if not isValid:
            self.view.login_fail_text(message)
        else:
            self.view.main_screen()
        
    def go_to_routine_form(self):
        self.view.new_routine_screen()

    def go_to_recommended_routine_screen(self):
        routine = self.model.get_routine()

        if routine:
            print("CLASSCONTROLLER - rotina encontrada")
            self.view.recommended_routine_screen(routine)
        else:
            print("CLASSCONTROLLER - rotina não encontrada")
            self.view.fail_alert_modal("consultar rotina", 
                                       "Rotina não encontrada. Monte sua rotina.")

    def generate_routine(self, skinWorries):
        routine = self.model.generate_routine(skinWorries) 
        self.view.recommended_routine_screen(routine)
       
    def go_to_add_entry_screen(self):
        self.view.add_entry_screen()

    def create_entry(self, entryData):
        try:
            action, message = self.model.create_entry(entryData)

            if action:
                self.view.success_alert_modal(message["title"], message["description"])
            else:
                self.view.fail_alert_modal(message["title"], message["description"])

        except Exception as e:
            message = "criar página do diário"
            self.view.fail_alert_modal(message, e)

    def go_to_diary_screen(self):
        result = self.model.get_diary()
        self.view.diary_screen(result)

    def go_to_entry_screen(self, entryId):
        entryData, imagePath = self.model.get_entry(entryId)

        if entryData:
            self.view.entry_screen(entryData, imagePath)

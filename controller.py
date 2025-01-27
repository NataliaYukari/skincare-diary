from view import *
from model import *


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.currentEntryIndex = 0

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
        result, message = self.model.create_user(userData)
            
        if result:
            self.view.success_alert_modal(message["title"], self.view.return_to_login)
        else:
            self.view.fail_alert_modal(message["title"], message["description"])

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
        result, message = self.model.create_entry(entryData)

        if result:
            self.view.success_alert_modal(message["title"], self.view.return_to_main)
        else:
            self.view.fail_alert_modal(message["title"], message["description"])

    def go_to_diary_screen(self):
        result = self.model.get_diary()

        if result:
            self.view.diary_screen(result)
        else:
            self.view.main_screen()
            self.view.fail_alert_modal("acessar diário", 
                                       "O diário está vazio. Crie novas entradas")
            
    def go_to_next_entry(self):
        entries = self.model.get_diary()

        self.currentEntryIndex = (self.currentEntryIndex + 1) % len(entries)

        entry = entries[self.currentEntryIndex]
        entryId = entry["_id"]

        self.view.go_to_entry_screen(entryId, self.currentEntryIndex)

    def go_to_previous_entry(self):
        entries = self.model.get_diary()

        self.currentEntryIndex = (self.currentEntryIndex - 1) % len(entries)

        if self.currentEntryIndex < 0:
            self.currentEntryIndex = len(entries) - 1

        entry = entries[self.currentEntryIndex]
        entryId = entry["_id"]

        self.view.go_to_entry_screen(entryId, self.currentEntryIndex)

    def go_to_entry_screen(self, entryId, index):
        entryData, imagePath = self.model.get_entry(entryId)

        if entryData:
            self.currentEntryindex = index
            self.view.entry_screen(entryData, imagePath)

    def delete_entry(self, entry): 
        result, message = self.model.delete_entry(entry)

        if result == True:
            self.view.success_alert_modal(message["title"], self.view.go_to_diary_screen)
        else:
            self.view.fail_alert_modal(message["title"], message["description"])

    def go_to_update_entry_screen(self, entryId):
        entryData, imagePath = self.model.get_entry(entryId)

        if entryData:
            self.view.update_entry_screen(entryData, imagePath)

    def update_entry(self, entryId, newEntryData):
        result, message = self.model.update_entry(entryId, newEntryData)

        if result == True:
            self.view.success_alert_modal(message["title"], self.view.go_to_diary_screen)
        else:
            self.view.fail_alert_modal(message["title"], message["description"])
from view import *
from model import *

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def go_to_register_screen(self):
        self.view.register_screen()

    def validate_user_data(self, user_data):
        if not user_data.username or not user_data.password or not user_data.email or not user_data.birthday or not user_data.skinType:
            message = "cadastrar"
            errorDescription = "Preencha todos os campos"
            self.view.fail_alert_modal(message, errorDescription)
            return
        
        self.create_user(user_data)

    def create_user(self, user_data):
        try:
            action, message = self.model.create_user(user_data)
            
            if action:
                self.view.success_alert_modal(message["title"], message["description"])
            else:
                self.view.fail_alert_modal(message["title"], message["description"])
            
        except Exception as e:
            message = "cadastrar"
            errorDescription = e
            self.view.fail_alert_modal(message, errorDescription)

    def validate_login(self, login, password):
        isValid, message = self.model.validate_login(login, password)

        if not isValid:
            self.view.login_fail_text(message)
        else:
            self.view.main_screen()
        
    def go_to_routine_form(self):
        self.view.new_routine_screen()

    def go_to_recommended_routine_screen(self):
        action = self.model.get_routine()

        if action:
            self.view.recommended_routine_screen()

    def generate_routine(self, skinWorries):
        routine = self.model.generate_routine(skinWorries) 
        self.view.recommended_routine_screen(routine)
       
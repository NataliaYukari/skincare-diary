import flet as ft
from models.entry import Entry
from views.login_screen import LoginScreen
from views.register_screen import RegisterScreen
from views.main_screen import MainScreen
from views.new_routine_screen import NewRoutineScreen
from views.recommended_routine_screen import RecommendedRoutineScreen
from views.add_entry_screen import AddEntryScreen
from views.diary_screen import DiaryScreen
from views.update_entry_screen import UpdateEntryScreen
from views.entry_screen import EntryScreen



class View:
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = None
        self.imagePath = None

        self.filePicker = ft.FilePicker()
        self.page.overlay.append(self.filePicker)

        self.BEIGE = "#F2F1E9"
        self.DEEPBEIGE = "#F0D2AB"
        self.ROSEQUARTZ = "#D9B7B4"
        self.PALESALMON = "#D9B4A7"
        self.WHITE = "#FFFFFF"
        self.DARKGRAY = "#736B6A"
        self.LIGHTGRAY = "#878787"

        self.page.fonts = {"AlbertSans": "assets/fonts/AlbertSans-Light.ttf"}
        self.page.bgcolor = self.BEIGE        

        self.routes = {
            "/": LoginScreen(self),
            "/registerScreen": RegisterScreen(self),
            "/mainScreen": MainScreen(self),
            "/newRoutineScreen": NewRoutineScreen(self),
            "/recommendedRoutineScreen": RecommendedRoutineScreen(self),
            "/addEntryScreen": AddEntryScreen(self, self.filePicker),
            "/diaryScreen": DiaryScreen(self),
            "/entryScreen": EntryScreen(self),
            "/updateEntryScreen": UpdateEntryScreen(self, self.filePicker)
        }

    def navigate_to(self, route):
        self.page.update()
        self.page.clean()
        self.page.add(self.routes[route])
        self.page.update()

    def set_controller(self, controller):
        self.controller = controller
    
    def go_to_register_screen(self, e):
        self.routes["/registerScreen"].reset_fields()
        self.controller.go_to_register_screen()

    def go_to_routine_form(self, e):
        self.controller.go_to_routine_form()

    def go_to_recommended_routine_screen(self, e):
        self.controller.go_to_recommended_routine_screen()

    def go_to_add_entry_screen(self, e):
        self.routes["/addEntryScreen"].reset_fields()
        self.controller.go_to_add_entry_screen()

    def go_to_diary_screen(self, e):
        self.controller.go_to_diary_screen()

    def go_to_entry_screen(self, entryId, index):
        self.controller.go_to_entry_screen(entryId, index)

    def delete_entry(self, entry):
        self.controller.delete_entry(entry)

    def go_to_update_entry_screen(self, entryId):
        self.controller.go_to_update_entry_screen(entryId)

    def return_button(self, action):
        returnButton = ft.FilledButton(
            text= "Voltar",
            on_click= action,
            style= ft.ButtonStyle(
                bgcolor= {"": ft.colors.TRANSPARENT, "hovered": self.BEIGE}, 
                color= ft.colors.BLACK,
                side= ft.BorderSide(
                color= ft.colors.BLACK, width= 0.5),
                padding= ft.Padding(60, 10, 60, 10),
                text_style= ft.TextStyle(size= 22)
            )
        )                      
        return returnButton
    
    def return_to_login(self, e):
        self.navigate_to("/")

    def return_to_main(self, e):
        self.navigate_to("/mainScreen")

    def return_to_diary(self, e):
        self.navigate_to("/diaryScreen")

    def success_alert_modal(self, message, whereToReturn):
        ok_button = ft.FilledButton(
            text= "Ok",
            on_click= self.close_success_modal,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                color= self.WHITE,
                padding= ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size=22)
            )
        )

        self.success_modal = ft.AlertDialog(
            modal= True, 
            bgcolor= self.ROSEQUARTZ,
            title= ft.Text(message + " com sucesso!"),
            content= ft.Text(""),
            actions= [ok_button],
            actions_alignment= ft.MainAxisAlignment.CENTER,
            on_dismiss= whereToReturn
        )

        self.page.open(self.success_modal)
        self.page.update()

    def close_success_modal(self, e):
        self.page.close(self.success_modal)

    def fail_alert_modal(self, message, errorDescription):
        ok_button = ft.FilledButton(
            text= "Ok",
            on_click= self.close_fail_modal,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                color= self.WHITE,
                padding= ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size=22)
            )
        )

        self.fail_modal = ft.AlertDialog(
            modal= True,
            bgcolor= self.ROSEQUARTZ,
            title= ft.Text("Erro ao " + message),
            content= ft.Column(controls= [ft.Text(errorDescription)], tight= True),
            actions= [ok_button],
            actions_alignment= ft.MainAxisAlignment.CENTER,
        )
        self.page.open(self.fail_modal)
        self.page.update()

    def close_fail_modal(self, e):
        self.page.close(self.fail_modal)

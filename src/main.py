import flet as ft
from controller import Controller
from models.model import Model
from models.model_database import Database 
from views.view import View


def main(page: ft.Page):
    database = Database()
    model = Model(database)
    view = View(page)
    controller = Controller(model, view) 

    view.set_controller(controller)
    view.navigate_to("/")

ft.app(target=main)


from controller import Controller
from model import Model
from model_database import Database 
from view import View


if __name__ == "__main__":
    database = Database()
    model = Model(database)
    view = View()
    controller = Controller(model, view) 

    view.set_controller(controller)
    view.init()
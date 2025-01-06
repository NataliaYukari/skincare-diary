from view import View
from model import Model, Database
from controller import Controller

if __name__ == "__main__":
    database = Database()
    model = Model(database)
    view = View()
    controller = Controller(model, view) 

    view.set_controller(controller)
    view.init()
   
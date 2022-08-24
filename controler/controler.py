from model.model import Model
from view.gui import Gui



class Controler():
    def __init__(self):
        '''
        When initiating call the GUI function to render the first screen
        '''
        self.gui = Gui()
        self.model = Model()

    def choose_operation(operation):
        '''
        Executes one operation, based on the parameter passed by the 
        view
        '''
        if operation == 'add':
            pass
        if operation == 'delete':
            pass
        if operation == 'update':
            pass
        if operation == 'filter':
            pass
        else:
            pass

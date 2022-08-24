from controler.controler import Controler
from tkinter import *

class Gui():
    def __init__(self):
        self.render_first_screen()



    def render_first_screen(self):
        '''
        Renders the first screen with the buttons 
        '''

        root = Tk()

        self.render_main_label(root,"Insert Client Info")

        root.mainloop()


    def render_main_label(self,root,text):
        '''
        Renders main title of the page
        '''
        title_label = Label(root, text=text,
            font=('Arial', 25))
        title_label.grid(row=0, column=1)


    def render_button(self, root, text, command, x, y):
        submit_button = Button()
        button = Button(root, text=text, command=command, bg="#B0E0E6")
        button.grid(row=y, column=x)
        
    
    def return_choice(self):
        pass



    def render_clients_table(client_list):
        '''
        Gets the df with the clients and prints them to an 
        interactive menu
        '''
        pass
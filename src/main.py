from kivy.app import App
from kivy.uix.widget import Widget
from app.TasksApp import TasksApp
from app.db import DB

class App(App):
    def build(self):
        app = TasksApp()
        app.init()
        return app

if __name__ == '__main__':
    App().run()
    

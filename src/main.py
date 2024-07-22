from kivy.app import App
from kivy.uix.widget import Widget
from app.TasksApp import TasksApp

class App(App):
    def build(self):
        return TasksApp()

if __name__ == '__main__':
    App().run()
    

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.db import DB
from app.Task import Task


Builder.load_file('app/TasksApp.kv')
class TasksApp(Widget):
    btn_add = ObjectProperty(None)
    input_add = ObjectProperty(None)
    layout_stack = ObjectProperty(None)
    db = ObjectProperty(None)

    def init(self):
        self.db = DB.instance()
        tasks = self.db.get_tasks()
        for task in tasks:
            self.add_task(task)


    def btn_done_click(self, instance):
        self.db.rm_task(instance.task_id)
        self.layout_stack.remove_widget(instance.parent)

    def btn_add_click(self):
        id_task = self.db.new_task(Task(text=self.input_add.text))
        self.add_task(Task(id_task, self.input_add.text))
        self.input_add.text = ""

    def add_task(self, task):
        container = BoxLayout(orientation='horizontal', width=self.width, size_hint=(1, .07))
        label = Label(text=task.text, size_hint=(.8, 1), color=(245,17,150, 1))
        btn = Button(text='done', size_hint=(.2, 1), on_press=self.btn_done_click)
        btn.task_id = task.id
        container.add_widget(label)
        container.add_widget(btn)
        self.layout_stack.add_widget(container)


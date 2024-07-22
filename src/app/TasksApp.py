from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_file('app/TasksApp.kv')
class TasksApp(Widget):
    count = 0;
    btn_add = ObjectProperty(None)
    input_add = ObjectProperty(None)
    layout_stack = ObjectProperty(None)

    def btn_add_click(self):
        label = Label(text=self.input_add.text, width=self.width, height=10, size_hint=(None, None), color=(245,17,150, 1))
        self.input_add.text = ""

        self.layout_stack.add_widget(label)

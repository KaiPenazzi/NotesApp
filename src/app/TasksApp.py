from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('app/TasksApp.kv')
class TasksApp(Widget):
    count = 0;
    btn_add = ObjectProperty(None)
    input_add = ObjectProperty(None)
    layout_stack = ObjectProperty(None)

    def btn_done_click(self, instance):
        self.layout_stack.remove_widget(instance.parent)

    def btn_add_click(self):
        container = BoxLayout(orientation='horizontal', width=self.width, size_hint=(1, .07))
        label = Label(text=self.input_add.text, size_hint=(.8, 1), color=(245,17,150, 1))
        btn = Button(text='done', size_hint=(.2, 1), on_press=self.btn_done_click)
        container.add_widget(label)
        container.add_widget(btn)

        self.layout_stack.add_widget(container)
        self.input_add.text = ""


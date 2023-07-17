from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.config import Config


Config.set('graphics', 'width', '400')

class P(Popup):
     def cancel(self):
         self.dismiss(self)
         

class TaskComplete(BoxLayout):
    def __init__(self, text):
        super().__init__()
        self.ids.label_c.text = text

    def remove(self):
        self.parent.remove_widget(self)
    
    def on_checkbox_deactive(self, value, label):
        if not value:
            self.parent.parent.parent.parent.parent.ids.principal.add_widget(TodoList(label))
            self.parent.parent.parent.parent.parent.ids.complete.remove_widget(self)

class TodoList(BoxLayout):
    def __init__(self, text):
        super().__init__()
        self.ids.label1.text = text

    def remove(self):
        self.parent.remove_widget(self)
    
    def on_checkbox_active(self, value, label):

        if value:
           self.parent.parent.parent.parent.parent.ids.complete.add_widget(TaskComplete(label))
           self.parent.parent.parent.parent.parent.ids.principal.remove_widget(self)
        
class MainTodo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def add_todo(self, text):
        if text == '':
           P().open()
        else:
            todo = TodoList(text)
            self.ids.principal.add_widget(todo)
            self.ids.todo.text = ''
        

class TodoApp(App):
    def build(self):
        self.todo = MainTodo()
        
        return self.todo

    def get_todo(self):
        return self.todo

TodoApp().run()
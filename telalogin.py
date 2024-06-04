from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder

def resize_window(*args):
    Window.size = (357, 550)

class TelaLoginScreen(Screen):
    def toggle_password_visibility(self):
        peso_input = self.ids.peso_input
        toggle_button = self.ids.toggle_button
        peso_input.password = not peso_input.password
        toggle_button.source = 'C:/Users/Administrador/Downloads/aberto.png' if peso_input.password else 'C:/Users/Administrador/Downloads/fechado.png'

    def forgot_password(self):
        print("vai pra outra tela")

class WhiteSquare(Widget):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class ClickableLabel(ButtonBehavior, Label):
    pass

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)
        return Builder.load_file('planner2.kv')

if __name__ == '__main__':
    Window.size = (350, 550)
    Window.bind(on_resize=resize_window)
    PlannerApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle
from kivy.lang import Builder

def resize_window(*args):
    Window.size = (357, 550)

class WhiteSquare(Widget):
    def __init__(self, **kwargs):
        super(WhiteSquare, self).__init__(**kwargs)
        with self.canvas:
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class SenhaScreen(Screen):
    pass

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)
        Window.bind(on_resize=resize_window)
        return Builder.load_file('senha.kv')

if __name__ == '__main__':
    Window.size = (400, 400)
    PlannerApp().run()

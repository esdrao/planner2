from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, Ellipse
from kivy.uix.behaviors import ButtonBehavior

def resize_window(*args):
    Window.size = (357, 550)

class Background(Image):
    pass

class HalfCircleWidget(ButtonBehavior, Image):
    def __init__(self, color, **kwargs):
        super(HalfCircleWidget, self).__init__(**kwargs)
        self.source = ''
        with self.canvas:
            Color(*color)
            self.ellipse = Ellipse(pos=self.pos, size=self.size, angle_start=90, angle_end=270)
        self.bind(pos=self.update_ellipse, size=self.update_ellipse)

    def update_ellipse(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

class ClickableSquare(ButtonBehavior, Image):
    def __init__(self, image_source, **kwargs):
        super(ClickableSquare, self).__init__(**kwargs)
        self.source = image_source
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = (None, None)
        self.size = (100, 100)

class MainApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        layout = FloatLayout()

        background = Background(source="C:/Users/Administrador/Downloads/fundo3.jpeg")
        layout.add_widget(background)

        top_half_circle = HalfCircleWidget(color=(0.87, 0.63, 0.87), size_hint=(None, None), size=(500, 400))
        top_half_circle.pos_hint = {'center_x': 0.5, 'y': 0.63}
        layout.add_widget(top_half_circle)

        # Adicione aqui a criação dos outros widgets

        return layout

if __name__ == '__main__':
    Window.size = (400, 540)
    Window.bind(on_resize=resize_window)
    MainApp().run()

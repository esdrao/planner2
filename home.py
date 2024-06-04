from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

def resize_window(*args):
    Window.size = (357, 550)

class HalfCircleWidget(Widget):
    def __init__(self, color, **kwargs):
        super(HalfCircleWidget, self).__init__(**kwargs)
        self.color = color
        with self.canvas:
            Color(*color)
            self.ellipse = Ellipse(pos=self.center, size=self.size, angle_start=90, angle_end=270)
        self.bind(pos=self.update_ellipse, size=self.update_ellipse)

    def update_ellipse(self, *args):
        self.ellipse.pos = self.center_x - self.ellipse.size[0] / 2, self.center_y - self.ellipse.size[1] / 2

class ClickableSquare(ButtonBehavior, Image):
    def __init__(self, image_source, target_screen, **kwargs):
        super(ClickableSquare, self).__init__(**kwargs)
        self.source = image_source
        self.target_screen = target_screen
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = (None, None)
        self.size = (100, 100)

    def on_press(self):
        self.parent.manager.current = self.target_screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        background = Image(source="C:/Users/Administrador/Downloads/fundo3.jpeg", size_hint=(None, None), size=(700, 1000),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        top_half_circle = HalfCircleWidget(color=(0.87, 0.63, 0.87), size_hint=(None, None), size=(500, 400))
        top_half_circle.pos_hint = {'center_x': 0.5, 'y': 0.63}
        layout.add_widget(top_half_circle)

        middle_half_circle = HalfCircleWidget(color=(1, 0.8, 0.6), size_hint=(None, None), size=(500, 400))
        middle_half_circle.pos_hint = {'center_x': 0.5, 'y': 0.7}
        layout.add_widget(middle_half_circle)

        bottom_half_circle = HalfCircleWidget(color=(1, 1, 1), size_hint=(None, None), size=(500, 400))
        bottom_half_circle.pos_hint = {'center_x': 0.5, 'y': 0.76}
        layout.add_widget(bottom_half_circle)

        title_image = Image(source="C:/Users/Administrador/Downloads/texto.jpeg", size_hint=(None, None), size=(250, 150),
                            pos_hint={'center_x': 0.5, 'y': 0.78})
        layout.add_widget(title_image)

        # Add three clickable squares with images
        square1 = ClickableSquare(image_source="C:/Users/Administrador/Downloads/agenda (1).jpeg", target_screen="agenda_screen")
        square1.size = (140, 130)
        square1.pos_hint = {'center_x': 0.3, 'y': 0.36}
        layout.add_widget(square1)

        square2 = ClickableSquare(image_source="C:/Users/Administrador/Downloads/cronograma2.jpeg", target_screen="cronograma_screen")
        square2.size = (140, 130)
        square2.pos_hint = {'center_x': 0.7, 'y': 0.36}
        layout.add_widget(square2)

        square3 = ClickableSquare(image_source="C:/Users/Administrador/Downloads/metas2.jpeg", target_screen="metas_screen")
        square3.size = (140, 130)
        square3.pos_hint = {'center_x': 0.5, 'y': 0.1}
        layout.add_widget(square3)

        self.add_widget(layout)

class AgendaScreen(Screen):
    def __init__(self, **kwargs):
        super(AgendaScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        label = Image(source="C:/Users/Administrador/Downloads/agenda (1).jpeg", size_hint=(None, None), size=(250, 250),
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(label)
        self.add_widget(layout)

class CronogramaScreen(Screen):
    def __init__(self, **kwargs):
        super(CronogramaScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        label = Image(source="C:/Users/Administrador/Downloads/cronograma2.jpeg", size_hint=(None, None), size=(250, 250),
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(label)
        self.add_widget(layout)

class MetasScreen(Screen):
    def __init__(self, **kwargs):
        super(MetasScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        label = Image(source="C:/Users/Administrador/Downloads/metas2.jpeg", size_hint=(None, None), size=(250, 250),
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(label)
        self.add_widget(layout)

class PlannerApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(AgendaScreen(name='agenda_screen'))
        sm.add_widget(CronogramaScreen(name='cronograma_screen'))
        sm.add_widget(MetasScreen(name='metas_screen'))

        return sm

if __name__ == '__main__':
    Window.size = (350, 550)
    Window.bind(on_resize=resize_window)
    PlannerApp().run()

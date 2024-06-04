from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from telalogin import TelaLoginScreen
from home import MainScreen, AgendaScreen, CronogramaScreen, MetasScreen

class ScreenManagement(ScreenManager):
    pass

class PlannerApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        Window.size = (350, 550)
        
        sm = ScreenManagement()
        sm.add_widget(TelaLoginScreen(name='login_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(AgendaScreen(name='agenda_screen'))
        sm.add_widget(CronogramaScreen(name='cronograma_screen'))
        sm.add_widget(MetasScreen(name='metas_screen'))
        
        return sm

if __name__ == '__main__':
    PlannerApp().run()

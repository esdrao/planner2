import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from calendar import monthrange
from kivy.lang import Builder

Window.size = (350, 550)

class WhiteSquareLabel(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class PlannerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_info()
        self.build_ui()

    def build_ui(self):
        # Create the main layout
        self.layout = FloatLayout()

        # Add background image
        background = Image(source="C:/Users/Administrador/Downloads/fundo3.jpeg", allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)

        # Create a white square behind the month label
        self.white_square_label = WhiteSquareLabel(size_hint=(None, None), size=(340, 60), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.layout.add_widget(self.white_square_label)

        # Create a label to display the selected month
        self.month_label = Label(
            text="Selecione um mês",
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            color=(0, 0, 0, 1),
            font_size='20sp'
        )
        self.layout.add_widget(self.month_label)

        # Create a button to open the month dropdown
        self.month_button = Button(
            text='Escolher Mês',
            size_hint=(None, None),
            size=(150, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            background_color=(0, 0, 0, 1)  # Black color for background
        )
        self.month_button.bind(on_release=self.open_month_dropdown)
        self.layout.add_widget(self.month_button)

        # Create a dropdown menu for the months
        self.month_dropdown = DropDown()
        self.months = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        for month in self.months:
            month_btn = Button(
                text=month,
                size_hint_y=None,
                height=40,
                background_color=(0, 0, 0, 1),  # Black color for background
                on_release=self.on_month_button_press,
                color=(1, 1, 1, 1)  # White color for text
            )
            self.month_dropdown.add_widget(month_btn)

        # Create a grid layout for days, initially hidden
        self.days_layout = GridLayout(cols=7, spacing=5, size_hint=(None, None), size=(350, 300),
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.days_layout)
        self.days_layout.opacity = 0  # Initially hide the days layout

        # Create a TextInput for entering information
        self.info_input = TextInput(
            hint_text="Digite sua informação",
            size_hint=(None, None),
            size=(280, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            background_color=(1, 1, 1, 1),  # White color for background
            foreground_color=(0, 0, 0, 1)  # Black color for text
        )
        self.layout.add_widget(self.info_input)
        self.info_input.opacity = 0  # Initially hide the TextInput

        # Create a Save button
        self.save_button = Button(
            text="Salvar",
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_color=(0, 0, 0, 1),  # Black color for background
            color=(1, 1, 1, 1)  # White color for text
        )
        self.save_button.bind(on_release=self.save_info)
        self.layout.add_widget(self.save_button)
        self.save_button.opacity = 0  # Initially hide the Save button

        self.add_widget(self.layout)

    def open_month_dropdown(self, instance):
        self.month_dropdown.open(instance)

    def on_month_button_press(self, instance):
        # Close the dropdown menu
        self.month_dropdown.dismiss()

        # Update the label text to the selected month
        month = instance.text
        self.month_label.text = f"Mês selecionado: {month}"

        # Get the number of days in the selected month
        month_index = self.months.index(month) + 1
        year = 2024  # You can change this to the current year or any other year
        num_days = monthrange(year, month_index)[1]

        # Clear the previous days
        self.days_layout.clear_widgets()

        # Add buttons for each day of the month
        for day in range(1, num_days + 1):
            day_button = Button(
                text=str(day),
                size_hint=(None, None),
                size=(40, 40),
                on_release=self.on_day_button_press,
                background_color=(0, 0, 0, 1),  # Black color for background
                color=(1, 1, 1, 1)  # White color for text
            )
            self.days_layout.add_widget(day_button)

        # Show the days layout
        self.days_layout.opacity = 1

    def on_day_button_press(self, instance):
        # Update the label text to the selected day
        selected_day = instance.text
        selected_month = self.month_label.text.split(": ")[1]
        self.month_label.text = f"Selecionado: {selected_day} , {selected_month}"

        # Show the TextInput and Save button
        self.info_input.opacity = 1
        self.save_button.opacity = 1

        # Load previously saved info if it exists
        self.info_input.text = self.saved_info.get(selected_month, {}).get(selected_day, "")

    def save_info(self, instance):
        selected_month = self.month_label.text.split(": ")[1]
        selected_day = self.month_label.text.split(" ")[1]
        info = self.info_input.text

        # Save the information in the dictionary
        if selected_month not in self.saved_info:
            self.saved_info[selected_month] = {}
        self.saved_info[selected_month][selected_day] = info

        # Save the dictionary to a JSON file
        with open("saved_info.json", "w") as f:
            json.dump(self.saved_info, f)

        print(f"Informação salva para {selected_day} de {selected_month}: {info}")

    def load_info(self):
        try:
            with open("saved_info.json", "r") as f:
                self.saved_info = json.load(f)
        except FileNotFoundError:
            self.saved_info = {}

class PlannerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PlannerScreen(name='planner'))
        return sm

if __name__ == '__main__':
    PlannerApp().run()

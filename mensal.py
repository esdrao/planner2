from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

class PlannerScreen(Screen):
    def __init__(self, **kwargs):
        super(PlannerScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # Adicionando a imagem de fundo
        self.background = Image(source="C:/Users/Administrador/Downloads/fundo3.jpeg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.layout.add_widget(self.background)
        
        # Adicionando a imagem de logotipo no topo
        self.logo = Image(source="C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 182808.png",
                          size_hint=(None, None), size=(400, 100), pos_hint={'center_x': 0.5, 'top': 1})
        self.layout.add_widget(self.logo)
        
        # Lista para armazenar referências das caixas de texto
        self.text_inputs = []
        
        # Adicionando as caixas de texto
        self.add_text_inputs()

        # Adicionando o botão "Salvar"
        self.save_button = Button(text="Salvar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'top': 0.1})
        self.save_button.bind(on_press=self.save_text)
        self.layout.add_widget(self.save_button)

    def add_text_inputs(self):
        x_position = 0.5  # Posição horizontal para o centro
        y_top = 0.8  # Posição inicial vertical (ajustada para dar espaço ao logotipo)

        for _ in range(3):  # Criando 3 caixas de texto
            # Adicionando a caixa de texto
            text_input = TextInput(hint_text=" ", size_hint=(None, None), size=(300, 100), pos_hint={'center_x': x_position, 'top': y_top})
            self.layout.add_widget(text_input)
            self.text_inputs.append(text_input)  # Salvando a referência da caixa de texto

            y_top -= 0.25  # Atualizando a posição vertical para a próxima caixa de texto

    def save_text(self, instance):
        # Função para salvar o texto das caixas de texto
        text_data = [text_input.text for text_input in self.text_inputs]
        with open("saved_texts.txt", "w") as file:
            for text in text_data:
                file.write(text + "\n")
        print("Textos salvos:", text_data)

class PlannerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PlannerScreen(name='planner'))
        return sm

if __name__ == '__main__':
    Window.size = (400, 540)
    PlannerApp().run()

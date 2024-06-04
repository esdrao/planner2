from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class PlannerLayout(Screen):
    def __init__(self, **kwargs):
        super(PlannerLayout, self).__init__(**kwargs)
        
        # Adicionando a imagem de fundo
        self.background = Image(source="C:/Users/Administrador/Downloads/fundo3.jpeg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)
        
        # Adicionando a imagem de logotipo no topo
        self.logo = Image(source="C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 092025.png", size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5, 'top': 1})
        self.add_widget(self.logo)
        
        # Adicionando os pares de imagem e caixa de texto
        self.add_image_text_pairs()

    def add_image_text_pairs(self):
        # Lista de imagens para adicionar acima das caixas de texto
        images = [
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 103017.png",
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 165613.png",
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 165632.png",
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 165645.png",
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 175906.png",
            "C:/Users/Administrador/OneDrive/Imagens/Capturas de tela/Captura de tela 2024-05-28 175917.png"
        ]

        x_positions = [0.3, 0.7]  # Posições horizontais para duas colunas
        y_top = 0.85  # Posição inicial vertical (ajustada para dar espaço ao logotipo)
        index = 0  # Índice para rastrear qual imagem usar

        for row in range(3):  # 3 pares por coluna, totalizando 6
            for col in range(2):  # 2 colunas
                if index >= len(images):
                    break

                img_path = images[index]

                # Adicionando a imagem
                image = Image(source=img_path, size_hint=(None, None), size=(100, 25), pos_hint={'center_x': x_positions[col], 'top': y_top})
                self.add_widget(image)

                # Adicionando a caixa de texto abaixo da imagem
                text_input = TextInput(hint_text="como será o dia?", size_hint=(None, None), size=(100, 60), pos_hint={'center_x': x_positions[col], 'top': y_top - 0.05})
                self.add_widget(text_input)

                index += 1

            y_top -= 0.2  # Atualizando a posição vertical para a próxima linha de pares

        # Adicionando o botão "Salvar" abaixo do último par
        save_button = Button(text="Salvar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'top': y_top - 0.1})
        save_button.bind(on_press=self.save_text)
        self.add_widget(save_button)

    def save_text(self, instance):
        # Implementar funcionalidade de salvar texto aqui, se necessário
        pass

class PlannerApp(App):
    def build(self):
        # Definindo a cor de fundo da janela para ser transparente
        Window.clearcolor = (0, 0, 0, 0)
        
        sm = ScreenManager()
        sm.add_widget(PlannerLayout(name='planner_screen'))
        
        return sm

if __name__ == '__main__':
    Window.size = (350, 550)
    PlannerApp().run()


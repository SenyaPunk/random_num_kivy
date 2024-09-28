from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class NumberGeneratorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text='Сгенерированное число: 0', font_size=24)
        self.layout.add_widget(self.label)

        self.button = Button(text='Сгенерировать число', font_size=24)
        self.button.bind(on_press=self.generate_number)
        self.layout.add_widget(self.button)

        return self.layout

    def generate_number(self, instance):
        number = random.randint(1, 100)  # Генерация случайного числа от 1 до 100
        self.label.text = f'Сгенерированное число: {number}'

if __name__ == '__main__':
    NumberGeneratorApp().run()

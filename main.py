# Импортируем kivy и все необходимые библиотеки, подробнее смотрим на https://kivy.org/doc/stable/
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):

    def build(self): # Метод для построения пользовательского интерфейса приложения
        layout = BoxLayout(orientation='vertical')
        self.expression = ""
        # Создание кнопок
        buttons_layout = BoxLayout()
        normal_btn = Button(text='Обычный', size_hint=(1, 0.1), on_press = CalculatorApp.build)
        engineer_btn = Button(text='Инженерный', size_hint=(1, 0.1), on_press = self.pass_func)
        extra_btn = Button(text = "Дополнительный", size_hint=(1, 0.1), on_press = self.pass_func)

        buttons_layout.add_widget(normal_btn)
        buttons_layout.add_widget(engineer_btn)
        buttons_layout.add_widget(extra_btn)
        layout.add_widget(buttons_layout)

        self.text_input = TextInput(multiline=False, readonly=True, font_size=40) # Создание TextInput для отображения выражения
        layout.add_widget(self.text_input) # Добавление TextInput на экран

        calculator_layout = GridLayout(cols=4)
        buttons = [ # Список кнопок для калькулятора 
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        for button in buttons: # Создание и добавление кнопок в layout
            btn = Button(text=button, font_size=40)
            btn.bind(on_press=self.on_button_press)
            calculator_layout.add_widget(btn)
            
        layout.add_widget(calculator_layout)

        return layout
    
    def engineer(self, instance):
        # очищаем экран
        self.text_input.text = ""
        self.expression = ""
        
    
    def on_button_press(self, instance): # Метод-обработчик нажатия на кнопку
        if instance.text == 'C': # Если нажата кнопка 'C', сбросить выражение
            self.expression = ""
        elif instance.text == '=': # Если нажата кнопка '=', вычислить результат выражения
            try:
                self.expression = str(eval(self.expression)) # Вычисление результата
            except Exception as e: # Обработка ошибок при вычислении
                self.expression = str(e) # Отображение сообщения об ошибке
        else:
            self.expression += instance.text # Добавление символов пользоветельского ввода к выражению

        self.text_input.text = self.expression # Отображение текущего выражения в TextInput

if __name__ == '__main__':
    CalculatorApp().run() # Создание экземпляра приложения и его запуск
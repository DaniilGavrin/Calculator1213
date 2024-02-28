# Импортируем kivy и все необходимые библиотеки, подробнее смотрим на https://kivy.org/doc/stable/
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):

    def build(self): # Метод для построения пользовательского интерфейса приложения
        self.expression = "" # Инициализация переменной для хранения выражения
        layout = GridLayout(cols=1) # Создание Grid layout с одной колонкой

        self.text_input = TextInput(multiline=False, readonly=True, font_size=40) # Создание TextInput для отображения выражения
        layout.add_widget(self.text_input) # Добавление TextInput на экран

        buttons = [ # Список кнопок для калькулятора
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        for button in buttons: # Создание и добавление кнопок в layout
            btn = Button(text=button, font_size=40) # Создание кнопки
            btn.bind(on_press=self.on_button_press) # Привязка обработчика нажатия на кнопку
            layout.add_widget(btn) # Добавление кнопки на экран

        return layout # Возвращаем layout как корневой элемент интерфейса
    
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
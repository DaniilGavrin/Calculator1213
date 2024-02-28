# Импортируем kivy и все необходимые бибилиотеки, подробнее смотрим https://kivy.org/doc/stable/
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):

    def build(self): # 
        self.expression = ""
        layout = GridLayout(cols=1)

        self.text_input = TextInput(multiline=False, readonly=True, font_size=40)
        layout.add_widget(self.text_input)

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        for button in buttons:
            btn = Button(text=button, font_size=40)
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout
    
    def on_button_press(self, instance):
        if instance.text == 'C':
            self.expression = ""
        elif instance.text == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = str(e)
        else:
            self.expression += instance.text

        self.text_input.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run() #запуск приложения
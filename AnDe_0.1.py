import kivy
kivy.require('1.10.0')
  
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
  
# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class AnDe(FloatLayout):
    
    def __init__(self,**kwargs):
        super(AnDe, self).__init__(**kwargs)
        layout = FloatLayout(size=(1800,900))
        button = Button(text='Hello world')
        layout.add_widget(button)


    


class MyApp(App):

    def build(self):
        return AnDe()


if __name__ == '__main__':
    MyApp().run()
'''
this is a library of funtions for frontend manegement
'''
import kivy

import json
import settingsman as st

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class wellcome(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a label
        Textin = TextInput(text="PATH to file for backup replace this text", font_size='24sp')

        # Create a button
        button = Button(text="next", size_hint=(1, 0.2))
        button.bind(on_press=self.on_button_press)

        # Add widgets to the layout
        layout.add_widget(Textin)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        st.update_setting("home_folder",T)


class TestApp(App):
    def build(self):
        return Button(text="Hello World")





if __name__ == '__main__':
    #TestApp().run()
    MyApp().run()

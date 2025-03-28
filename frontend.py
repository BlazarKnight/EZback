'''
this is a library of funtions for frontend manegement
'''
import kivy

import json

from kivy.config import value

import settingsman as st

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from tkinter import filedialog
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

global GLOB_BACK_GROUND_COLOR_AS_RGBA
global GLOB_BORDER_COLOR_AS_RGBA
global GLOB_TEXT_COLOR_AS_RGBA

# set defalt color palet
GLOB_BORDER_COLOR_AS_RGBA = [225,0,0,1] #red
GLOB_TEXT_COLOR_AS_RGBA = [1,1,1,1] #white
GLOB_BACK_GROUND_COLOR_AS_RGBA = [0,0,0,1] #black

#this function is here so we dont need to write it again but dont use or impiment it untill kivy has full coloring suport for all used functions
'''def theme():
    print(bool(st.read_setting("dark_theme")))
    if not  bool(st.read_setting("dark_theme")):
        GLOB_TEXT_COLOR_AS_RGBA = [0,0,0,1] #black
        GLOB_BACK_GROUND_COLOR_AS_RGBA = [1,1,1,1] #white
    return 0'''

class homeselect(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        self.butlay = BoxLayout(orientation='horizontal',spacing=20, padding=20)
        # Create a label
        #Textin = TextInput(text="PATH to file for backup replace this text", font_size='24sp')
        warn_lable= Label(text="input the path of folder you want to back up")


        self.textin= TextInput(multiline=False)
        #textinput.bid(on_text_validate=on_enter)

        # Create a button
        btn1 = Button(text="next", size_hint=(1, 0.2))
        btn2 = Button(text="choose a directory", size_hint=(1, 0.2))
        btn2.bind(on_press=self.on_button2_press)
        btn1.bind(on_press=self.on_button1_press)

        # Add widgets to the layout
        layout.add_widget(warn_lable)
        #layout.add_widget(self.textin)

        self.butlay.add_widget(self.textin)
        self.butlay.add_widget(btn2)
        layout.add_widget(self.butlay)
        layout.add_widget(btn1)


        return layout
    def on_button2_press(self,bnt2):
        self.textin.insert_text(filedialog.askdirectory())



    def on_button1_press(self, btn1):
        st.update_setting(key="home_folder",value=self.textin.text)
        print('The widget', self.textin.text, 'have:',self.textin.text)
        print(type(self.textin.text))

class TestApp(App):
    def build(self):
        return Button(text="Hello World")

def runhomeselect():
    homeselect().run()


if __name__ == '__main__':
    st.init_settings()
    #theme()
    #TestApp().run()
    runhomeselect()

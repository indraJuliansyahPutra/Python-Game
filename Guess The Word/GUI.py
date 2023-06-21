import random
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

class GuessTheWord(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        
        self.word_list = self.load_word_list()
        self.word = ""
        self.guess = []
        self.chances = 10
        
        self.label_info = Label(text="")
        self.add_widget(self.label_info)
        
        self.label_kata = Label(text="")
        self.add_widget(self.label_kata)
        
        self.keyboard_layout = GridLayout(cols = 6, spacing = 10)
        self.add_widget(self.keyboard_layout)
        
        self.label_chance = Label(text="")
        self.add_widget(self.label_chance)
        
        """ self.button_reset = Label(text="Ganti Kata", on_press = self.change_word)
        self.add_widget(self.button_reset) """
        
        self.button_stop = Label(text="Stop Game", on_press = self.stop_game)
        self.add_widget(self.button_stop)
        
        #self.reset_game()
        
        #Window.bind(on_key_down = self.keyboard_on_key_down)
        
    def load_word_list(self):
        with open("Guess The Word\word_list.txt", "r") as file:
            word_list = file.read().splitlines()
        return word_list
        
    """ def change_word():
        App.get_running_app().stop() """
        
    def stop_game(self, instance):
        App.get_running_app().stop()
        
        
class GuessTheWordApp(App):
    def build(self):
        return GuessTheWord()
    
if __name__ == "__main__":
    GuessTheWordApp().run()
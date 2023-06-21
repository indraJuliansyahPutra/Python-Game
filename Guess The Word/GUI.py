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
        super(GuessTheWord, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        
        self.word_list = self.load_word_list()
        self.word = ""
        self.guesses = []
        self.chances = 10
        
        self.label_info = Label(text="")
        self.add_widget(self.label_info)
        
        self.label_word = Label(text="")
        self.add_widget(self.label_word)
        
        self.keyboard_layout = GridLayout(cols = 6, spacing = 10)
        self.add_widget(self.keyboard_layout)
        
        self.label_chance = Label(text="")
        self.add_widget(self.label_chance)
        
        self.button_reset = Button(text="Change The Word", on_press = self.change_word)
        self.add_widget(self.button_reset)
        
        self.button_stop = Button(text="Stop Game", on_press = self.stop_game)
        self.add_widget(self.button_stop)
        
        self.reset_game()
        
        Window.bind(on_key_down = self.keyboard_on_key_down)
        
    def load_word_list(self):
        with open("Guess The Word\word_list.txt", "r") as file:
            word_list = file.read().splitlines()
        return word_list
    
    def create_keyboard(self):
        self.keyboard_layout.clear_widgets()
        
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = Button(text = letter, on_press=self.submit_from_keyboard)
            self.keyboard_layout.add_widget(button)
            
    def reset_game(self, instance = None):
        self.word = self.get_random_word()
        self.guesses = []
        self.chances = 10
        self.update_label_word()
        self.enable_keyboard()
        self.create_keyboard()
        
        self.label_info.text = ""
        
    def submit(self, instance):
        guess = instance.text.lower()
        
        if guess in self.guesses:
            self.label_info.text = "You have already guessed this letter before."
            return
        
        self.guesses.append(guess)
        guess_result = self.guess_the_word()
        
        self.label_word.text = guess_result
        
        if "_" not in guess_result:
            self.label_info.text = "Congratulations! You have successfully guessed the word."
            self.disable_keyboard()
            self.show_result_popup()
        else:
            if guess not in self.word:
                self.chances -= 1
                self.label_info.text = "Your guess is incorrect. You have {} chances left.".format(self.chances)
                
            if self.chances == 0:
                self.label_info.text = "Sorry, you have run out of chances. The correct word is {}".format(self.word)
                self.disable_keyboard()
                self.show_result_popup()
                
    def submit_from_keyboard(self, instance):
        self.submit(instance)
        
    def guess_the_word(self):
        result = ""
        for letter in self.word:
            if letter in self.guesses:
                result += letter + " "
            else:
                result += "_"
        return result.strip()
    
    def disable_keyboard(self):
        for button in self.keyboard_layout.children:
            button.disabled = True
            
    def enable_keyboard(self):
        for button in self.keyboard_layout.children:
            button.disabled = False
            
    def change_word(self, instance):
        self.reset_game()
        
    def stop_game(self, instance):
        App.get_running_app().stop()
        
    def show_result_popup(self, *args):
        content = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10)
        
        label_result = Label(text = "Play Again?")
        content.add_widget(label_result)
        
        button_play_again = Button(text="Play Again", size_hint=(None, None), size=(120, 40))
        button_play_again.bind(on_release=self.reset_game)
        content.add_widget(button_play_again)
        
        button_quit = Button(text = 'Quit', size_hint = (None, None), size = (120, 40))
        button_quit.bind(on_release = self.stop_game)
        content.add_widget(button_quit)
        
        popup = Popup(title = "Result: " + self.word, content = content, size_hint = (None, None), size = (300, 200), auto_dismiss = False)
        
        button_play_again.bind(on_release = popup.dismiss)
        button_quit.bind(on_release = self.stop_game)
        
        popup.open()
        
    def get_random_word(self):
        return random.choice(self.word_list)
    
    def update_label_word(self):
        self.label_word.text = "_" * len(self.word)
        
    def keyboard_on_key_down(self, window, key, *args):
        character = chr(key).lower()
        
        if character.isalpha():
            self.submit_from_keyboard(Button(text = character))
        
        
class GuessTheWordApp(App):
    def build(self):
        return GuessTheWord()
    
if __name__ == "__main__":
    GuessTheWordApp().run()
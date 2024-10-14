import logic
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
# from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager

class MainMenuScreen(Screen):

    def __init__(self, **kwargs):

        super(MainMenuScreen, self).__init__(**kwargs)

        Window.size = (1920, 1080)
        # Window.clearcolor = (0, 0, 0, 1)
        Window.fullscreen = True
        layout = FloatLayout()

        background = Image(source="background//rps3.jpg", allow_stretch = True, keep_ratio = False)

        self.label = Label(text = "[color=ffffff]Welcome  to  Rock Paper  and  Scissors![/color]", markup = True, font_size = 40,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.4, 'center_y': 0.8},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        self.label2 = Label(text = "[color=ffffff]guilehideout[/color]", markup = True, font_size = 20,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.1, 'center_y': 0.05},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        button1 = Button(text="Play", size_hint=(0.05, 0.05), pos_hint={'x':0.2, 'y':0.5}, background_color = (1, 1, 1, 1),
                         font_name = "font//ARCADECLASSIC.TTF", font_size = 30)
        button1.bind(on_press=self.on_button_1_click)
        button1.bind(on_release=self.on_button_release)

        button2 = Button(text="Quit", size_hint=(0.05, 0.05), pos_hint={'x':0.4, 'y':0.5}, background_color = (1, 1, 1, 1),
                         font_name = "font//ARCADECLASSIC.TTF", font_size = 30)
        button2.bind(on_press=self.on_button_2_click)
        button2.bind(on_release=self.on_button_release)

        Window.bind(on_key_down=self.on_key_down)
        # background_video = Video(source="video//videoplayback.mp4", state='play')
        # background_video.options = {'eos':'loop'}
        # background_video.play = True
        # layout.add_widget(background_video)

        layout.add_widget(background)
        layout.add_widget(self.label)
        layout.add_widget(self.label2)
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)
        # return layout
    
    def on_button_1_click(self, instance):
        instance.background_color = (1, 1, 1, 1)
        self.manager.current = 'game_screen'
        
    def on_button_release(self, instance):
        instance.background_color = (1, 1, 1, 1)

    def on_button_2_click(self, instance):
        self.label.text = "Thanks for playing!"
        instance.background_color = (1, 1, 1, 1)
        Clock.schedule_once(self.stopApp, 2)

    # def goToGameplayScreen(self, instance):
    #     self.manager.current = 'game_screen'

    def stopApp(self, dt):
        App.get_running_app().stop()

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        if codepoint == ' ':
            fileHandle = open("text.txt", 'w')
            fileHandle.write('hi')


class GameplayScreen(Screen):

    def __init__(self, **kwargs):

        super(GameplayScreen, self).__init__(**kwargs)

        Window.size = (1920, 1080)
        Window.fullscreen = True
        # Window.clearcolor = (0, 0, 0, 1)

        layout = FloatLayout()

        background = Image(source="background//rps3.jpg", allow_stretch = True, keep_ratio = False)

        # rock_art = Image(source="pixel_art//scissors.png", allow_strech = True, keep_ratio = False)

        self.label = Label(text = "[color=ffffff]Welcome  to  Rock Paper  and  Scissors![/color]", markup = True,
                      font_size=40, size_hint = (0.200, 0.50), pos_hint={'center_x': 0.4, 'center_y': 0.8},
                      font_name = "font//ARCADECLASSIC.TTF")

        self.label2 = Label(text = "[color=ffffff]Select your move![/color]", markup = True, font_size = 40,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.4, 'center_y': 0.6},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        self.label3 = Label(text = "[color=ffffff]guilehideout[/color]", markup = True, font_size = 20,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.1, 'center_y': 0.05},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        self.rockLabel = Label(text = "[color=ffffff]Rock[/color]", markup = True, font_size = 40,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.15, 'center_y': 0.27},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        self.paperLabel = Label(text = "[color=ffffff]Paper[/color]", markup = True, font_size = 40,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.35, 'center_y': 0.27},
                      font_name = "font//ARCADECLASSIC.TTF")
        
        self.scissorsLabel = Label(text = "[color=ffffff]Scissors[/color]", markup = True, font_size = 40,
                      size_hint = (0.200, 0.50), pos_hint={'center_x': 0.55, 'center_y': 0.27},
                      font_name = "font//ARCADECLASSIC.TTF")

        button1 = Button(text="Back to Main Menu", size_hint=(0.15, 0.05), pos_hint={'x':0.2, 'y':0.1}, background_color = (1, 1, 1, 1),
                         font_name = "font//ARCADECLASSIC.TTF", font_size = 30)
        button1.bind(on_press=self.on_button_1_click)

        button2 = Button(text="Quit", size_hint=(0.05, 0.05), pos_hint={'x':0.4, 'y':0.1}, background_color = (1, 1, 1, 1),
                         font_name = "font//ARCADECLASSIC.TTF", font_size = 30)
        button2.bind(on_press=self.on_button_2_click)

        rockButton = Button(size_hint=(0.15, 0.25), pos_hint={'x':0.07,'y':0.3}, font_name = "font//ARCADECLASSIC.TTF",
                             font_size = 40, background_normal="pixel_art//rock.png")
        rockButton.bind(on_press=self.on_rock_button_click)
        
        PaperButton = Button(size_hint=(0.15, 0.25), pos_hint={'x':0.27,'y':0.3}, font_name = "font//ARCADECLASSIC.TTF",
                             font_size = 40, background_normal="pixel_art//paper.png")
        PaperButton.bind(on_press=self.on_paper_button_click)

        ScissorsButton = Button(size_hint=(0.15, 0.25), pos_hint={'x':0.47,'y':0.3}, font_name = "font//ARCADECLASSIC.TTF",
                             font_size = 40, background_normal="pixel_art//scissors.png")
        ScissorsButton.bind(on_press=self.on_scissors_button_click)

        layout.add_widget(background)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(rockButton)
        layout.add_widget(PaperButton)
        layout.add_widget(ScissorsButton)
        layout.add_widget(self.label)
        layout.add_widget(self.label2)
        layout.add_widget(self.label3)
        layout.add_widget(self.rockLabel)
        layout.add_widget(self.paperLabel)
        layout.add_widget(self.scissorsLabel)

        self.add_widget(layout)

    def on_button_1_click(self, instance):
        self.manager.current = 'main_menu'
    
    def on_button_2_click(self, instance):
        self.label.text = "Thanks for playing!"
        self.label2.text = ''
        instance.background_color = (1, 1, 1, 1)
        Clock.schedule_once(self.stopApp, 2)

    def on_rock_button_click(self, instance):
        comp_choice = logic.ComputerChoice()
        user_choice = "Rock"
        self.label2.text = f"Computer chose {comp_choice}\nYou chose {user_choice}\nSo {logic.WhoWon(user_choice, comp_choice)}"
        
    def on_paper_button_click(self, instance):
        comp_choice = logic.ComputerChoice()
        user_choice = "Paper"
        self.label2.text = f"Computer chose {comp_choice}\nYou chose {user_choice}\nSo {logic.WhoWon(user_choice, comp_choice)}"
        
    def on_scissors_button_click(self, instance):
        comp_choice = logic.ComputerChoice()
        user_choice = "Scissors"
        self.label2.text = f"Computer chose {comp_choice}\nYou chose {user_choice}\nSo {logic.WhoWon(user_choice, comp_choice)}"

    def stopApp(self, dt):
        App.get_running_app().stop()


class RockPaperScissorsApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainMenuScreen(name = 'main_menu'))
        sm.add_widget(GameplayScreen(name = 'game_screen'))

        sm.current = 'main_menu'

        return sm

# if __name__ == "__main__":
#     RockPaperScissorsApp().run()
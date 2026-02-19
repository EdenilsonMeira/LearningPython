from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from helper import username_helper


class MegaPlayApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        button = MDRectangleFlatButton(text="Submit",
                                       pos_hint={'center_x': .5, 'center_y': .4},
                                       on_release=self.show_data)

        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print(self.username.text)


MegaPlayApp().run()

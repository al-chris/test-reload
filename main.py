from kivymd.uix.screen import MDScreen
from kivymd.tools.hotreload.app import MDApp
import os
from kivymd.uix.screenmanager import ScreenManager

class UI(ScreenManager):
    def change_screen(self, screen_name):
        self.current = screen_name

class FirstScreen(MDScreen):
    pass

class SecondScreen(MDScreen):
    pass


class MyApp(MDApp):
    DEBUG = True
    KV_DIRS = [
        os.getcwd(), # current directory for app.kv
        os.path.join(os.getcwd(), "screens"),
        os.path.join(os.getcwd(), "widgets"),
        os.path.join(os.getcwd(), "themes"),
        os.path.join(os.getcwd(), "assets"),
    ]

    def __init__(self, *args):
        super().__init__(*args)

    def build_app(self):
        self.manager_screens = UI()
        return self.manager_screens
    

if __name__ == '__main__':
    MyApp().run()

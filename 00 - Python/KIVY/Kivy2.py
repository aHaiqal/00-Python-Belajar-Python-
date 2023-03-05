from kivymd.app import MDApp 
from kivymd.uix.screenmanager import ScreenManager

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Test(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            

        ]
        return self.wm


if __name__ == '__main__':
    Test().run()
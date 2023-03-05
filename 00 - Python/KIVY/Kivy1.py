from kivymd.app import MDApp 
from kivymd.uix.button import MDRoundFlatIconButton

class Test(MDApp):
    def build(self):
        return MDRoundFlatIconButton(icon = 'language-python', pos_hint = {'center_x': .5, 'center_y' : .7}, text = 'Halooo')


if __name__ == '__main__':
    Test().run()

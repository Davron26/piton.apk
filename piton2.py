from kivy.app import App
from kivy.uix.image import Image
#from kivy.uix.button import Button

class PitonApp(App):
    def build(self):
        img = Image(source='figure-up.gif')

        return img
        #return Button(text="Test")

if __name__=="__main__":
    PitonApp().run()
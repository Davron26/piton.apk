from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.uix.carousel import Carousel
from kivy.animation import Animation
from kivy.uix.button import Button

class PitonApp(App):
    def c_animation(self,instance):
        animation=Animation(pos=(200,0))
        animation.start(self.img)
    def build(self):
        btn=Button(text="Move",on_press=self.c_animation)
        self.img = Image(source='figure-right.gif')

        self.img.add_widget(btn)

        return self.img
if __name__=="__main__":
    PitonApp().run()
from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.clock import Clock

class PitonApp(App):
    #velocity = ListProperty([10, 15])
    #def __init__(self, **kwargs):
    #    super(PitonApp, self).__init__(**kwargs)
    #    Clock.schedule_interval(self.r_animation)

    #def update(self, *args):
    #    self.img.x += self.velocity[0]
    #    self.img.y += self.velocity[1]
#
    #    if self.img.x < 0 or (self.img.x + self.img.width) > Window.width:
    #        self.velocity[0] *= -1
    #    if self.img.y < 0 or (self.img.y + self.img.width) > Window.width:
    #        self.velocity[0] *= -1

    def r_animation(self, instance):
        self.img.source = 'figure-right.gif'
        #animation = Animation(x=+500)
        #animation.start(self.img)
        #while self.img.source == 'figure-right.gif':
        self.img.x += 5

    def d_animation(self, instance):
        self.img.source = 'figure-down.gif'
        #animation = Animation(y=+500)
        #animation.start(self.img)
        self.img.y -= 5

    def l_animation(self, instance):
        self.img.source = 'figure-left.gif'
        #animation = Animation(x=-500)
        #animation.start(self.img)
        self.img.x -= 5

    def u_animation(self, instance):
        self.img.source = 'figure-up.gif'
        #animation = Animation(y=-500)
        #animation.start(self.img)
        self.img.y += 5

    def build(self):
        gl = GridLayout(rows=2, padding=[0, 100, 0, 0], size_hint=(1, .5))
        fl = FloatLayout(size=(500, 500))

        btn_u = Button(text="^", on_press=self.u_animation)
        btn_d = Button(text="v", on_press=self.d_animation)
        btn_l = Button(text="<", on_press=self.l_animation)
        btn_r = Button(text=">", on_press=self.r_animation)

        self.img = Image(source='figure-down.gif')

        fl.add_widget(self.img)
        fl.add_widget(gl)

        gl.add_widget(Widget())
        gl.add_widget(btn_u)
        gl.add_widget(Widget())
        gl.add_widget(btn_l)
        gl.add_widget(btn_d)
        gl.add_widget(btn_r)

        return fl


if __name__ == "__main__":
    PitonApp().run()

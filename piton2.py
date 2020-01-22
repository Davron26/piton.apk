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

upni = 0
downni = 0
leftni = 0
rightni = 0

class PitonApp(App):
    def r_animation(self, instance):
        self.img.source = 'figure-right.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 0
        leftni = 0
        rightni = 1
        #Clock.schedule_interval(self.runpiton, 0.1)

    def d_animation(self, instance):
        self.img.source = 'figure-down.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 1
        leftni = 0
        rightni = 0
        #Clock.schedule_interval(self.runpiton, 0.1)

    def l_animation(self, instance):
        self.img.source = 'figure-left.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 0
        leftni = 1
        rightni = 0
        #Clock.schedule_interval(self.runpiton, 0.1)

    def u_animation(self, instance):
        self.img.source = 'figure-up.gif'
        global upni, downni, leftni, rightni
        upni = 1
        downni = 0
        leftni = 0
        rightni = 0

    def runpiton(self, *args):
        if upni == 1:
            self.img.y += 5
        if downni == 1:
            self.img.y -= 5
        if leftni == 1:
            self.img.x -= 5
        if rightni == 1:
            self.img.x += 5

    def build(self):
        gl = GridLayout(rows=2, padding=[0, 100, 0, 0], size_hint=(1, .5))
        fl = FloatLayout(size=(500, 500))

        btn_u = Button(text="^", on_press=self.u_animation)
        btn_d = Button(text="v", on_press=self.d_animation)
        btn_l = Button(text="<", on_press=self.l_animation)
        btn_r = Button(text=">", on_press=self.r_animation)

        self.img = Image(source='figure-down.gif')
        Clock.schedule_interval(self.runpiton, 0.01)

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

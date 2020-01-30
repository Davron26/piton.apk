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
import random

upni = 0
downni = 0
leftni = 0
rightni = 0
hasItem = True

o = random.randint(-240, 240)
p = random.randint(-150, 300)

Window.size = (500, 600)

class PitonApp(App):
    def redraw(self, args):
        self.wgt.bg_rect.size = self.wgt.size
        self.wgt.bg_rect.pos = self.wgt.pos
    def r_animation(self, instance):
        self.img.source = 'figure-right.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 0
        leftni = 0
        rightni = 1

    def d_animation(self, instance):
        self.img.source = 'figure-down.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 1
        leftni = 0
        rightni = 0

    def l_animation(self, instance):
        self.img.source = 'figure-left.gif'
        global upni, downni, leftni, rightni
        upni = 0
        downni = 0
        leftni = 1
        rightni = 0

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
        if self.img.x == 250 or self.img.x == -250:
            Window.close()
        if self.img.y == 300 or self.img.y == -150:
            Window.close()

    def build(self):
        gl = GridLayout(rows=2, padding=[0, 150, 0, 0], size_hint=(1, .5))
        fl = FloatLayout(size=(500, 500))

        btn_u = Button(text="^", on_press=self.u_animation)
        btn_d = Button(text="v", on_press=self.d_animation)
        btn_l = Button(text="<", on_press=self.l_animation)
        btn_r = Button(text=">", on_press=self.r_animation)

        self.bgd = Image(source='background.gif')
        self.img = Image(source='figure-down.gif')
        self.itm = Image(source='item.gif')

        Clock.schedule_interval(self.runpiton, 0.02)

        fl.add_widget(self.bgd)
        fl.add_widget(self.itm)
        fl.add_widget(self.img)
        fl.add_widget(gl)

        gl.add_widget(Widget())
        gl.add_widget(btn_u)
        gl.add_widget(Widget())
        gl.add_widget(btn_l)
        gl.add_widget(btn_d)
        gl.add_widget(btn_r)

        self.bgd.pos = [0, 100]
        self.img.pos = [0, 80]
        self.itm.pos = [o, p]

        """if (hasItem):
            try:
                x1, y1 = canvas.coords(item)
                x2, y2 = canvas.coords(mytriangle)
            except ValueError:
                pass
            x2 += 8;
            y2 += 6
            if (abs(x1 - x2) < 5) and (abs(y1 - y2) < 5):
                opit += 1
                canvas.delete(ochko)
                ochko = canvas.create_text(45, 10, text=opit, fill="white")
                o = random.randint(10, 490)
                p = random.randint(10, 490)
                canvas.coords(item, o, p)"""

        return fl

if __name__ == "__main__":
    PitonApp().run()

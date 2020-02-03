from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.label import Label
import random

upni = 0
downni = 0
leftni = 0
rightni = 0
hasItem = True
opit = str(0)
number = 0

o = random.randint(20, Window.width - 20)
p = random.randint(20, Window.height - 20)

Window.size = (500, 600)

class PitonApp(App):
    def itmcall(self):
        o = random.randint(0, Window.width)
        p = random.randint(0, Window.height)
        self.itm.pos = [o, p]
    def redraw(self, *args):
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
        global opit
        global number
        print(self.itm.pos)

        def lose(self, *args):
            self.gl.remove_widget(self.w)
            self.gl.remove_widget(self.btn_u)
            self.gl.remove_widget(self.w1)
            self.gl.remove_widget(self.btn_l)
            self.gl.remove_widget(self.btn_d)
            self.gl.remove_widget(self.btn_r)

            self.fl.remove_widget(self.bgd)
            self.fl.remove_widget(self.ochko)
            self.fl.remove_widget(self.point)
            self.fl.remove_widget(self.itm)
            self.fl.remove_widget(self.img)
            self.fl.remove_widget(self.gl)

            self.fl.add_widget(Label(text='Вы проиграли', pos=[0, 50], font_size=(30)))
            self.fl.add_widget(Label(text='Очки: ', pos=[-20, 15], font_size=(30)))
            self.fl.add_widget(Label(text=opit, pos=[30, 15], font_size=(30)))
        if upni == 1:
            self.img.y += 5
        if downni == 1:
            self.img.y -= 5
        if leftni == 1:
            self.img.x -= 5
        if rightni == 1:
            self.img.x += 5

        if self.img.x < 0 or (self.img.x + self.img.width) > Window.width:
            lose(self)
        if self.img.y < 0 or (self.img.y + self.img.height) > Window.height:
            lose(self)

        if self.itm.x < 0 or (self.itm.x + self.itm.width) > Window.width:
            PitonApp.itmcall(self)
        if self.itm.y < 0 or (self.itm.y + self.itm.height) > Window.height:
            PitonApp.itmcall(self)

        if self.img.collide_widget(self.btn_u) == True or self.img.collide_widget(self.w) == True \
                or self.img.collide_widget(self.w1):
            lose(self)

        if self.itm.collide_widget(self.btn_u) == True or self.itm.collide_widget(self.w) == True \
                or self.itm.collide_widget(self.w1) == True or self.itm.collide_widget(self.btn_l) == True \
                or self.itm.collide_widget(self.btn_d) == True or self.itm.collide_widget(self.btn_r) == True:
            PitonApp.itmcall(self)

        if (hasItem):
            try:
                x1, y1 = self.itm.pos
                x2, y2 = self.img.pos
            except ValueError:
                pass
            x2 += 8
            y2 += 6
            if (abs(x1 - x2) < 7) and (abs(y1 - y2) < 7):
                number += 1
                opit = str(number)
                self.point.text = opit
                o = random.randint(20, Window.width - 20)
                p = random.randint(20, Window.height - 20)
                self.itm.pos = [o, p]
    def build(self):
        self.gl = GridLayout(rows=2, padding=[0, 150, 0, 0], size_hint=(1, .5))
        self.fl = FloatLayout(size=(500, 500))

        self.btn_u = Button(text="^", on_press=self.u_animation)
        self.btn_d = Button(text="v", on_press=self.d_animation)
        self.btn_l = Button(text="<", on_press=self.l_animation)
        self.btn_r = Button(text=">", on_press=self.r_animation)
        self.w = Widget()
        self.w1 = Widget()

        self.bgd = Image(source='background.gif')
        self.bgd.size_hint_max = self.bgd.texture_size
        self.ochko = Label(text='Очки:')
        self.point = Label(text=opit)
        self.img = Image(source='figure-down.gif')
        self.img.size_hint_max = self.img.texture_size
        self.itm = Image(source='item.gif')
        self.itm.size_hint_max = self.itm.texture_size

        Clock.schedule_interval(self.runpiton, 0.03)

        self.bgd.pos = [0, 150]
        self.ochko.pos = [-220, 285]
        self.point.pos = [-195, 285]
        self.img.pos = [240, 375]
        self.itm.pos = [o, p]

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.ochko)
        self.fl.add_widget(self.point)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.img)
        self.fl.add_widget(self.gl)

        self.gl.add_widget(self.w)
        self.gl.add_widget(self.btn_u)
        self.gl.add_widget(self.w1)
        self.gl.add_widget(self.btn_l)
        self.gl.add_widget(self.btn_d)
        self.gl.add_widget(self.btn_r)

        return self.fl


if __name__ == "__main__":
    PitonApp().run()

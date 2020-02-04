import kivy
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

    def restart(self, instance):
        global number
        global opit
        global upni, downni, leftni, rightni

        number = 0
        opit = str(number)

        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)

        self.fl.clear_widgets()

        try:
            self.bl.add_widget(self.rubtn)
            self.bl.add_widget(self.enbtn)
            self.bl.add_widget(self.ochko)
            self.bl.add_widget(self.point)
        except kivy.uix.widget.WidgetException:
            pass

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.img)
        self.fl.add_widget(self.gl)

        self.bgd.pos = [0, 150]
        self.img.pos = [240, 375]
        self.itm.pos = [o, p]

        self.img.source = 'figure-up.gif'

        self.point.text = opit

        upni = 0
        downni = 0
        leftni = 0
        rightni = 0

    def english(self, instance):
        self.w1.text = 'Restart'

        self.ochko.text = 'Points:'
        self.ochko.pos = [-225, 285]

        # self.los.text = 'You lose'
        # self.pon.text = 'Points: '
        self.en = 1
        self.ru = 0

    def russian(self, instance):
        self.w1.text = 'Рестарт'

        self.ochko.text = 'Очки:'
        self.ochko.pos = [-220, 285]

        # self.los.text = 'Вы проиграли'
        # self.pon.text = 'Очки: '
        self.en = 0
        self.ru = 1

    def runpiton(self, *args):
        self.los = Label(text='Вы проиграли', pos=[0, 50], font_size=(30))
        self.pon = Label(text='Очки: ', pos=[-20, 15], font_size=(30))
        self.sub1 = Label(text='Piton ver.1.0', pos=[100, -100])
        self.sub2 = Label(text='(c) Davron Tokhirov, Feb.2020', pos=[100, -120])

        global opit
        global number

        def lose(self, *args):
            self.bl.remove_widget(self.rubtn)
            self.bl.remove_widget(self.enbtn)
            self.bl.remove_widget(self.ochko)
            self.bl.remove_widget(self.point)

            self.fl.remove_widget(self.bgd)
            self.fl.remove_widget(self.ochko)
            self.fl.remove_widget(self.point)
            self.fl.remove_widget(self.itm)
            self.fl.remove_widget(self.img)

            opit = str(number)

            self.fl.add_widget(self.los)
            self.fl.add_widget(self.pon)
            self.fl.add_widget(Label(text=opit, pos=[30, 15], font_size=(30)))
            self.fl.add_widget(self.sub1)
            self.fl.add_widget(self.sub2)

        if self.en == 1 and self.ru == 0:
            self.los.text = 'You lose'
            self.pon.text = 'Points: '
        if self.en == 0 and self.ru == 1:
            self.los.text = 'Вы проиграли'
            self.pon.text = 'Очки: '
        if self.en == 0 and self.ru == 0:
            self.los.text = 'Вы проиграли'
            self.pon.text = 'Очки: '

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
            self.img.pos = [240, 375]

        if self.img.y < 0 or (self.img.y + self.img.height) > Window.height:
            lose(self)
            self.img.pos = [240, 375]

        if self.itm.x < 0 or (self.itm.x + self.itm.width) > Window.width:
            PitonApp.itmcall(self)
        if self.itm.y < 0 or (self.itm.y + self.itm.height) > Window.height:
            PitonApp.itmcall(self)

        if self.img.collide_widget(self.btn_u) == True or self.img.collide_widget(self.bl) == True \
                or self.img.collide_widget(self.w1):
            lose(self)
            self.img.pos = [240, 375]

        if self.itm.collide_widget(self.btn_u) == True or self.itm.collide_widget(self.bl) == True \
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
        self.en = 0
        self.ru = 0

        self.gl = GridLayout(rows=2, padding=[0, 150, 0, 0], size_hint=(1, .5))
        self.fl = FloatLayout(size=(500, 500))
        self.bl = GridLayout(rows=2, cols=2)

        self.btn_u = Button(text="^", on_press=self.u_animation)
        self.btn_d = Button(text="v", on_press=self.d_animation)
        self.btn_l = Button(text="<", on_press=self.l_animation)
        self.btn_r = Button(text=">", on_press=self.r_animation)
        self.w1 = Button(text="Рестарт", on_press=self.restart)

        self.rubtn = Button(text="RU", font_size=(13), on_press=self.russian)
        self.enbtn = Button(text="EN", font_size=(13), on_press=self.english)

        self.bgd = Image(source='background.gif')
        self.bgd.size_hint_max = self.bgd.texture_size
        self.ochko = Label(text='Очки:')
        self.point = Label(text=opit)
        self.img = Image(source='figure-down.gif')
        self.img.size_hint_max = self.img.texture_size
        self.itm = Image(source='item.gif')
        self.itm.size_hint_max = self.itm.texture_size

        self.event = Clock.schedule_interval(self.runpiton, 0.03)

        self.bgd.pos = [0, 150]
        self.point.pos = [-195, 285]
        self.img.pos = [240, 375]
        self.itm.pos = [o, p]

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.img)
        self.fl.add_widget(self.gl)

        self.gl.add_widget(self.bl)
        self.gl.add_widget(self.btn_u)
        self.gl.add_widget(self.w1)
        self.gl.add_widget(self.btn_l)
        self.gl.add_widget(self.btn_d)
        self.gl.add_widget(self.btn_r)

        self.bl.add_widget(self.rubtn)
        self.bl.add_widget(self.enbtn)
        self.bl.add_widget(self.ochko)
        self.bl.add_widget(self.point)

        return self.fl


if __name__ == "__main__":
    PitonApp().run()

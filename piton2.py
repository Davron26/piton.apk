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
from kivy.core.audio import SoundLoader
import random
import time

upni = 0
downni = 0
leftni = 0
rightni = 0
hasItem = True
opit = str(0)
number = 0

eat = SoundLoader.load('eat.wav')

o = random.randint(20, Window.width - 20)
p = random.randint(20, Window.height - 20)

class PitonApp(App):
    def itmcall(self):
        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)
        self.itm.pos = [o, p]

    def r_animation(self, instance):
        if self.sptime == False:
            self.img.source = 'figure-right.gif'
            global upni, downni, leftni, rightni
            upni = 0
            downni = 0
            leftni = 0
            rightni = 1
        else:
            pass

    def d_animation(self, instance):
        global upni, downni, leftni, rightni
        if self.sptime == False:
            if upni == 1:
                pass
            else:
                self.img.source = 'figure-down.gif'
                upni = 0
                downni = 1
                leftni = 0
                rightni = 0
        else:
            pass

    def l_animation(self, instance):
        if self.sptime == False:
            self.img.source = 'figure-left.gif'
            global upni, downni, leftni, rightni
            upni = 0
            downni = 0
            leftni = 1
            rightni = 0
        else:
            pass

    def u_animation(self, instance):
        global upni, downni, leftni, rightni
        if self.sptime == False:
            if downni == 1:
                pass
            else:
                self.img.source = 'figure-up.gif'
                upni = 1
                downni = 0
                leftni = 0
                rightni = 0
        else:
            pass

    def restart(self, instance):
        if self.pause.text == 'Продолжить':
            self.event = Clock.schedule_interval(self.runpiton, self.timer)
            self.pause.text = 'Пауза'
            self.sptime = False
        global number
        global opit
        global upni, downni, leftni, rightni

        number = 0
        opit = str(number)

        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)

        self.fl.clear_widgets()

        try:
            self.bl.remove_widget(self.ochko)
            self.bl.remove_widget(self.point)
            self.bl.add_widget(self.ochko)
            self.bl.add_widget(self.point)
        except kivy.uix.widget.WidgetException:
            pass

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.img)
        self.fl.add_widget(self.gl)

        self.fl.add_widget(self.up)
        self.fl.add_widget(self.down)
        self.fl.add_widget(self.right)
        self.fl.add_widget(self.left)

        self.bgd.pos = [0, 0]
        self.img.pos = [Window.width / 2, Window.height / 2]
        self.itm.pos = [o, p]

        self.img.source = 'figure-up.gif'

        self.point.text = opit

        self.timer = 0.03

        upni = 0
        downni = 0
        leftni = 0
        rightni = 0

    def english(self, instance):
        self.w1.text = 'Restart'

        self.pause.text = 'Pause'

        self.options.text = 'Options'
        self.ochko.text = 'Points:'
        self.los.text = 'You lose'

        self.proz.text = 'Transparent wall'
        self.real.text = 'Not transparent wall'

        self.en = 1
        self.ru = 0

    def russian(self, instance):
        self.w1.text = 'Рестарт'

        self.pause.text = 'Пауза'

        self.options.text = 'Опция'
        self.ochko.text = 'Очки:'
        self.los.text = 'Вы проиграли'

        self.proz.text = 'Прозрачная стена'
        self.real.text = 'Непрозрачная стена'

        self.en = 0
        self.ru = 1

    def lose(self):
        self.fl.remove_widget(self.bgd)
        self.fl.remove_widget(self.itm)
        self.fl.remove_widget(self.img)

        self.fl.add_widget(self.los)
        self.fl.add_widget(self.sub1)
        self.fl.add_widget(self.sub2)

    def funproz(self, instance):
        self.devol = False

    def funreal(self, instance):
        self.devol = True

    def runoptions(self, instance):
        self.restart(instance)
        self.lose()
        self.fl.remove_widget(self.los)
        self.fl.remove_widget(self.sub1)
        self.fl.remove_widget(self.sub2)

        self.glo = GridLayout(cols=2, padding = [0, 0, 0, Window.height / 4])
        self.rubtn = Button(text='Русский язык', on_press = self.russian)
        self.enbtn = Button(text='English language', on_press = self.english)
        self.proz = Button(text='Прозрачная стена', on_press = self.funproz)
        self.real = Button(text='Непрозрачная стена', on_press = self.funreal)

        self.fl.add_widget(self.glo)

        self.glo.add_widget(self.rubtn)
        self.glo.add_widget(self.enbtn)
        self.glo.add_widget(self.proz)
        self.glo.add_widget(self.real)

    def runpause(self, instance):
        if self.pause.text == 'Пауза':
            self.event = Clock.unschedule(self.runpiton)
            self.pause.text = 'Продолжить'
            self.sptime = True
        elif self.pause.text == 'Продолжить':
            self.event = Clock.schedule_interval(self.runpiton, self.timer)
            self.pause.text = 'Пауза'
            self.sptime = False

    def runpiton(self, *args):
        self.gl.padding = [0, Window.height / 4, 0, 0]
        self.bgd.pos = [0, Window.height / 4]
        self.img.size_hint_max = Window.height / 45, Window.height / 45
        self.itm.size_hint_max = Window.height / 60, (Window.height / 60) + 1

        self.up.size_hint_max = Window.height / 25, Window.height / 25
        self.down.size_hint_max = Window.height / 25, Window.height / 25
        self.right.size_hint_max = Window.height / 25, Window.height / 25
        self.left.size_hint_max = Window.height / 25, Window.height / 25

        self.up.pos = [Window.width / 2.15, Window.height / 5.5]
        self.down.pos = [Window.width / 2.15, Window.height / 20.5]
        self.right.pos = [Window.width / 1.256, Window.height / 20.5]
        self.left.pos = [Window.width / 6.65, Window.height / 20.5]

        self.los = Label(text='Вы проиграли', pos=[0, 0 + Window.height / 4])
        self.sub1 = Label(text='Piton ver.1.1', pos=[0, (self.w1.pos[1] * -1) + 50])
        self.sub2 = Label(text='(c) Davron Tokhirov, Feb.2020', pos=[0, (self.w1.pos[1] * -1)])

        global opit
        global number

        if self.en == 1 and self.ru == 0:
            self.los.text = 'You lose'
            try:
                self.proz.text = 'Transparent wall'
                self.real.text = 'Not transparent wall'
            except AttributeError:
                pass
        if self.en == 0 and self.ru == 1:
            self.los.text = 'Вы проиграли'
            try:
                self.proz.text = 'Прозрачная стена'
                self.real.text = 'Непрозрачная стена'
            except AttributeError:
                pass
        if self.en == 0 and self.ru == 0:
            self.los.text = 'Вы проиграли'
            try:
                self.proz.text = 'Прозрачная стена'
                self.real.text = 'Непрозрачная стена'
            except AttributeError:
                pass

        if upni == 1:
            self.img.y += 5
        if downni == 1:
            self.img.y -= 5
        if leftni == 1:
            self.img.x -= 5
        if rightni == 1:
            self.img.x += 5

        if self.img.x < 0 or self.img.x > Window.width:
            if self.devol:
                self.lose()
            if self.devol == False:
                if self.img.x < 0:
                    self.img.x = Window.width
                if self.img.x > Window.width:
                    self.img.x = 0

        if self.img.y > Window.height:
            if self.devol:
                self.lose()
            if self.devol == False:
                self.img.y = Window.height / 3.9

        if self.itm.x < 0 or (self.itm.x + self.itm.width) > Window.width:
            PitonApp.itmcall(self)
        if self.itm.y < 0 or (self.itm.y + self.itm.height) > Window.height:
            PitonApp.itmcall(self)

        if self.img.collide_widget(self.btn_u) or self.img.collide_widget(self.bl)  \
                or self.img.collide_widget(self.pause):
            if self.devol:
                self.lose()
            if self.devol == False:
                self.img.y = Window.height

        if self.itm.collide_widget(self.btn_u) or self.itm.collide_widget(self.bl)  \
                or self.itm.collide_widget(self.pause) or self.itm.collide_widget(self.btn_l)  \
                or self.itm.collide_widget(self.btn_d) or self.itm.collide_widget(self.btn_r) :
            PitonApp.itmcall(self)

        if self.img.collide_widget(self.itm):
                eat.play()
                number += 1
                opit = str(number)
                self.point.text = opit
                PitonApp.itmcall(self)
                self.speed += 1
                if self.speed == 3:
                    self.event = Clock.unschedule(self.runpiton)
                    self.timer -= 0.0050
                    self.event = Clock.schedule_interval(self.runpiton, self.timer)

    def build(self):
        self.en = 0
        self.ru = 0
        self.timer = 0.03
        self.devol = True
        self.sptime = 0
        self.speed = 0

        self.gl = GridLayout(rows=2, padding=[0, 0, 0, 0], size_hint=(1, .5))
        self.fl = FloatLayout(size=(500, 500))
        self.bl = GridLayout(rows=2, cols=2)

        self.btn_u = Button(on_press=self.u_animation)
        self.btn_d = Button(on_press=self.d_animation)
        self.btn_l = Button(on_press=self.l_animation)
        self.btn_r = Button(on_press=self.r_animation)

        self.options = Button(text="Опция", on_press=self.runoptions)
        self.w1 = Button(text="Рестарт", on_press=self.restart)

        self.bgd = Image(source='background.gif', allow_stretch = True, keep_ratio = False)
        self.ochko = Label(text='Очки:')
        self.point = Label(text=opit)
        self.img = Image(source='figure-down.gif', allow_stretch = True, keep_ratio = False)
        self.itm = Image(source='item.gif', allow_stretch = True, keep_ratio = False)

        self.up = Image(source='up.png')
        self.down = Image(source='down.png')
        self.right = Image(source='right.png')
        self.left = Image(source='left.png')

        self.pause = Button(text='Пауза', on_press=self.runpause)

        self.event = Clock.schedule_interval(self.runpiton, self.timer)

        self.bgd.pos = [0, 0]
        self.img.pos = [Window.width / 2, Window.height / 2]
        self.itm.pos = [o, p]

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.img)
        self.fl.add_widget(self.gl)

        self.gl.add_widget(self.bl)
        self.gl.add_widget(self.btn_u)
        self.gl.add_widget(self.pause)
        self.gl.add_widget(self.btn_l)
        self.gl.add_widget(self.btn_d)
        self.gl.add_widget(self.btn_r)

        self.bl.add_widget(self.options)
        self.bl.add_widget(self.w1)
        self.bl.add_widget(self.ochko)
        self.bl.add_widget(self.point)

        self.fl.add_widget(self.up)
        self.fl.add_widget(self.down)
        self.fl.add_widget(self.right)
        self.fl.add_widget(self.left)

        return self.fl


if __name__ == "__main__":
    PitonApp().run()
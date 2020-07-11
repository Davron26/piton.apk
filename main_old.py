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

speed_x = 0
speed_y = 0
hasItem = True
opit = str(0)
number = 0

eat = SoundLoader.load('sounds/eat.wav')
music = SoundLoader.load('sounds/music.mp3')

o = random.randint(20, Window.width - 20)
p = random.randint(20, Window.height - 20)

class PitonApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.imglist = None

    def itmcall(self):
        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)
        self.itm.pos = [o, p]

    def r_animation(self, instance):
        if self.sptime == False:
            global speed_x, speed_y
            if speed_x != -5:
                self.imglist[0].source = 'images/figure-right.gif'
                speed_x = 5
                speed_y = 0

    def d_animation(self, instance):
        if self.sptime == False:
            global speed_x, speed_y
            if speed_y != 5:
                self.imglist[0].source = 'images/figure-down.gif'
                speed_x = 0
                speed_y = -5

    def l_animation(self, instance):
        if self.sptime == False:
            global speed_x, speed_y
            if speed_x != 5:
                self.imglist[0].source = 'images/figure-left.gif'
                speed_x = -5
                speed_y = 0

    def u_animation(self, instance):
        if self.sptime == False:
            global speed_x, speed_y
            if speed_y != -5:
                self.imglist[0].source = 'images/figure-up.gif'
                speed_x = 0
                speed_y = 5

    def restart(self, instance):
        self.lose()
        self.game_over = False
        self.del_imglist = False
        self.coordinates.clear()
        self.coordinates.insert(0, self.imglist[0].pos.copy())

        self.chislo = 0

        if self.pause.text == 'Продолжить':
            self.event = Clock.schedule_interval(self.runpiton, self.timer)
            self.pause.text = 'Пауза'
            self.sptime = False
        global number
        global opit
        global speed_x, speed_y

        number = 0
        opit = str(number)

        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)

        try:
            self.glo.remove_widget(self.w2)
        except AttributeError:
            pass
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
        self.fl.add_widget(self.imglist[0])
        self.fl.add_widget(self.gl)

        self.fl.add_widget(self.up)
        self.fl.add_widget(self.down)
        self.fl.add_widget(self.right)
        self.fl.add_widget(self.left)

        self.bgd.pos = [0, 0]
        self.imglist[0].pos = [Window.width / 2, Window.height / 2]
        self.itm.pos = [o, p]

        self.imglist[0].source = 'images/figure-up.gif'

        self.point.text = opit

        self.timer = 0.025

        speed_x = 0
        speed_y = 0

        self.new_tail_counter = 1000

    def english(self, instance):
        self.w1.text = 'Restart'
        self.w2.text = 'Restart'

        if self.sptime != True:
            self.pause.text = 'Pause'
        else:
            self.pause.text = 'Continue'

        self.options.text = 'Options'
        self.ochko.text = 'Points:'
        self.los.text = 'You lose'

        self.proz.text = 'Transparent wall'
        self.real.text = 'Not transparent wall'

        self.en = 1
        self.ru = 0

    def russian(self, instance):
        self.w1.text = 'Рестарт'
        self.w2.text = 'Рестарт'

        if self.sptime != True:
            self.pause.text = 'Пауза'
        else:
            self.pause.text = 'Продолжить'

        self.options.text = 'Опция'
        self.ochko.text = 'Очки:'
        self.los.text = 'Вы проиграли'

        self.proz.text = 'Сквозные края'
        self.real.text = 'Закрытые края'

        self.en = 0
        self.ru = 1

    def lose(self, *args):
        if self.sptime != True:
            self.game_over = True
            self.fl.remove_widget(self.bgd)
            self.fl.remove_widget(self.itm)
            self.fl.remove_widget(self.imglist[0])
            self.del_imglist = True

            self.fl.add_widget(self.los)
            self.fl.add_widget(self.sub1)
            self.fl.add_widget(self.sub2)
            try:
                self.fl.add_widget(self.options)
                self.fl.add_widget(self.w1)
            except kivy.uix.widget.WidgetException:
                pass

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
        self.fl.remove_widget(self.options)
        self.fl.remove_widget(self.w1)

        self.glo = GridLayout(rows=3, padding = [0, 0, 0, Window.height / 4])
        self.rubtn = Button(text='Русский язык', on_press = self.russian)
        self.enbtn = Button(text='English language', on_press = self.english)
        self.proz = Button(text='Сквозные края', on_press = self.funproz)
        self.real = Button(text='Закрытые края', on_press = self.funreal)

        self.fl.add_widget(self.glo)

        self.glo.add_widget(self.rubtn)
        self.glo.add_widget(self.enbtn)
        self.glo.add_widget(self.proz)
        self.glo.add_widget(self.real)
        self.glo.add_widget(Widget())
        self.glo.add_widget(self.w2)

    def runpause(self, instance):
        if self.pause.text == 'Пауза' or self.pause.text == 'Pause':
            self.event = Clock.unschedule(self.runpiton)
            if self.ru == 1:
                self.pause.text = 'Продолжить'
            if self.en == 1:
                self.pause.text = 'Continue'
            else:
                self.pause.text = 'Продолжить'
            self.sptime = True

            if self.game_over != True:
                self.fl.remove_widget(self.los)
                self.fl.remove_widget(self.sub1)
                self.fl.remove_widget(self.sub2)
                self.fl.remove_widget(self.options)
                self.fl.remove_widget(self.w1)

                self.glo = GridLayout(rows=3, padding=[0, 0, 0, Window.height / 4])
                self.rubtn = Button(text='Русский язык', on_press=self.russian)
                self.enbtn = Button(text='English language', on_press=self.english)
                self.proz = Button(text='Сквозные края', on_press=self.funproz)
                self.real = Button(text='Закрытые края', on_press=self.funreal)

                self.fl.add_widget(self.glo)

                self.glo.add_widget(self.rubtn)
                self.glo.add_widget(self.enbtn)
                self.glo.add_widget(self.proz)
                self.glo.add_widget(self.real)
                self.glo.add_widget(Widget())
                self.glo.add_widget(self.w2)
        elif self.pause.text == 'Продолжить' or self.pause.text == 'Continue':
            self.event = Clock.schedule_interval(self.runpiton, self.timer)
            if self.ru == 1:
                self.pause.text = 'Пауза'
            if self.en == 1:
                self.pause.text = 'Pause'
            else:
                self.pause.text = 'Пауза'
            self.sptime = False

            if self.game_over != True:
                self.fl.remove_widget(self.glo)

                self.glo.remove_widget(self.rubtn)
                self.glo.remove_widget(self.enbtn)
                self.glo.remove_widget(self.proz)
                self.glo.remove_widget(self.real)
                self.glo.remove_widget(Widget())
                self.glo.remove_widget(self.w2)

    def runpiton(self, *args):
        global opit
        global number

        try:
            music.play()
        except AttributeError:
            pass

        self.gl.padding = [0, Window.height / 4, 0, 0]
        self.bgd.pos = [0, Window.height / 4]
        self.imglist[0].size_hint_max = Window.height / 45, Window.height / 45
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
        self.sub1 = Label(text='Piton ver.1.2', pos=[0, (self.pause.pos[1] * -1)])
        self.sub2 = Label(text='(c) Davron Tokhirov, May.2020', pos=[0, (self.pause.pos[1] * -1) - 50])

        self.options.pos = [Window.width / 2.5, Window.height / 2]
        self.w1.pos = [Window.width / 2.5, self.options.pos[1] - self.options.size_hint_max[1]]

        if self.del_imglist == True:
            for i in range(1, self.chislo + 1):
                try:
                    self.fl.remove_widget(self.imglist[i])
                    self.imglist.pop(i)
                except IndexError:
                    pass

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
                self.proz.text = 'Сквозные края'
                self.real.text = 'Закрытые края'
            except AttributeError:
                pass
        if self.en == 0 and self.ru == 0:
            self.los.text = 'Вы проиграли'
            try:
                self.proz.text = 'Сквозные края'
                self.real.text = 'Закрытые края'
            except AttributeError:
                pass

        self.imglist[0].x += speed_x
        self.imglist[0].y += speed_y
        if speed_x != 0 or speed_y != 0:
            self.coordinates.insert(0, self.imglist[0].pos.copy())
            self.new_tail_counter += 1
            try:
                if self.new_tail_counter == (int((self.imglist[self.chislo].size_hint_max[0] / 3))):
                    self.imglist.append(Image(source='images/figure.gif', allow_stretch=True, keep_ratio=False))
                    self.chislo = len(self.imglist) - 1
                    self.imglist[self.chislo].size_hint_max = Window.height / 45, Window.height / 45
                    self.fl.add_widget(self.imglist[self.chislo])
                elif self.new_tail_counter > (int((self.imglist[self.chislo].size_hint_max[0] / 3))):
                    self.coordinates.pop(len(self.coordinates) - 1)
            except IndexError:
                pass

        for i in range(2, self.chislo + 1):
            try:
                if self.imglist[0].collide_widget(self.imglist[i]):
                    self.lose()
            except IndexError:
                pass

        for i in range(1, self.chislo + 1):
            try:
                self.imglist[i].size_hint_max = Window.height / 45, Window.height / 45
                self.imglist[i].pos = self.coordinates[i * int((self.imglist[i].size_hint_max[0] / 4.3))]
            except IndexError:
                pass

        if self.imglist[0].x < 0 or self.imglist[0].x > Window.width:
            if self.devol:
                self.lose()
            if self.devol == False:
                if self.imglist[0].x < 0:
                    self.imglist[0].x = Window.width
                if self.imglist[0].x > Window.width:
                    self.imglist[0].x = 0

        if self.imglist[0].y > Window.height:
            if self.devol:
                self.lose()
            if self.devol == False:
                self.imglist[0].y = Window.height / 3.9

        if self.itm.x < 0 or (self.itm.x + self.itm.width) > Window.width:
            PitonApp.itmcall(self)
        if self.itm.y < 0 or (self.itm.y + self.itm.height) > Window.height:
            PitonApp.itmcall(self)

        if self.imglist[0].collide_widget(self.btn_u) or self.imglist[0].collide_widget(self.bl)\
                or self.imglist[0].collide_widget(self.pause):
            if self.devol:
                self.lose()
            if self.devol == False:
                self.imglist[0].y = Window.height

        if self.itm.collide_widget(self.btn_u) or self.itm.collide_widget(self.bl) \
                or self.itm.collide_widget(self.pause) or self.itm.collide_widget(self.btn_l) \
                or self.itm.collide_widget(self.btn_d) or self.itm.collide_widget(self.btn_r) :
            PitonApp.itmcall(self)

        if self.imglist[0].collide_widget(self.itm):
            eat.play()
            self.new_tail_counter = 0
            number += 1
            opit = str(number)
            self.point.text = opit
            PitonApp.itmcall(self)
            self.speed += 1
            if self.speed == 3:
                self.speed = 0
                self.event = Clock.unschedule(self.runpiton)
                self.timer -= 0.0025#на сколько будет меняться скорость
                self.event = Clock.schedule_interval(self.runpiton, self.timer)

    def build(self):
        self.en = 0
        self.ru = 0
        self.timer = 0.025#текущая скорость
        self.devol = True
        self.sptime = 0
        self.speed = 0
        self.new_tail_counter = 1000
        self.chislo = 0
        self.del_imglist = False
        self.game_over = False

        self.gl = GridLayout(rows=2, padding=[0, 0, 0, 0], size_hint=(1, .5))
        self.fl = FloatLayout(size=(500, 500))
        self.bl = GridLayout(rows=2, cols=2)

        self.btn_u = Button(on_press=self.u_animation)
        self.btn_d = Button(on_press=self.d_animation)
        self.btn_l = Button(on_press=self.l_animation)
        self.btn_r = Button(on_press=self.r_animation)

        self.options = Button(text="Опция", on_press=self.runoptions)
        self.w1 = Button(text="Рестарт", on_press=self.restart)
        self.w2 = Button(text="Рестарт", on_press=self.restart)

        self.options.size_hint_max = Window.width / 5, Window.height / 20
        self.w1.size_hint_max = Window.width / 5, Window.height / 20

        self.bgd = Image(source='images/background.gif', allow_stretch = True, keep_ratio = False)
        self.ochko = Label(text='Очки:')
        self.point = Label(text=opit)
        self.imglist = [Image(source='images/figure-down.gif', allow_stretch = True, keep_ratio = False)]
        self.itm = Image(source='images/item.gif', allow_stretch = True, keep_ratio = False)

        self.up = Image(source='images/up.png')
        self.down = Image(source='images/down.png')
        self.right = Image(source='images/right.png')
        self.left = Image(source='images/left.png')

        self.pause = Button(text='Пауза', on_press=self.runpause)

        self.event = Clock.schedule_interval(self.runpiton, self.timer)

        self.bgd.pos = [0, 0]
        self.imglist[0].pos = [Window.width / 2, Window.height / 2]
        self.coordinates = [self.imglist[0].pos]
        self.itm.pos = [o, p]

        self.fl.add_widget(self.bgd)
        self.fl.add_widget(self.itm)
        self.fl.add_widget(self.imglist[0])
        self.fl.add_widget(self.gl)

        self.gl.add_widget(self.bl)
        self.gl.add_widget(self.btn_u)
        self.gl.add_widget(self.pause)
        self.gl.add_widget(self.btn_l)
        self.gl.add_widget(self.btn_d)
        self.gl.add_widget(self.btn_r)

        self.bl.add_widget(self.ochko)
        self.bl.add_widget(self.point)

        self.fl.add_widget(self.up)
        self.fl.add_widget(self.down)
        self.fl.add_widget(self.right)
        self.fl.add_widget(self.left)

        return self.fl

if __name__ == "__main__":
    PitonApp().run()

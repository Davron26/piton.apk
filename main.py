import random
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.clock import Clock
from kivy.core.audio import SoundLoader


class HomeScreen(Screen):
    pass
class LoseScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")
eat = SoundLoader.load('sounds/eat.ogg')
music = SoundLoader.load('sounds/music.ogg')

#Window.size = (360, 720)

class MainApp(App):
    def itmcall(self):
        home_screen = self.root.ids["home_screen"]
        itm = home_screen.ids["itm"]
        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)
        itm.pos = [o, p]

    def r_animation(self):
        if self.sptime == False:
            if self.speed_x != -5:
                self.imglist[0].source = 'images/figure-right.png'
                self.speed_x = 5
                self.speed_y = 0

    def d_animation(self):
        if self.sptime == False:
            if self.speed_y != 5:
                self.imglist[0].source = 'images/figure-down.png'
                self.speed_x = 0
                self.speed_y = -5

    def l_animation(self):
        if self.sptime == False:
            if self.speed_x != 5:
                self.imglist[0].source = 'images/figure-left.png'
                self.speed_x = -5
                self.speed_y = 0

    def u_animation(self):
        if self.sptime == False:
            if self.speed_y != -5:
                self.imglist[0].source = 'images/figure-up.png'
                self.speed_x = 0
                self.speed_y = 5

    def lose(self):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = "lose_screen"
        self.game_over = True
        music.stop()

    def runpause(self):
        home_screen = self.root.ids["home_screen"]
        pause = home_screen.ids["pause"]

        if not self.game_over:
            if pause.text == 'Пауза' or pause.text == 'Pause':
                self.event = Clock.unschedule(self.runpiton)
                if self.lang == 0:
                    pause.text = 'Продолжить'
                else:
                    pause.text = 'Continue'
                self.sptime = True

                if self.game_over == False:
                    tr = NoTransition()
                    screen_manager = self.root.ids["screen_manager"]
                    screen_manager.transition = tr
                    screen_manager.current = "settings_screen"

            else:
                self.event = Clock.schedule_interval(self.runpiton, self.timer)
                if self.lang == 0:
                    pause.text = 'Пауза'
                else:
                    pause.text = 'Pause'
                self.sptime = False

                tr = NoTransition()
                screen_manager = self.root.ids["screen_manager"]
                screen_manager.transition = tr
                screen_manager.current = "home_screen"

    def restart(self):
        home_screen = self.root.ids["home_screen"]
        itm = home_screen.ids["itm"]
        point = home_screen.ids["point"]
        fl = home_screen.ids["fl"]
        lose_screen = self.root.ids["lose_screen"]
        point2 = lose_screen.ids["point2"]

        for i in range(0, self.chislo + 1):
            fl.remove_widget(self.imglist[i])

        self.imglist = [Image(source='images/figure-down.png', allow_stretch=True,
                              keep_ratio=False, size_hint_max=(Window.height / 45, Window.height / 45),
                              pos=[Window.width / 2, Window.height / 2])]
        fl.add_widget(self.imglist[0])

        self.game_over = False
        self.chislo = 0
        self.number = 0
        self.opit = str(self.number)
        self.new_tail_counter = 1000
        self.speed_x = 0
        self.speed_y = 0
        self.timer = self.default_time
        self.coordinates.clear()
        self.coordinates.insert(0, self.imglist[0].pos.copy())

        if self.sptime == True:
            MainApp.runpause(self)

        o = random.randint(20, Window.width - 20)
        p = random.randint(20, Window.height - 20)

        self.imglist[0].pos = [Window.width / 2, Window.height / 2]
        self.imglist[0].source = 'images/figure-down.png'
        itm.pos = [o, p]
        point.text = self.opit
        point2.text = self.opit

        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = "home_screen"

        music.play()

    def funproz(self):
        self.devol = False

    def funreal(self):
        self.devol = True

    def english(self):
        home_screen = self.root.ids["home_screen"]
        point_text = home_screen.ids["point_text"]

        lose_screen = self.root.ids["lose_screen"]
        los = lose_screen.ids["los"]
        ochko = lose_screen.ids["ochko"]
        pause_button = lose_screen.ids["pause_button"]
        restart = lose_screen.ids["restart"]

        settings_screen = self.root.ids["settings_screen"]
        proz = settings_screen.ids["proz"]
        real = settings_screen.ids["real"]
        ochko2 = settings_screen.ids["ochko2"]
        pause2 = settings_screen.ids["pause2"]
        restart2 = settings_screen.ids["restart2"]

        self.lang = 1

        point_text.text = 'Points:'

        los.text = 'You lose'
        ochko.text = 'Points:'
        pause_button.text = 'Pause'
        restart.text = 'Restart'

        proz.text = 'Transparent wall'
        real.text = 'Not transparent wall'
        ochko2.text = 'Points:'
        pause2.text = 'Continue'
        restart2.text = 'Restart'
    def russian(self):
        home_screen = self.root.ids["home_screen"]
        point_text = home_screen.ids["point_text"]

        lose_screen = self.root.ids["lose_screen"]
        los = lose_screen.ids["los"]
        ochko = lose_screen.ids["ochko"]
        pause_button = lose_screen.ids["pause_button"]
        restart = lose_screen.ids["restart"]

        settings_screen = self.root.ids["settings_screen"]
        proz = settings_screen.ids["proz"]
        real = settings_screen.ids["real"]
        ochko2 = settings_screen.ids["ochko2"]
        pause2 = settings_screen.ids["pause2"]
        restart2 = settings_screen.ids["restart2"]

        self.lang = 0

        point_text.text = 'Очки:'

        los.text = 'Вы проиграли'
        ochko.text = 'Очки:'
        pause_button.text = 'Пауза'
        restart.text = 'Рестарт'

        proz.text = 'Сквозные края'
        real.text = 'Закрытые края'
        ochko2.text = 'Очки:'
        pause2.text = 'Продолжить'
        restart2.text = 'Рестарт'
    def runpiton(self, *args):
        if not self.is_setup:
            self.setup()

        home_screen = self.root.ids["home_screen"]
        itm = home_screen.ids["itm"]
        point = home_screen.ids["point"]
        fl = home_screen.ids["fl"]
        lose_screen = self.root.ids["lose_screen"]
        point2 = lose_screen.ids["point2"]

        self.imglist[0].x += self.speed_x
        self.imglist[0].y += self.speed_y

        if self.speed_x != 0 or self.speed_y != 0:
            self.coordinates.insert(0, self.imglist[0].pos.copy())
            self.new_tail_counter += 1
            if self.new_tail_counter == (int((self.imglist[self.chislo].size_hint_max[0] / 3))):
                self.imglist.append(Image(source='images/figure.png', allow_stretch=True, keep_ratio=False))
                self.chislo = len(self.imglist) - 1
                self.imglist[self.chislo].size_hint_max = Window.height / 45, Window.height / 45
                fl.add_widget(self.imglist[self.chislo])
            elif self.new_tail_counter > (int((self.imglist[self.chislo].size_hint_max[0] / 3))):
                self.coordinates.pop(len(self.coordinates) - 1)
        for i in range(2, self.chislo + 1):
            if self.imglist[0].collide_widget(self.imglist[i]):
                self.lose()
        for i in range(1, self.chislo + 1):
            self.imglist[i].pos = self.coordinates[i * int((self.imglist[i].size_hint_max[0] / 4.3))]

        if self.imglist[0].x < 0 or self.imglist[0].x > Window.width - 13:
            if self.devol:
                self.lose()
            else:
                if self.imglist[0].x < 0:
                    self.imglist[0].x = Window.width
                if self.imglist[0].x > Window.width:
                    self.imglist[0].x = 0
        if self.imglist[0].y > Window.height - 13:
            if self.devol:
                self.lose()
            else:
                self.imglist[0].y = Window.height / 4 + 1
        if self.imglist[0].y < Window.height / 4:
            if self.devol:
                self.lose()
            else:
                self.imglist[0].y = Window.height - 13

        if itm.x < 0 or (itm.x + itm.width) > Window.width:
            MainApp.itmcall(self)
        if itm.y < 0 or (itm.y + itm.height) > Window.height:
            MainApp.itmcall(self)
        if itm.y < Window.height / 4:
            MainApp.itmcall(self)
        if self.imglist[0].collide_widget(itm):
            eat.play()
            self.new_tail_counter = 0
            self.number += 1
            self.opit = str(self.number)
            point.text = self.opit
            point2.text = self.opit
            MainApp.itmcall(self)
            self.speed += 1
            if self.speed == 2:
                self.speed = 0
                self.event = Clock.unschedule(self.runpiton)
                self.timer -= 0.0025  # на сколько будет меняться скорость
                self.event = Clock.schedule_interval(self.runpiton, self.timer)

    def setup(self):
        music.loop = True
        music.play()

        self.is_setup = True
        home_screen = self.root.ids["home_screen"]
        fl = home_screen.ids["fl"]
        self.imglist = [Image(source='images/figure-down.png', allow_stretch=True,
                              keep_ratio=False, size_hint_max=(Window.height / 45, Window.height / 45),
                              pos=[Window.width / 2, Window.height / 2])]

        self.lang = 0  # 0 = RU; 1 = EN
        self.sptime = False
        self.speed_x = 0
        self.speed_y = 0
        self.new_tail_counter = 1000
        self.number = 0
        self.opit = str(0)
        self.speed = 0
        self.coordinates = [self.imglist[0].pos]
        self.chislo = 0
        self.devol = True
        self.game_over = False
        self.music_pos = 0

        fl.add_widget(self.imglist[0])

    def build(self):
        self.default_time = Window.height / 122500
        self.timer = self.default_time
        self.is_setup = False
        self.event = Clock.schedule_interval(self.runpiton, self.timer)
        return GUI

    """def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = "home_screen"""

MainApp().run()

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.clock import Clock

class HomeScreen(Screen):
    pass
class LoseScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        home_screen = self.root.ids["home_screen"]

        self.sptime = False
        self.timer = 0.025
        self.speed_x = 0
        self.speed_y = 0

        self.imglist = [home_screen.ids["piton"]]

        self.event = Clock.schedule_interval(self.runpiton, self.timer)

        return GUI
    def r_animation(self):
        if self.sptime == False:
            if self.speed_x != -5:
                self.imglist[0].source = 'images/figure-right.gif'
                self.speed_x = 5
                self.speed_y = 0
    def d_animation(self):
        if self.sptime == False:
            if self.speed_y != 5:
                self.imglist[0].source = 'images/figure-down.gif'
                self.speed_x = 0
                self.speed_y = -5
    def l_animation(self):
        if self.sptime == False:
            if self.speed_x != 5:
                self.imglist[0].source = 'images/figure-left.gif'
                self.speed_x = -5
                self.speed_y = 0
    def u_animation(self):
        if self.sptime == False:
            if self.speed_y != -5:
                self.imglist[0].source = 'images/figure-up.gif'
                self.speed_x = 0
                self.speed_y = 5
    def runpiton(self, *args):
        self.imglist[0].x += self.speed_x
        self.imglist[0].y += self.speed_y
        print(self.imglist[0].pos)
    """def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = "home_screen"""

MainApp().run()


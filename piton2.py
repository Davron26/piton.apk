from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class PitonApp(App):
    def r_animation(self,instance):
        animation=Animation(x=+390)
        animation.start(self.img)
    def d_animation(self,instance):
        animation=Animation(y=+160)
        animation.start(self.img)
    def l_animation(self,instance):
        animation=Animation(x=-390)
        animation.start(self.img)
    def u_animation(self,instance):
        animation=Animation(y=+440)
        animation.start(self.img)
    def build(self):
        gl=GridLayout(rows=1)
        bl=BoxLayout(orientation='vertical')

        btn_u = Button(text="Up", on_press=self.u_animation)
        btn_d = Button(text="Down", on_press=self.d_animation)
        btn_l = Button(text="Left", on_press=self.l_animation)
        btn_r = Button(text="Right",on_press=self.r_animation)

        self.img = Image(source='figure-down.gif')

        bl.add_widget(self.img)
        bl.add_widget(gl)

        gl.add_widget(btn_u)
        gl.add_widget(btn_d)
        gl.add_widget(btn_r)
        gl.add_widget(btn_l)

        return bl
if __name__=="__main__":
    PitonApp().run()
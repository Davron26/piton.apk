from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = (1, 1, 1, 1)

class PitonApp(App):
    def r_animation(self,instance):
        animation=Animation(x=+390)
        animation.start(self.img)
    def d_animation(self,instance):
        animation=Animation(y=+60)
        animation.start(self.img)
    def l_animation(self,instance):
        animation=Animation(x=-390)
        animation.start(self.img)
    def u_animation(self,instance):
        animation=Animation(y=+440)
        animation.start(self.img)
    def build(self):
        gl=GridLayout(rows=2,padding=[0,100,0,0])
        bl=BoxLayout(orientation='vertical')

        btn_u = Button(text="^", on_press=self.u_animation)
        btn_d = Button(text="v", on_press=self.d_animation)
        btn_l = Button(text="<", on_press=self.l_animation)
        btn_r = Button(text=">",on_press=self.r_animation)

        self.img = Image(source='figure-down.gif')

        bl.add_widget(self.img)
        bl.add_widget(gl)

        gl.add_widget(Widget())
        gl.add_widget(btn_u)
        gl.add_widget(Widget())
        gl.add_widget(btn_l)
        gl.add_widget(btn_d)
        gl.add_widget(btn_r)

        return bl
if __name__=="__main__":
    PitonApp().run()
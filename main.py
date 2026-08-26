from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Keja47App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='KEJA 47', font_size=40, bold=True))
        layout.add_widget(Label(text='Garissa Rentals - Find Your Home', font_size=18))
        layout.add_widget(Label(text='Welcome Victor!', font_size=20))
        btn = Button(text='Search Houses', size_hint=(1,0.3), background_color=(0,0.7,0,1))
        btn.bind(on_press=lambda x: print("Searching..."))
        layout.add_widget(btn)
        return layout

Keja47App().run()

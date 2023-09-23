from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import requests
import json
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

Window.size = (300, 500)


class FaceRecognitionScreenFound(Screen):
    pass


class FaceRecognitionScreenNotFound(Screen):
    pass


class LoginPage(Screen):
    pass


class RegisterPage(Screen):
    pass


class Demo(Screen):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)

    def NearestPoliceStation(self):
        print("Nearest Police station")

    def NearestHospital(self):
        print("Nearest Hospital")

    def ScanFace(self):
        print("Scan Face")

    def EmergencyCall(self):
        print("Emergency Call")

    def Login(self):
        print("logged in successfully")

    def Registration(self):
        print("Registered successfully")

    def HelpCenter(self):
        print("HelpCenter")

    def MessageCenter(self):
        print("Message Center")

    def AboutUs(self):
        print("About Us")

    def Settings(self):
        print("Settings")


class Main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        Builder.load_file("My.kv")
        screen = ScreenManager(transition=FadeTransition())
        screen.add_widget(Demo(name='Demo'))
        screen.add_widget(FaceRecognitionScreenFound(
            name='FaceRecognitionScreenFound'))
        screen.add_widget(LoginPage(
            name='LoginPage'))
        screen.add_widget(RegisterPage(
            name='RegisterPage'))
        screen.add_widget(FaceRecognitionScreenNotFound(
            name='FaceRecoginitionScreenNotFound'))

        return screen


Main().run()

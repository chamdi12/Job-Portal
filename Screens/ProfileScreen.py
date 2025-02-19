
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import os

kv_path = os.path.join(os.path.dirname(__file__), "../kv/profile_screen.kv")
Builder.load_file(kv_path)  

class ProfileScreen(MDScreen):  
    pass

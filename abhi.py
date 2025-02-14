from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from kivymd.uix.gridlayout import MDGridLayout

Window.maximize()

KV = """
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Job Portal"
            elevation: 10
            left_action_items: [["menu", lambda x: app.open_menu(x)]]

        MDBoxLayout:
            adaptive_height: True
            padding: [dp(450), dp(20), dp(400), 0]

            MDTextField:
                hint_text: "Search for jobs..."
                size_hint_x: 0.3  # Reducing the width
                pos_hint: {"center_x": 0.5}  # Keeping it centered horizontally
                mode: "rectangle"
                padding: [0, dp(40), 0, 0]  # Moving it down
                on_focus:
                    if self.focus: self.hint_text = ""
                    else: self.hint_text = "Search for jobs..." 
        MDBoxLayout:
            MDGridLayout:
                adaptive_height: True

                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "400dp", "100dp"
                    MDLabel:
                        text: "Software Engineer"
                        halign: "center"



 


        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(40)
            pos_hint: {"center_y": 0.5}
"""

class MainScreen(Screen):
    pass


class JobPortalApp(MDApp):
    def build(self):
        self.menu_items = [
            {"viewclass": "OneLineListItem", "text": "Home", "on_release": lambda: self.menu_callback("home")},
            {"viewclass": "OneLineListItem", "text": "About Us", "on_release": lambda: self.menu_callback("about")},
            {"viewclass": "OneLineListItem", "text": "Logout", "on_release": lambda: self.menu_callback("logout")},
        ]
        
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4
        )
        return Builder.load_string(KV)
    
    def open_menu(self, button):
        self.menu.caller = button
        self.menu.open()
    
    def menu_callback(self, text_item):
        print(f"Selected menu item: {text_item}")
        self.menu.dismiss()

if __name__ == "__main__":
    JobPortalApp().run()

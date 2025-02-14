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
        size_hint_x: 1  
        
        MDTopAppBar:
            md_bg_color: 0, 0, 0.6, 1
            title: "Job Portal"
        
        MDBoxLayout:
            md_bg_color: 0, 0, 0.6, 1
            MDLabel: 
                text: "Find your Dream Job"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                halign: "center"
                font_style: "H3"
                bold: True

        MDBoxLayout:
            # md_bg_color: 0,0,0,1
            orientation: "vertical"
            size_hint_x: 0.5
            size_hint_y: None  
            pos_hint: {"center_x": 0.5, "center_y": -1}
            spacing: dp(30)

            MDBoxLayout: 
                spacing: dp(50)
                size_hint_y: None
                MDTextField:
                    hint_text: "Search for jobs..." 
                    size_hint_x: 0.5
                    pos_hint: {"center_x": 0.5} 
                    mode: "rectangle"
                    padding: [0, dp(40), 0, 0]  
                    on_focus:
                        if self.focus: self.hint_text = ""
                        else: self.hint_text = "Search for jobs..." 

                MDTextField:
                    hint_text: "Location" 
                    size_hint_x: 0.5
                    pos_hint: {"center_x": 0.5} 
                    mode: "rectangle"
                    padding: [0, dp(40), 0, 0]  
                    on_focus:
                        if self.focus: self.hint_text = ""
                        else: self.hint_text = "Search for jobs..."

                MDRaisedButton:
                    text: "Search"
                    size_hint_x: 0.2
                    size_hint_y: 0.5 
                    md_bg_color: 0, 0, 0.6, 1
                    text_color: 1, 1, 1, 1  # White text
                    elevation: 0  # No shadow



            MDGridLayout:
                cols: 3
                spacing: dp(10)
                padding: dp(20)
                
                MDCard:
                    size_hint: None, None
                    size: dp(300), dp(140) 
                    padding: dp(10)
                    MDLabel:
                        text: "Job 1"
                        halign: "center"
        Widget:
            size_hint_y: 1
                

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

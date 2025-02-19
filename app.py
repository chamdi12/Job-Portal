from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from Screens.HomeScreen import HomeScreen
from Screens.ProfileScreen import ProfileScreen 

class Jobportalapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.font_styles.update({
            "H1": ["Roboto", 96, False, -1.5],
            "H2": ["Roboto", 60, False, -0.5],
            "H3": ["Roboto", 48, False, 0],
            "H4": ["Roboto", 34, False, 0.25],
            "H5": ["Roboto", 24, False, 0],
            "H6": ["Roboto", 20, False, 0.15],
            "Subtitle1": ["Roboto", 16, False, 0.15],
            "Subtitle2": ["Roboto", 14, False, 0.1],
            "Body1": ["Roboto", 16, False, 0.5],
            "Body2": ["Roboto", 14, False, 0.25],
            "Button": ["Roboto", 14, True, 1.25],
            "Caption": ["Roboto", 12, False, 0.4],
            "Overline": ["Roboto", 10, True, 1.5],
        })
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(HomeScreen(name = "Home"))
        sm.add_widget(ProfileScreen(name = "Profile"))

        return sm

    def open_profile(self):
        self.root.current = "Profile"


if __name__=="__main__":
    Jobportalapp().run()
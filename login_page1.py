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
from kivy.core.window import Window
from pymongo import MongoClient

Window.maximize()

KV = """
ScreenManager:
    MainScreen:
    JobSeekerScreen:
    JobGiverScreen:

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Job Portal"
            elevation: 9
            
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(400)
            pos_hint: {"center_y": 0.5}
            
            MDLabel:
                text: "Welcome to Job Portal"
                halign: "center"
                font_style: "H4"

            MDBoxLayout:
                orientation: "horizontal"
                spacing: dp(20)
                size_hint: None, None
                size: dp(350), dp(48)
                pos_hint: {"center_x": 0.53, "center_y": 0.5}
                
                MDRaisedButton:
                    text: "Job Seeker Login"
                    size_hint_x: None
                    width: dp(150)
                    on_release: app.root.current = "job_seeker"

                MDRaisedButton:
                    text: "Job Giver Login"
                    size_hint_x: None
                    width: dp(150)
                    on_release: app.root.current = "job_giver"

<JobSeekerScreen>:
    name: "job_seeker"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Job Seeker Login"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(280)

            MDCard:
                padding: dp(20)
                size_hint: None, None
                size: dp(350), dp(450)
                pos_hint: {"center_x": 0.5}

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(10)

                    MDTextField:
                        id: seeker_name
                        hint_text: "First Name"

                    MDTextField:
                        id: seeker_lastname
                        hint_text: "Last Name"

                    MDTextField:
                        id: seeker_email
                        hint_text: "Email"

                    MDTextField:
                        id: seeker_phone
                        hint_text: "Phone Number"
                        input_filter: "int"

                    MDTextField:
                        id: seeker_password
                        hint_text: "Password"
                        password: True

                    MDRaisedButton:
                        text: "Submit"
                        on_release: app.submit_job_seeker()
                        pos_hint: {"center_x": 0.5}

<JobGiverScreen>:
    name: "job_giver"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Job Giver Login"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(280)

            MDCard:
                padding: dp(20)
                size_hint: None, None
                size: dp(350), dp(450)
                pos_hint: {"center_x": 0.5}

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(10)

                    MDTextField:
                        id: giver_name
                        hint_text: "First Name"

                    MDTextField:
                        id: giver_lastname
                        hint_text: "Last Name"

                    MDTextField:
                        id: giver_email
                        hint_text: "Email"

                    MDTextField:
                        id: giver_phone
                        hint_text: "Phone Number"
                        input_filter: "int"

                    MDTextField:
                        id: giver_password
                        hint_text: "Password"
                        password: True

                    MDRaisedButton:
                        text: "Submit"
                        on_release: app.submit_job_giver()
                        pos_hint: {"center_x": 0.5}
"""

class MainScreen(Screen):
    pass

class JobSeekerScreen(Screen):
    pass

class JobGiverScreen(Screen):
    pass


class JobPortalApp(MDApp):
    def change_screen(self, screen_name):
        self.root.current = screen_name

    def build(self):
        return Builder.load_string(KV)

    def submit_job_seeker(self):
        seeker_name = self.root.get_screen('job_seeker').ids.seeker_name.text
        seeker_lastname = self.root.get_screen('job_seeker').ids.seeker_lastname.text
        seeker_email = self.root.get_screen('job_seeker').ids.seeker_email.text
        seeker_phone = self.root.get_screen('job_seeker').ids.seeker_phone.text
        seeker_password = self.root.get_screen('job_seeker').ids.seeker_password.text

        client = MongoClient("mongodb://localhost:27017/")  # Default MongoDB connection
        db = client["JobPortal"]  # Creates "MyDatabase" if it doesn't exist
        collection = db["JobSeeker"] 

        sample_data = {"Name": seeker_name, "Last Name": seeker_lastname,"Email":seeker_email,"Phone Number":seeker_phone,"Password":seeker_password}
        collection.insert_one(sample_data)

    def submit_job_giver(self):
        giver_name = self.root.get_screen('job_giver').ids.giver_name.text
        giver_lastname = self.root.get_screen('job_giver').ids.giver_lastname.text
        giver_email = self.root.get_screen('job_giver').ids.giver_email.text
        giver_phone = self.root.get_screen('job_giver').ids.giver_phone.text
        giver_password = self.root.get_screen('job_giver').ids.giver_password.text

        client = MongoClient("mongodb://localhost:27017/")  # Default MongoDB connection
        db = client["JobPortal"]  # Creates "MyDatabase" if it doesn't exist
        collection = db["JobGiver"] 

        sample_data = {"Name": giver_name, "Last Name": giver_lastname,"Email":giver_email,"Phone Number":giver_phone,"Password":giver_password}
        collection.insert_one(sample_data)

if __name__ == "__main__":
    JobPortalApp().run()

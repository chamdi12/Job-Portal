from kivy.uix.screenmanager import Screen
from kivy.lang import Builder 
from kivy.uix.floatlayout import FloatLayout 


Builder.load_string("""
<HomeScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 1 
        
        # MDTopAppBar:
        #     title: "Home" 
        
        # FloatLayout:
        #     MDLabel:        
        #         text: "Welcome to the Job Portal" 
        #         pos_hint: {"x": 0.2, "y": 0.5}

        MDBoxLayout:
            orientation: "vertical"
            
            MDBoxLayout:
                size_hint_y: 0.5
                # md_bg_color: 0, 0, 0.6, 1   
                MDLabel:
                    text: "Find your Dream Job" 
                    # halign: "center"
                    font_style: "H3"
                    bold: True

         
""")

class HomeScreen(Screen):
    pass

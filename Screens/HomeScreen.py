from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDRaisedButton


import os 

kv_path = os.path.join(os.path.dirname(__file__), "../kv/home_screen.kv")
Builder.load_file(kv_path)  

class HomeScreen(MDScreen):  
    def on_enter(self): 
        job_list = [
    {
        "title": "Software Engineer",
        "salary": 1200000,
        "location": "Bangalore, India",
        "time_of_upload": 2,
        "company_name": "Google India",
        "description": "Design, develop, and maintain software applications. Collaborate with cross-functional teams."
    },
    {
        "title": "Data Scientist",
        "salary": 1500000,
        "location": "Hyderabad, India",
        "time_of_upload": 7,
        "company_name": "Microsoft India",
        "description": "Analyze data to extract insights. Build machine learning models and improve data pipelines."
    },
    {
        "title": "Product Manager",
        "salary": 1800000,
        "location": "Mumbai, India",
        "time_of_upload": 3,
        "company_name": "Amazon India",
        "description": "Lead product development from ideation to launch. Define product roadmaps and collaborate with stakeholders."
    },
    {
        "title": "Backend Developer",
        "salary": 1000000,
        "location": "Pune, India",
        "time_of_upload": 4,
        "company_name": "Infosys",
        "description": "Build and maintain server-side logic. Optimize databases and application performance."
    },
    {
        "title": "Frontend Developer",
        "salary": 950000,
        "location": "Chennai, India",
        "time_of_upload": 5,
        "company_name": "TCS",
        "description": "Create responsive web interfaces. Work with design teams to implement UI/UX."
    },
    {
        "title": "UX Designer",
        "salary": 1100000,
        "location": "Bangalore, India",
        "time_of_upload": 1,
        "company_name": "Flipkart",
        "description": "Design user experiences for web and mobile apps. Create wireframes and prototypes."
    },
    {
        "title": "Mobile App Developer",
        "salary": 1250000,
        "location": "Delhi, India",
        "time_of_upload": 6,
        "company_name": "Paytm",
        "description": "Develop Android and iOS apps. Work with product and design teams for seamless UX."
    },
    {
        "title": "DevOps Engineer",
        "salary": 1400000,
        "location": "Noida, India",
        "time_of_upload": 14,
        "company_name": "Zomato",
        "description": "Manage CI/CD pipelines. Ensure application deployment and server reliability."
    },
    {
        "title": "Business Analyst",
        "salary": 1050000,
        "location": "Gurgaon, India",
        "time_of_upload": 3,
        "company_name": "Ola Cabs",
        "description": "Analyze business processes and gather requirements. Create reports and support decision-making."
    },
    {
        "title": "Technical Support Engineer",
        "salary": 800000,
        "location": "Kolkata, India",
        "time_of_upload": 7,
        "company_name": "Wipro",
        "description": "Provide technical support for software products. Troubleshoot issues and assist clients."
    }
]


        cities_of_india = [
            {"title": "Mumbai", "job": 100},
            {"title": "Delhi", "job": 80},
            {"title": "Bangalore", "job": 50},
            {"title": "Hyderabad", "job": 35},
            {"title": "Chennai", "job": 31},
            {"title": "Kolkata", "job": 27},
            {"title": "Ahmedabad", "job": 24},
            {"title": "Pune", "job": 15},
            {"title": "Jaipur", "job": 12},
            {"title": "Lucknow", "job": 9},
        ]

        self.populate_jobs(job_list)
        self.location_filter(cities_of_india)

        def open_profile():
            print("Hello world")

    def location_filter(self,c_o_I):
        location_box = self.ids.location_box
        location_box.clear_widgets()
        for loc in c_o_I:
            Box = MDBoxLayout(
                orientation = 'horizontal',
                size_hint_y = None,
                height =  dp(30) ,
                padding = [dp(10),0,0,0]
            )
            label = MDLabel(
                text = loc['title'],
                halign = "left",
                size_hint_x = 1
            )
            widget = Widget()

            checkbox = MDCheckbox(
                size_hint_x = 0.3,
                pos_hint =  {"center_y": 0.5}
            )

            Box.add_widget(label)
            Box.add_widget(widget)
            Box.add_widget(checkbox)
            location_box.add_widget(Box)

    def populate_jobs(self, job_list):
        jobs_grid = self.ids.jobs_grid
        jobs_grid.clear_widgets()

        for job in job_list:
            card = MDCard(
                size_hint_y=None,
                height=dp(250),
                size_hint_x=None,
                width=dp(550),
                md_bg_color=(0.95, 0.95, 0.95, 1),
                elevation=3,
                radius=[15],
                padding=dp(15),
            )

            box = MDBoxLayout(
                orientation="vertical",
                spacing=dp(6),
            )

            header = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(30),
            )

            title = MDLabel(
                text=job["title"],
                bold=True,
                font_size="18sp",
                theme_text_color="Primary",
                halign="left",
            )

            time_of_upload = MDLabel(
                text=f"Posted {job['time_of_upload']} days ago",
                font_size="12sp",
                theme_text_color="Hint",
                halign="right",
            )

            header.add_widget(title)
            header.add_widget(time_of_upload)

            company = MDLabel(
                text=f"Company: {job['company_name']}",
                font_size="14sp",
                theme_text_color="Secondary",
            )

            location = MDLabel(
                text=f"Location: {job['location']}",
                font_size="14sp",
                theme_text_color="Secondary",
            )

            salary = MDLabel(
                text=f"Salary: ₹{job['salary']:,} per annum",
                font_size="14sp",
                theme_text_color="Secondary",
            )

            description = MDLabel(
                text=job["description"],
                font_size="13sp",
                theme_text_color="Secondary",
                max_lines=3,
            )

            button = MDRaisedButton(
                text="Apply Now",
                elevation=1,
                md_bg_color=(0, 0, 0.5, 1),
                size_hint=(None, None),
                size=(dp(100), dp(40)),
                pos_hint={"center_x": 0.5},
            )

            box.add_widget(header)
            box.add_widget(company)
            box.add_widget(location)
            box.add_widget(salary)
            box.add_widget(description)
            box.add_widget(button)

            card.add_widget(box)
            jobs_grid.add_widget(card)

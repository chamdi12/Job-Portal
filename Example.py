from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp

KV = '''
ScreenManager:
    MainScreen:
    ApplyScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Job Portal'
        MDDataTable:
            id: job_table
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: (0.9, 0.8)
            on_row_press: app.on_job_selected

<ApplyScreen>:
    name: 'apply'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Apply for Job'
            left_action_items: [['arrow-left', lambda x: app.go_back()]]
        MDLabel:
            id: job_title
            text: 'Job Title'
            halign: 'center'
        MDRaisedButton:
            text: 'Apply Now'
            pos_hint: {'center_x': 0.5}
            on_release: app.apply_job
'''

class MainScreen(Screen):
    pass

class ApplyScreen(Screen):
    pass

class JobPortalApp(MDApp):
    def build(self):
        self.jobs = [['Software Engineer', 'Google'], ['Data Scientist', 'Microsoft'], ['UI/UX Designer', 'Apple']]
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(ApplyScreen(name='apply'))
        return Builder.load_string(KV)

    def on_start(self):
        self.populate_jobs()
    
    def populate_jobs(self):
        table = self.root.ids.job_table
        table.column_data = [('Job Title', dp(40)), ('Company', dp(40))]
        table.row_data = self.jobs

    def on_job_selected(self, table, row):
        job_title = row.text
        self.root.ids.job_title.text = f'Applying for: {job_title}'
        self.sm.current = 'apply'
    
    def apply_job(self):
        dialog = MDDialog(title='Application Submitted', text='Your job application has been submitted successfully!', buttons=[MDRaisedButton(text='OK', on_release=lambda x: dialog.dismiss())])
        dialog.open()
    
    def go_back(self):
        self.sm.current = 'main'

if __name__ == '__main__':
    JobPortalApp().run()

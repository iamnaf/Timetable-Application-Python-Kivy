from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_string("""

<HomeScreen>:
    GridLayout:
        pos: self.pos
        rows: 8
        padding: 70
        spaccing: 10, 10
        Label:
            text: "ELECT CLASS '18 2015/2016 RAIN SEMESTER TIMETABLE" 
        Button:
            text: "WELCOME"
            size_hint: None, None
            size: 50, 40
            on_release: root.welcome()
                
        Button:
            text: "MONDAY"
            on_release:root.manager.current='monday'
        Button:
            text: "TUESDAY"
            on_release: root.manager.current='tuesday'
        Button:
            text: "WEDNESDAY"
            on_release: root.manager.current='wednesday'
        Button:
            text: "THURSDAY"
            on_release: root.manager.current='thursday'
        Button:
            text: "FRIDAY"
            on_release: root.manager.current='friday'
        Button:
            text: "Quit"
            on_release: quit()
            
<MainScreen>:
    BoxLayout:
        Widget:
            Label:
                text: "World"

<Monday>:
    GridLayout:
        cols:4
        rows:5
        Label:
            text: "Course"
        Label:
            text: "Time"
        Label:
            text: "Venue"
        Label:
            text: "Lecturer"
        Label:
            text: "ELE 324"
        Label:
            text: "10:00-11:00"
        Label:
            text: "9F1"
        Label:
            text: "Engr. J. Akanni"
        Label:
            text: "ELE 316"
        Label:
            text: "12:00-2:00"
        Label:
            text: "ELH"
        Label:
            text: "Prof. Y.A. Adediran"
        Label:
            text: "Practical"
        Label:
            text: "2:00PM"
        Label:
            text: "LAB"
        Label:
            text: "Engr. Ariyo"
        Button:
            text: "Main Menu"
            on_release: root.manager.current='home'

<Tuesday>:
    GridLayout:
        cols:4
        rows:5
        Label:
            text: "Course"
        Label:
            text: "Time"
        Label:
            text: "Venue"
        Label:
            text: "Lecturer"
        Label:
            text: "ABE 376"
        Label:
            text: "9:00-10:00"
        Label:
            text: "LT III"
        Label:
            text: "Unknown"
        Label:
            text: "ELE 312"
        Label:
            text: "10:00-12:00"
        Label:
            text: "LT III"
        Label:
            text: "Dr. Mrs. Bakinde"
        Label:
            text: "ABE 306"
        Label:
            text: "2:00"
        Label:
            text: "ELT"
        Label:
            text:"Unknown"
        Button:
            text: "Main Menu"
            on_release: root.manager.current='home'
            
<Wednesday>:
    GridLayout:
        cols:4
        rows:5
        Label:
            text: "Course"
        Label:
            text: "Time"
        Label:
            text: "Venue"
        Label:
            text: "Lecturer"
        Label:
            text: "ELE 342"
        Label:
            text: "8:00-10:00"
        Label:
            text: "LT IV"
        Label:
            text: "Dr. S.A.Y. Amuda"
        Label:
            text: "ELE 324"
        Label:
            text: "11:00-1:00"
        Label:
            text: "10G2"
        Label:
            text: "Engr. J. Akanni"
        Label:
            text: "MEE 362"
        Label:
            text: "1:00-2:00"
        Label: 
            text: "LT III"
        Label: 
            text: "Engr. O.T. Popoola"
        
        Button:
            text: "Main Menu"
            on_release: root.manager.current='home'

<Thursday>:
    GridLayout:
        cols:4
        rows:5
        Label:
            text: "Course"
        Label:
            text: "Time"
        Label:
            text: "Venue"
        Label:
            text: "Lecturer"
        Label:
            text: "ELE 344"
        Label:
            text: "8:00-10:00"
        Label:
            text: "LT IV"
        Label:
            text: "Dr. J.F. Opadiji"
        Label:
            text: "MEE 362"
        Label:
            text: "12:00-2:00"
        Label:
            text: "LT III"
        Label:
            text: "Engr. O.T. Popoola"
        Label:
            text: "Practical"
        Label:
            text: "2:00 PM"
        Label:
            text: "LAB"
        Label:
            text: "Engr. Ariyo"
        Button:
            text: "Main Menu"
            on_release: root.manager.current='home'
<Friday>:
    GridLayout:
        cols:4
        rows:4
        Label:
            text: "Course"
        Label:
            text: "Time"
        Label:
            text: "Venue"
        Label:
            text: "Lecturer"
        Label:
            text: "ELE 316"
        Label:
            text: "10:00-11:00"
        Label:
            text: "Graphics Room"
        Label:
            text: "Prof. Y.A. Adediran"
        Label:
            text: "Practical"
        Label:
            text: "2:00 PM"
        Label:
            text: "LAB"
        Label:
            text: "Engr. Ariyo"
        Button:
            text: "Main Menu"
            on_release: root.manager.current='home'
""")

class HomeScreen(Screen):
    def welcome(self):
        popup = Popup(title=("Class '18 2015/2016 Rain Semester Timetable"), title_align=('centre'), content=Label(text=("*ELH - Engineering Lecture Hall\n*ELT - Engineering Lecture Theatre\n*LT III - Lecture Theatre III\n*LT IV - Lecture Theatre IV")), size_hint=(.8,.8))
        popup.open()

class MainScreen(Screen):
    pass

class Monday(Screen):
    pass

class Tuesday(Screen):
    pass

class Wednesday(Screen):
    pass

class Thursday(Screen):
    pass

class Friday(Screen):
    pass



sm=ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(Monday(name='monday'))
sm.add_widget(Tuesday(name='tuesday'))
sm.add_widget(Wednesday(name='wednesday'))
sm.add_widget(Thursday(name='thursday'))
sm.add_widget(Friday(name='friday'))

class TimeTableApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    TimeTableApp().run()Timetable-Application-Python-Kivy

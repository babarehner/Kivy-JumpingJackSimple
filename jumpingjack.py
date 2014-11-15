'''
Created on Nov 6, 2014

@author: mike
'''
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty

from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string('''
<Jump>:
    Image:
        source: root.src
''')

class Jump(BoxLayout):
    src = StringProperty('')
    next = 1 #which jump png file will be shown next
    up = True #Is the jumper going up or coming down
    
    def __init__(self, **kwargs):
        super(Jump, self).__init__(**kwargs)
        Clock.schedule_interval(self.updateImage, 1/2.0)
      
    def updateImage(self, *args): 
        
        if self.next == 1:
            self.src = 'JumpingJack01.png'
            self.next = 2
        elif self.next == 2:
            self.src = 'JumpingJack02.png'
            if self.up:
                self.next = 3
            else:
                self.next = 1
            self.up = not self.up
        else:
            self.src = 'JumpingJack03.png'
            self.next = 2
        
        print (self.next, 'xxxx', self.up, '---', self.src)  #debugging print statement
#####################################################
runTouchApp(Jump())
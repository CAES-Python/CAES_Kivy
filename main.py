from kivy.app import App

from kivy.clock import Clock
from kivy.clock import Clock as clock

from kivy.config import Config
from kivy.gesture import Gesture,GestureDatabase

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse)
from kivy.graphics.context_instructions import Color

from kivy.lang import Builder

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.togglebutton import ToggleButton

from kivy.garden.knob import Knob
from kivy.garden.gauge import Gauge
from kivy.garden.gauges import Gauges
from kivy.garden.light_indicator import  Light_indicator

from kivy.properties import ListProperty, ObjectProperty



import collections 
import math
import os
import random
import sys
from math import *


import gesture_box as gesture

# This is where Kivy captures gestures.
class Runner(gesture.GestureBox):
	pass


#define the Screen Manager
class NuclearScreenManager(ScreenManager):
	pass
	
#define the screens
class NCPScreen(Screen):
	pass
class MenuScreen(Screen):
	def stop(self):
		sys.exit()

class NSRScreen(Screen):
	pass
class ToggleScreen(Screen):
	pass

class MyPanel(Screen):
	def __init__(self, **kwargs):
			
		super(MyPanel, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)
		Clock.schedule_interval(self.warning,0.1)
		
#experiment with getting ids from different screens.
	def _finish_init(self,dt):
		self.NCPvalue1=self.manager.get_screen('ncp').ids.knob1.value 
		self.NCPvalue2=self.manager.get_screen('ncp').ids.knob2.value
		self.NCPvalue3=self.manager.get_screen('ncp').ids.knob3.value
		self.NCPvalue4=self.manager.get_screen('ncp').ids.knob4.value 
	def warning(self,dt):
		
		
		self.knob = self.ids.knob
		self.knob2 = self.ids.knob2
		self.warning1 = self.ids.warning1
		self.warning2 = self.ids.warning2
		self.knob1value = self.knob.value
		self.knob2value = self.knob2.value
		self.value1 = self.knob1value
		self.value2 = self.knob2value
		self.NCPvalue1=self.manager.get_screen('ncp').ids.knob1.value
		self.NCPvalue2=self.manager.get_screen('ncp').ids.knob2.value
		self.NCPvalue3=self.manager.get_screen('ncp').ids.knob3.value
		self.NCPvalue4=self.manager.get_screen('ncp').ids.knob4.value 


		if (self.NCPvalue1 <  75 or self.NCPvalue2 <  50 or self.NCPvalue3 < 60 or self.NCPvalue4 < 90 or self.value2 <  50) and self.value1 >  50:
			
			if self.value1 < 75:
				self.warning1.turn_off_l1()
				self.warning1.turn_off_l3()
				self.warning1.turn_on_l2()
			elif self.value1 > 75 :
				self.warning1.turn_off_l1()
				self.warning1.turn_off_l2()
				self.warning1.turn_on_off_l3()

		elif (self.NCPvalue1 >  75 or self.NCPvalue2 >  50 or self.NCPvalue3 > 60 or self.NCPvalue4 > 90 or self.value2 >  50) and self.value1< 75:
			self.warning1.turn_off_l1()
			self.warning1.turn_off_l2()
			self.warning1.turn_on_off_all()

		elif (self.NCPvalue1 >  75 and self.NCPvalue2 >  50 and self.NCPvalue3 > 60 and self.NCPvalue4 > 90 and self.value2 >  75) and self.value1> 75:
			self.warning2.turn_on_all()
			self.warning1.turn_on_all()

		else :
			
			self.warning1.turn_off_all()
			self.warning1.turn_on_l1()			

		if (self.NCPvalue1 <  75 or self.NCPvalue2 <  50 or self.NCPvalue3 < 60 or self.NCPvalue4 < 90 or self.value1 <  50) and self.value2 >  50:
			
			if self.value2 < 75:
				self.warning2.turn_off_l1()
				self.warning2.turn_off_l3()
				self.warning2.turn_on_l2()
			elif self.value2 > 75:
				self.warning2.turn_off_l1()
				self.warning2.turn_off_l2()
				self.warning2.turn_on_off_l3()
		elif  (self.NCPvalue1 >  75 or self.NCPvalue2 >  75 or self.NCPvalue3 > 80 or self.NCPvalue4 > 90 or self.value1 >  75) and self.value2<50:
			self.warning2.turn_off_l1()
			self.warning2.turn_off_l2()
			self.warning2.turn_on_off_all()
		elif  self.NCPvalue1 >  75 and self.NCPvalue2 > 75  and self.NCPvalue3 > 80 and self.NCPvalue4 > 90 and self.value1 >  75 and self.value2>75:
			self.warning1.turn_on_all()
			self.warning2.turn_on_all()


		else :
			
			self.warning2.turn_off_all()
			self.warning2.turn_on_l1()
			



class NuclearControlPanel(Screen):

	def __init__(self, **kwargs):
				
		super(NuclearControlPanel, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)
		Clock.schedule_interval(self.warning,0.1)


	def _finish_init(self,dt):
		self.gauge1 = self.ids.gauge1
		self.knob1 = self.ids.knob1
		self.knob2 = self.ids.knob2
		self.knob3 = self.ids.knob3
		self.knob4 = self.ids.knob4
		self.knob1value = self.knob1.value
		self.knob2value = self.knob2.value
		self.knob3value = self.knob3.value
		self.knob4value = self.knob4.value
		self.warning1 = self.ids.warning1
		self.warning2 = self.ids.warning2
		self.warning3 = self.ids.warning3
		self.warning4 = self.ids.warning4
		#self.P1knob1.value=self.manager.get_screen('panel1').ids.knob.value 
		#self.P1knob2.value=self.manager.get_screen('panel1').ids.knob2.value 

	def stop(self):
		sys.exit()
	def warning(self,dt):
		
		
		self.knob1 = self.ids.knob1
		self.knob2 = self.ids.knob2
		self.knob3 = self.ids.knob3
		self.knob4 = self.ids.knob4
		self.knob1value = self.knob1.value
		self.knob2value = self.knob2.value
		self.knob3value = self.knob3.value
		self.knob4value = self.knob4.value
		self.value1 = self.knob1value
		self.value2 = self.knob2value
		self.value3 = self.knob3value
		self.value4 = self.knob4value
		self.P1knob1value=self.manager.get_screen('panel1').ids.knob.value 
		self.P1knob2value=self.manager.get_screen('panel1').ids.knob2.value 

		if self.value1 >  50 and (self.value2 < 75 or self.value3 < 80 or self.value4 < 90 or self.P1knob1value < 75 or self.P1knob2value < 75 ):
			if self.value1 < 75:
				self.warning1.turn_off_l1()
				self.warning1.turn_off_l3()
				self.warning1.turn_on_l2()
			elif self.value1 > 75:
				self.warning1.turn_off_l1()
				self.warning1.turn_off_l2()
				self.warning1.turn_on_off_l3()
		elif self.value1 <  75 and (self.value2 > 75 or self.value3 > 80 or self.value4 > 90 or self.P1knob1value > 75 or self.P1knob2value > 75):
			self.warning1.turn_off_all()
			self.warning1.turn_on_off_all()
		elif self.value1 >  75 and (self.value2 > 75 and self.value3 > 80 and self.value4 > 90 and self.P1knob1value > 75 and self.P1knob2value > 75):
			
			self.warning4.turn_on_off_all()
			self.warning3.turn_on_off_all()
			self.warning2.turn_on_off_all()
			self.warning1.turn_on_off_all()
		else:
			self.warning1.turn_off_all()
			self.warning1.turn_on_l1()


		if self.value2 >  50 and (self.value1 < 75 or self.value3 < 80 or self.value4 < 90 or self.P1knob1value < 75 or self.P1knob2value < 75):
			if self.value2 < 80:
				self.warning2.turn_off_l1()
				self.warning2.turn_off_l3()
				self.warning2.turn_on_l2()
			elif self.value2 > 75:
				self.warning2.turn_off_l1()
				self.warning2.turn_off_l2()
				self.warning2.turn_on_off_l3()

		elif self.value2 >  75 and (self.value1 > 75 and self.value3 > 80 and self.value4 > 90 and self.P1knob1value > 75 and self.P1knob2value > 75):
			
			self.warning4.turn_on_off_all()
			self.warning3.turn_on_off_all()
			self.warning2.turn_on_off_all()
			self.warning1.turn_on_off_all()

		elif self.value2 <  50 and (self.value1 > 75 or self.value3 > 80 or self.value4 > 90 or self.P1knob1value > 75 or self.P1knob2value > 75):
			self.warning2.turn_off_all()
			self.warning2.turn_on_off_all()
		else:
			self.warning2.turn_off_all()
			self.warning2.turn_on_l1()




		if self.value3 >  60 and (self.value1 < 75 or self.value2 < 75 or self.value4 < 90 or self.P1knob1value < 75 or self.P1knob2value < 75):
			if self.value3 < 80:
				self.warning3.turn_off_l1()
				self.warning3.turn_off_l3()
				self.warning3.turn_on_l2()
			elif self.value3 > 80 :
				self.warning3.turn_off_l1()
				self.warning3.turn_off_l2()
				self.warning3.turn_on_off_l3()
		elif self.value3 >  80 and (self.value1 > 75 and self.value4 > 90 and self.value2 > 75 and self.P1knob1value > 75 and self.P1knob2value > 75):
			
			self.warning4.turn_on_off_all()
			self.warning3.turn_on_off_all()
			self.warning2.turn_on_off_all()
			self.warning1.turn_on_off_all()

		elif self.value3 <  60 and (self.value1 > 75 or self.value2 > 75 or self.value4 > 90 or self.P1knob1value > 75 or self.P1knob2value > 75):
			self.warning3.turn_off_all()
			self.warning3.turn_on_off_all()
		else:
			self.warning3.turn_off_all()
			self.warning3.turn_on_l1()



		if self.value4 >  80 and (self.value1 < 75 or self.value3 < 80 or self.value2 < 75 or self.P1knob1value < 75 or self.P1knob2value < 75):
			if self.value4 < 90:
				self.warning4.turn_off_l1()
				self.warning4.turn_off_l3()
				self.warning4.turn_on_l2()
			elif self.value4 > 90:
				self.warning4.turn_off_l1()
				self.warning4.turn_off_l2()
				self.warning4.turn_on_off_l3()
		elif self.value4 >  90 and (self.value1 > 75 and self.value3 > 80 and self.value2 > 75 and self.P1knob1value > 75 and self.P1knob2value > 75):
			
			self.warning4.turn_on_all()
			self.warning3.turn_on_all()
			self.warning2.turn_on_all()
			self.warning1.turn_on_all()

		elif self.value4 <  80 and (self.value1 > 75 or self.value3 > 80 or self.value2 > 75 or self.P1knob1value > 75 or self.P1knob2value > 75):
			self.warning4.turn_off_all()
			self.warning4.turn_on_off_all()
		else:
			self.warning4.turn_off_all()
			self.warning4.turn_on_l1()


#Building the app. The program will look for the file "nuclear.kv" because the app is called Nuclear			
class NuclearApp(App):
	def build(self):
		Config.set('graphics','fullscreen', True)
		return NuclearScreenManager()
# Run the program
if __name__ == "__main__":
	NuclearApp().run()


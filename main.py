from kivy.app import App

from kivy.lang import Builder
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout

from kivy.garden.knob import Knob
from kivy.garden.graph import Graph, MeshLinePlot, SmoothLinePlot, Plot
from kivy.garden.gauge import Gauge

from kivy.clock import Clock
from kivy.clock import Clock as clock
from kivy.properties import ListProperty, ObjectProperty
from kivy.config import Config

from kivy.gesture import Gesture,GestureDatabase

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color
import collections 

import random
import math
import os
import sys
from math import *


import gesture_box as gesture


class Runner(gesture.GestureBox):
	pass

class NCPScreen(Screen):
	pass

class NuclearScreenManager(ScreenManager):
	pass

class MenuScreen(Screen):
	pass
class KnobScreen(Screen):

	def __init__(self, **kwargs):
		super(KnobScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
		


	def _finish_init(self,dt):
		self.knob_value = self.ids.knob1.value


		
	def pause():
		time.sleep(5)
	def stop(self):
		sys.exit()
	def start(self):
		pass


class NuclearControlPanel(Screen):

	def __init__(self, **kwargs):
				
		super(NuclearControlPanel, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
		Clock.schedule_interval(self.warning,0.1)


	def _finish_init(self,dt):
		self.gauge1 = self.ids.gauge1
		self.knob1 = self.ids.knob1
		self.knob1value = self.knob1.value
		self.warninglabel = self.ids.warning

	def stop(self):
		sys.exit()
	def warning(self,dt):
		
		
		self.knob1 = self.ids.knob1
		self.knob1value = self.knob1.value
		self.value = self.knob1value
		if self.value <75:
			self.warninglabel.color = [0,1,0,1]
		else:
			self.warninglabel.color = [1,0,0,1]
			
class NuclearApp(App):
	def build(self):
		Config.set('graphics','fullscreen', 'auto')
		return NuclearScreenManager()

if __name__ == "__main__":
	NuclearApp().run()


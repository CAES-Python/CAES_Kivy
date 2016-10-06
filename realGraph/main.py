from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider

from kivy.garden.knob import Knob
from kivy.garden.graph import Graph, MeshLinePlot, SmoothLinePlot, Plot

from kivy.clock import Clock as clock

from kivy.properties import ListProperty, ObjectProperty

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color

import random
from math import *
import math
import time
import collections

from scipy import *



class NuclearControlPanel(BoxLayout):
	
	def __init__(self, **kwargs):
		super(NuclearControlPanel, self).__init__(**kwargs)
		knob_value = self.ids.knob1.value
		graph =MeshLinePlot(color=[0, 0, 1, 1]) 
		self.input_plot = MeshLinePlot(color=[0, 1, 0, 1])

		self.xvals = collections.deque(maxlen=100)
		self.yvals = [1,2,3,6,3,7,9,3,11,22,16,23]#[knob_value]
				

			
		
		self.ids.my_plot.add_plot(self.input_plot)
		
		

		
		for i in self.yvals:

			wave1 = self.yvals
		        
		        clock.schedule_interval(self.update_points, 1 / 100)
		        clock.schedule_interval(self.update_graph, 1 / 100)

		        clock.schedule_interval(lambda *args: self.add_points(wave1), 0.2)
		        #self.ids.my_plot.add_plot(self.input_plot)


	def update_points(self, *args):
		for x in range(len(self.xvals)):
			self.yvals.append(self.ids.knob1.value)
			x+=1	
		self.input_plot.points = zip(range(len(self.xvals)), self.yvals)
		

	def update_graph(self, *args):
		if len(self.xvals) >3:
			
			self.ids.my_plot.ymin= math.ceil(min(self.yvals))
			self.ids.my_plot.ymax= math.ceil(max(self.yvals))
			self.ids.my_plot.add_plot(self.input_plot)
	
	def change_knob(self,*args):
		self.yvals.append(self.ids.knob1.value)


	def add_points(self,active):
		self.xvals.append(active)
		for x in range(len(self.xvals)):
			self.change_knob()
			
	def pause():
		time.sleep(5)
	def stop(self):
		clock.idle()
	def start(self):
		pass
	def on_touch_move(self,touch):
		self.yvals.append(self.ids.knob1.value)
class NuclearApp(App):
	def build(self):
		return NuclearControlPanel()

if __name__ == "__main__":
	NuclearApp().run()

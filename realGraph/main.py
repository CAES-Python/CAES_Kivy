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

from kivy.clock import Clock

from kivy.properties import ListProperty, ObjectProperty

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color

import random
from math import *
import math
import collections



class NuclearControlPanel(BoxLayout):
	
	def __init__(self, **kwargs):
		super(NuclearControlPanel, self).__init__(**kwargs)
		knob_value = self.ids.knob1.value
		graph =MeshLinePlot(color=[0, 0, 1, 1]) 
		self.input_plot = MeshLinePlot(color=[0, 1, 0, 1])
		self.knob_plotpoints =(0,knob_value)
		self.knob_plotpoints = zip(range(len(self.knob_plotpoints)), self.ids.knob1.value)
		
		self.ids.my_plot.add_plot(self.input_plot)
		
		for i in xrange(10):

			self.wave1 = self.ids.knob1.value
			self.wave2 = self.ids.knob1.value
			Clock.schedule_interval(self.update_points, 1 / 60)
			Clock.schedule_interval(self.update_graph, 1 / 60)

			Clock.schedule_interval(lambda *args: self.add_points(self.wave1, self.wave2), 0.2)
			self.ids.my_plot.add_plot(graph)


	def update_points(self, *args):
		self.input_plot.points = zip(range(len(self.knob_plotpoints)), self.knob_plotpoints)
		

	def update_graph(self, *args):
		if len(self.knob_plotpoints) >3:
			
			self.ids.my_plot.ymin= 0
			self.ids.my_plot.ymax= 2 #math.ceil(max(self.knob_plotpoints))

	def add_points(self,active,predictive):
		self.knob_plotpoints.append(active)
	
	def pause():
		time.sleep(5)
	def stop():
		Clock.cancel()

class NuclearApp(App):
	def build(self):
		return NuclearControlPanel()

if __name__ == "__main__":
	NuclearApp().run()

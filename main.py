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
class NuclearControlPanel(BoxLayout):

	def __init__(self, **kwargs):
		super(NuclearControlPanel, self).__init__(**kwargs)
		self.plot = MeshLinePlot(color = [0,1,0,1])
		graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
		x_ticks_major=25, y_ticks_major=1,
		y_grid_label=True, x_grid_label=True, padding=5,
		x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=0, ymax=1)
		plot = MeshLinePlot(color=[0, 1, 0, 1])
		plot.points = [(x, sin(x)) for x in range(0, 101)]
		plot2 = MeshLinePlot(color = [1,0,0,1])
		plot2.points = [(x, 0.75) for x in range(0, 101)]
		plot3 = MeshLinePlot(color = [1,0,0,1])
		plot3.points = [(x, -0.25) for x in range(0, 101)]
		self.ids.my_plot.add_plot(plot)
    		self.ids.my_plot.add_plot(plot2)
		self.ids.my_plot.add_plot(plot3)

# Experiment with real time graph
		
		def update_xaxis(self,*args):
		        global graph
			global cnt
			graph.xmin = cnt - 50
			graph.xmax = cnt

		def update_points(self, *args):
			global i
			global MYLIST
			global cnt
 
#self.plot.points = [(i,i)]
			self.plot.points = [z for z in MYLIST]
			Clock.schedule_interval(self.update_points, 1/60.)
			Clock.schedule_interval(self.update_xaxis, 1/60.)
			plot4 = MeshLinePlot(color = [1,1,0,1])
			plot4.points = [(x, sin(2*x)) for x in MYLIST]
			self.ids.my_plot.add_plot(plot4)
class NuclearApp(App):
	def build(self):
		return NuclearControlPanel()

if __name__ == "__main__":
	NuclearApp().run()

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

from kivy.garden.knob import Knob
from kivy.garden.graph import Graph, MeshLinePlot, SmoothLinePlot, Plot

from kivy.clock import Clock
from kivy.clock import Clock as clock
from kivy.properties import ListProperty, ObjectProperty

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
		graph =MeshLinePlot(color=[0, 0, 1, 1]) 
		self.input_plot = MeshLinePlot(color=[0, 1, 0, 1])

		self.xvals = collections.deque(maxlen=100)
		self.yvals = [1,2,3,6,3,7,9,3,11,22,16,23]#[knob_value]
				

		for i in self.yvals:

			wave1 = self.yvals
			
			clock.schedule_interval(self.update_points, 1 / 100)
			clock.schedule_interval(self.update_graph, 1 / 100)

			clock.schedule_interval(lambda *args: self.add_points(wave1), 0.2)
	        #self.ids.my_plot.add_plot(self.input_plot)
		
		self.ids.my_plot.add_plot(self.input_plot)
		
		

		
		
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
		sys.exit()
	def start(self):
		pass
	def on_touch_move(self,touch):
		self.yvals.append(self.ids.knob1.value)

class NuclearControlPanel(BoxLayout):

	def __init__(self, **kwargs):
				
		super(NuclearControlPanel, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
		Clock.schedule_once(self._my_plots)

#
# Experiment with real time graph
		
#	def update_xaxis(self,*args):
#	        global graph
#		global cnt
#		graph.xmin = cnt - 50
#		graph.xmax = cnt

#	def update_points(self, *args):
#		global i
#		global MYLIST
#		global cnt

#	def start(self):
#		self.ids.graph.add_plot(self.plot)
#		Clock.schedule_interval(self.get_value, 0.001)

#	def stop(self):
#		Clock.unschedule(self.get_value)

#	def get_value(self, dt):
#		self.plot.points = [(i, j/5) for i, j in enumerate(levels)]
#self.plot.points = [(i,i)]
#		self.plot.points = [z for z in MYLIST]
#		Clock.schedule_interval(self.update_points, 1/60.)
#		Clock.schedule_interval(self.update_xaxis, 1/60.)
#		plot4 = MeshLinePlot(color = [1,1,0,1])
#		plot4.points = [(x, sin(2*x)) for x in MYLIST]
#		self.ids.my_plot.add_plot(plot4)
	def _finish_init(self,dt):
		self.my_plot =self.ids.my_plot
		self.my_real_plot =self.ids.my_real_plot
		self.plot = MeshLinePlot(color=[0, 1, 0, 1])
		self.plot.points = [(x, sin(x)) for x in range(0, 101)]
		plot2 = MeshLinePlot(color = [1,0,0,1])
		plot2.points = [(x, 0.75) for x in range(0, 101)]
		plot3 = MeshLinePlot(color = [1,0,0,1])
		plot3.points = [(x, -0.25) for x in range(0, 101)]
		self.plot5 = MeshLinePlot(color = [0,0,1,1])
		self.plot5.points = [(x,x**2) for x in range(0,50)]
		
		
	def _my_plots(self, dt):
		self.ids.my_plot.add_plot(self.plot)
#  		self.ids.my_plot.add_plot(plot2)
#		self.ids.my_plot.add_plot(plot3)
		self.ids.my_real_plot.add_plot(self.plot5)
class NuclearApp(App):
	def build(self):
		return NuclearScreenManager()

if __name__ == "__main__":
	NuclearApp().run()

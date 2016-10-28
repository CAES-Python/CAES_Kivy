#!/usr/bin/env python


'''
Light indicator
=====

The :class:`Light_indicator` widget is a widget for displaying Light_indicator. 

.. note::

Source svg file provided for customing.

'''
# This is the dictionary which maps the user color choice to the rgba list property.

__all__ = ('Light_indicator',)

__title__ = 'garden.light_indicator'
__version__ = '0.1'
__author__ = 'Marcus Holden'

import kivy
kivy.require('1.9.1')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.lang  import  Builder

from kivy.properties    import   StringProperty, BooleanProperty, ReferenceListProperty, ListProperty, StringProperty, BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Ellipse, Rectangle
from kivy.graphics.context_instructions import Color
from functools import partial
import os,inspect,sys

class DummyClass: 
	pass

class Light(Widget):
	Builder.load_file('light.kv')
	light_color = ListProperty([1,0,0,1])
class Light_indicator(Widget):
	'''
	Light_indicator class

	'''
	dummy = DummyClass
	mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
	file_setting = StringProperty(mypath + os.sep + "setting.png")
	size_setting = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
	color_dictionary = {'red':[1,0,0,1], 'green':[0,1,0,1], 'blue':[0,0,1,1], 'yellow':[0,0.5,0.5,1], 'off':[0.5,0.5,0.5,1]}
      
	bol = BooleanProperty(False) # The boolean that turns on and off the light.
	color = StringProperty("")# name of color to refrence the dictionary.
	
	off_color = color_dictionary['off']# the off color of the light.

	

	def __init__(self, **kwargs):
		super(Light_indicator, self).__init__(**kwargs)
		self._setting = Scatter(
			size=(self.size_setting, self.size_setting),
			do_rotate=False, 
			do_scale=True,
			do_translation=False
			)
		self._light = Light(light_color = self.get_color())
		self._light.pos = (100,self._setting.center_y)
		_img_setting = Image(source=self.file_setting, size=(self.size_setting, 
			self.size_setting))

		self._setting.add_widget(_img_setting)
		self.add_widget(self._setting)
		self.add_widget(self._light)
		self.bind(pos=self._update)
		self.bind(size=self._update)
		Clock.schedule_interval(self.my_schedule, 0.1)
		

	def _update(self, *args):
		
		self._setting.pos = self.pos
		self._setting.size = self.size
		self._light.pos = self._setting.center#(100,self._setting.center_y)
		self._light.light_color = self.get_color()
#self.get_color()
		
	def get_color(self):
		color_rgba=self.off_color
		if self.bol == True:
			try:
				color_rgba = self.color_dictionary[self.color]

			except:
				print 'ERROR: Your color doesn\'t exist in the dictionary. Add it to the __init__.py file to use that color.  '
				sys.exit()
		else:
			color_rgba = self.off_color
			
		
		
		return color_rgba


	def turn_on_off(self):
		if self.bol == False :
			self.bol = True
			self.get_color()
		else:
			self.bol = False
			self.get_color() 
	def my_schedule(self,dt):
		self._light.light_color = self.get_color()	


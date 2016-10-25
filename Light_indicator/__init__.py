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

from kivy.properties    import   StringProperty, BooleanProperty, ReferenceListProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Ellipse, Rectangle
Builder.load_string('''
#
#    Light_indicator
#    ====
#     To create a basic Light_indicator (in a kv file):
#
#	Light_indicator:
#		bol: change() # some function to change from false to true.
#       img_source:     "setting.png"    # Light_indicator texture
#
#     
#
<Light_indicator>
	size_hint: None, None

	canvas.before:

		Rectangle:
			pos: self.pos
			size: self.size
			source: self.img_source
			

		canvas:
			PopMatrix

''')


class Light_indicator(Widget):
	'''
	Light_indicator class

	'''
	color_dictionary = {'red':[1,0,0,1], 'green':[0,1,0,1],'blue':[0,1,0,1], 'yellow':[0,0.5,0.5,1], 'off':[0.5,0.5,0.5,1]}
      
	bol = BooleanProperty(False) # The boolean that turns on and off the light.
	color = StringProperty("")# name of color to refence the dictionary.
	color_rgba = ListProperty([])# Color of the light when turned on.
	off_color = color_dictionary['off']# the off color of the light.
    
	img_source = StringProperty("setting.png") # This option is for the background img of the light.

	def __init__(self, **kwargs):
		super(Light_indicator, self).__init__(**kwargs)
		if self.bol == True:
			try:
				color_rgba = color_dictionary[color]
			except:
				print 'Your color doesn\'t exist in the dictionary. Add it to the __init__.py file to use that color.  '
			else:
				color_rgba = self.off_color
        



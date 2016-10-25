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

from kivy.properties    import   StringProperty, BooleanProperty, ReferenceListProperty,\ 
                                 ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label





class Light_indicator(Widget):
    '''
    Light_indicator class

    '''
    color_dictionary = {'red':[1,0,0,1], 'green':[0,1,0,1],'blue':[0,1,0,1], 'yellow':[0,0.5,0.5,1], 'off':[0.5,0.5,0.5,1]}   
    bol = BooleanProperty(False)
    color = StringProperty("")
    color_rgba = ListProperty([])
    off_color = color_ditionary.off


    def __init__(self, **kwargs):
        super(Light_indicator, self).__init__(**kwargs)
        if bol == True:
		try:
			color_rgba = color_dictionary.color
		except:
			print 'Your color doesn\'t exist in the dictionary. Add it to the __init__.py file to use that color.  '
	else:
		color_rgba = off_color
        
class Light_indicatorApp(App):
    
    return box        
      
if __name__ == '__main__':
    Light_indicatorApp().run()

"""
    Gauge
    ====

    The :class:`Gauge` widget creates a component that looks like a
    control Gauge or Dial 
    To configure a Gauge a max/min, slope and step values should be provided.
    Additionally, gauge_img_source could be set to load
    a texture that visually represents the Gauge.

"""
__all__     = ('NuclearGauge',)
__version__ = '0.1'

import kivy
kivy.require('1.6.0')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
                                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                                ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import os,inspect
Builder.load_string('''
#
#    Gauge
#    ====
#     To create a basic Gauge (in a kv file):
#
#     Gauge:
#       size:               100, 100
#       min:                0
#       max:                100
#       step:               1
#       slope:              1
#       value:              0                       # Default position of Gauge.
#       gauge_img_source:     "img/Gauge_metal.png"    # Gauge texture
#       show_marker:        False                   # Do not show surrounding marker
#
#     To create a Gauge with a surrounding marker:
#
#     Gauge:
#       size:               100, 100
#       min:                0
#       max:                100
#       step:               1
#       slope:              1
#       value:              0                       # Default position of Gauge.
#       gauge_img_source:     "img/Gauge_metal.png"    # Gauge texture
#       show_marker:        True                    # Show surrounding marker
#       marker_img:         "img/bline.png"         # Marker texture image
#       Gauge_size:          0.9                     # Scales Gauge size to leave space for marker
#       markeroff_color:    0, 0, 0, 0

#: 
<Gauge>
    size_hint: None, None

    canvas.before:


      
        Ellipse:
            pos: self.pos[0] + (self.size[0] * (1 - self.Gaugeimg_size))/2, self.pos[1] + (self.size[1] * (1 - self.Gaugeimg_size)) / 2
            size: self.size * (self.Gaugeimg_size), self.size * (self.Gaugeimg_size) #self.size[0] * (self.Gaugeimg_size), self.size[1] * (self.Gaugeimg_size)
	    do_scale: True
	    color:
		rgba: [1,0,0,.5]

        PushMatrix
        Rotate:
            angle: 360 - self._angle
            origin: self.center
        Rectangle:
            pos: self.pos[0] + (self.size[0] * (1 - self.Gaugeimg_size)) /2, self.pos[1] + (self.size[1] * (1 - self.Gaugeimg_size)) / 2
            size: self.size[0] * (self.Gaugeimg_size), self.size[1] * (self.Gaugeimg_size) # self.size[0] * (self.Gaugeimg_size), self.size[1] * (self.Gaugeimg_size)
            source: Image(self.gauge_img_source)
	    do_scale: True

    canvas:
        PopMatrix

''')

class Gauge(Widget):
    """Class for creating a Gauge widget."""

    min = NumericProperty(0)
    '''Minimum value for value :attr:`value`.
    :attr:`min` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 0.
    '''

    max = NumericProperty(100)
    '''Maximum value for value :attr:`value`.
    :attr:`max` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 100.
    '''

    range = ReferenceListProperty(min, max)
    ''' Range of the values for Gauge.
    :attr:`range` is a :class:`~kivy.properties.ReferenceListProperty` of
    (:attr:`min`, :attr:`max`).
    '''

    value = NumericProperty(0)
    '''Current value of the Gauge. Set :attr:`value` when creating a Gauge to
    set its initial position. An internal :attr:`_angle` is calculated to set
    the position of the Gauge.
    :attr:`value` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 0.
    '''

    step = BoundedNumericProperty(1, min=0)
    '''Step interval of Gauge to go from min to max. An internal
    :attr:`_angle_step` is calculated to set Gauge step in degrees.
    :attr:`step` is a :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to 1 (min=0).
    '''

    curve = BoundedNumericProperty(1, min=1)
    '''This parameter determines the shape of the map function. It represent the
    reciprocal of a power function's exponent used to map the input value.
    So, for higher values of curve the contol is more reactive, and conversely.
    '''

    gauge_img_source = StringProperty("")
    '''Path of texture image that visually represents the Gauge. Use PNG for
    transparency support. The texture is rendered on a centered rectangle of
    size = :attr:`size` * :attr:`Gaugeimg_size`.
    :attr:`gauge_img_source` is a :class:`~kivy.properties.StringProperty`
    and defaults to empty string.
    '''

     gauge_type = StringProperty(" ")
    '''Type of gauge desired. Types included are 'Full' (meaning 360 deg), '3/4' (270 degrees) or 'half' (180 deg).
    :attr:`gauge_type` is a :class:`~kivy.properties.StringProperty`
    and defaults to empty string.
    '''

  

    _angle          = NumericProperty(0)            # Internal angle calculated from value.
    _angle_step     = NumericProperty(0)            # Internal angle_step calculated from step.

    def __init__(self, *args, **kwargs):
        super(Gauge, self).__init__(*args, **kwargs)
        self.bind(show_marker   =   self._show_marker)
        self.bind(value         =   self._value)

    def _value(self, instance, value):
        self._angle     =   pow( (value - self.min)/(self.max - self.min), 1./self.curve) * 360.
        self.on_Gauge(value)

    def _show_marker(self, instance, flag):
        # "show/hide" marker.
        if flag:
            self.Gaugeimg_bgcolor[3] = 1
            self.marker_color[3] = 1
            self.markeroff_color[3] = 1
        else:
            self.Gaugeimg_bgcolor[3] = 0
            self.marker_color[3] = 0
            self.markeroff_color[3] = 0



    def update_angle(self, touch):
        posx, posy          =   touch.pos
        cx, cy              =   self.center
        rx, ry              =   posx - cx, posy - cy

        if ry >= 0:                                 # Quadrants are clockwise.
            quadrant = 1 if rx >= 0 else 4
        else:
            quadrant = 3 if rx <= 0 else 2

        try:
            angle    = math.atan(rx / ry) * (180./math.pi)
            if quadrant == 2 or quadrant == 3:
                angle = 180 + angle
            elif quadrant == 4:
                angle = 360 + angle

        except:                                   # atan not def for angle 90 and 270
            angle = 90 if quadrant <= 2 else 270

        self._angle_step    =   (self.step*360)/(self.max - self.min)
        self._angle         =   self._angle_step
        while self._angle < angle:
            self._angle     =   self._angle + self._angle_step

        relativeValue   =   pow((angle/360.), 1./self.curve)
        self.value      =   (relativeValue * (self.max - self.min)) + self.min


    #TO OVERRIDE
    def on_Gauge(self, value):
        pass #Gauge values listener

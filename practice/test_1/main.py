from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch


from kivy.properties import ListProperty, ObjectProperty

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color

import random

class NuclearControlPanel(BoxLayout):

	def __init__(self, **kwargs):
		super(NuclearControlPanel, self).__init__(**kwargs)


    
class NuclearApp(App):
	def build(self):
		return NuclearControlPanel()

if __name__ == "__main__":
	NuclearApp().run()

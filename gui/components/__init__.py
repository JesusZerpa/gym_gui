from pygame_gui.elements import UITextBox as _UITextBox 
from pygame_gui.elements import UITextEntryBox as _UITextEntryBox 
from pygame_gui.elements import UITextEntryLine as _UITextEntryLine 
from pygame_gui.core import ObjectID
from pygame_gui.elements.ui_panel import UIPanel as _UIPanel
from pygame_gui.elements.ui_window import UIWindow as _UIWindow 
from pygame_gui.elements.ui_image import UIImage as _UIImage
from pygame_gui.elements import UIButton as _UIButton
from pygame_gui.core import IncrementalThreadedResourceLoader as _IncrementalThreadedResourceLoader
from pygame_gui.elements import UIButton as _UIButton, UIImage as _UIImage
from pygame_gui.windows import UIFileDialog as _UIFileDialog
from pygame_gui.core.utility import create_resource_path
from pygame_gui.windows import UIColourPickerDialog as _UIColourPickerDialog
from pygame_gui import UIManager
import variables,pygame

class GUI:
	def __init__(self,width=100,height=100,top=0,left=0,right=None,bottom=None,
		manager=None,container=None,object_id=None):
		print("uuuuu",container.__class__)
		self.container=container
		if variables.COMPONENT and isinstance(variables.COMPONENT,UIManager):
			self.container=variables.COMPONENT
			rect=variables.COMPONENT.get_root_container().rect
			print("XXXXX",rect)
		elif variables.COMPONENT:
			print("oooooo",variables.COMPONENT.__class__)
			variables.COMPONENT.add_widget(self)
			rect=variables.COMPONENT.rect

		variables.COMPONENT_BEFORE=variables.COMPONENT
		variables.COMPONENT=self

		if type(height)==str and "-" in height:
			p1,p2=height.split("-")
			p1,p2=p1.strip(),p2.strip()

			p1=int(p1.replace("%",""))/100
			height=int(p1*rect.height-int(p2))

		if type(width)==str and "-" in width:
			p1,p2=width.split("-")
			p1,p2=p1.strip(),p2.strip()
			p1=int(p1.replace("%",""))/100
			width=int(p1*rect.width-int(p2))

		if type(width)==str and "%" in width:
			p=int(width.replace("%",""))/100
			width=int(p*rect.width)

		if type(height)==str and "%" in height:
			print("fff ",height)
			p=int(height.replace("%",""))/100
			height=int(p*rect.height)

		
		
		

		
		print("rrrr", (top,left),(width,height))
		self._rect=pygame.Rect((top,left),(width,height))
			

		
		if right!=None and bottom!=None:
			self.rect.bottomright=(bottom,right)
		if not manager:
			self.manager=variables.MANAGER
		self.children=[]
		

	def __enter__(self):
		variables.COMPONENT=self
		return self

	def __exit__(self,type, value, traceback):
		variables.COMPONENT=variables.COMPONENT_BEFORE

	def add_widget(self,component):
		component.container=self
		self.children.append(component)

	def update(self,timedelta):
		for child in self.children: 
			child.update(timedelta)

	def __call__(self,method):
		"""
		Decorador para metodos el componente
		"""

class UIWindow(_UIWindow,GUI):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,object_id=None):

		GUI.__init__(self,width,height,top,left,
		right,bottom,manager,object_id=object_id)

		_UIWindow.__init__(self,self.rect,manager=manager)

class UITextBox(GUI,_UITextBox):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,object_id=None):

		GUI.__init__(self,width,height,top,left,
		right,bottom,manager,object_id=object_id)
		_UITextBox.__init__(self.rect,manager=manager)


class UITextEntryBox(GUI,_UITextEntryBox):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,object_id=None):
		GUI.__init__(self,width,height,top,left,
			right,bottom,manager,object_id=object_id)
		_UITextEntryBox.__init__(self.rect,manager=manager)
		

class UITextEntryLine(GUI,_UITextEntryLine):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,object_id=None):
		GUI.__init__(self,width,height,top,left,
			right,bottom,manager,object_id=object_id)
		_UITextEntryLine.__init__(self.rect,manager=manager)
		

class UIPanel(GUI,_UIPanel):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,container=variables.COMPONENT,object_id=None):
		
		GUI.__init__(self,width,height,top,left,
			right,bottom,manager,object_id=object_id,container=container)
		print("sssss",container.__class__,variables.COMPONENT.__class__)
		_UIPanel.__init__(self,self.rect,
			container=container,manager=manager)

class UIButton(GUI,_UIButton):
	def __init__(self,
		width=100,height=100,top=0,left=0,
		right=None,bottom=None,manager=variables.MANAGER,object_id=None):
		GUI.__init__(self,width,height,top,left,
			right,bottom,manager,object_id=object_id)
		_UIButton.__init__(self,self.rect,container=container,manager=manager)
		
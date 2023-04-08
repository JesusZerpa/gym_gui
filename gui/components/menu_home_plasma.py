from pygame_gui import UIManager, PackageResource
from components import UIPanel
from components import UIWindow
from components import UIButton
from components import UITextEntryBox
from components import UITextEntryLine
#from components import UIHorizontalSlider

import pygame
from utils import position
import variables
from components import  GUI
class PanelLeft(UIPanel):
    def __init__(self,width="50%",height="100%",top=0,left=0,
        right=None,bottom=None,container=None,manager=variables.MANAGER,object_id="#panel_left"):
        if not container:
            container=variables.COMPONENT
        super(PanelLeft,self).__init__(
            width,height,top,left,
            right,bottom,manager=manager,container=container,object_id=object_id)


        #self.set_visual_debug_mode(True)


    




class PanelRight(UIPanel):
    def __init__(self,width="50%",height="100%",top=0,left=0,
        right=None,bottom=None,container=None,manager=variables.MANAGER,
        object_id="#panel_right"):
   
        super(PanelRight,self).__init__(
            width,height,top,left,
            right,bottom,container=container,manager=manager,object_id=object_id)
        self.background_colour="#ffffff"
        



class UIMenu(UIWindow):
    def __init__(self,width=100,height=100,top=0,left=0,right=None,bottom=None,manager=variables.MANAGER):
        super(UIMenu,self).__init__(width,height,top,left,right,bottom,manager)
        
        with PanelLeft(
            width="50%",
            height="100% - 30",
            ) as w1:

            pass
        



        #self.panel_right=PanelRight(self)
        rect=pygame.Rect((0,self.rect.y-50),(100,30))
        """
        position(rect,self.rect)
        with UITextEntryLine(
                initial_text="",
                relative_rect=rect,
                manager=self.ui_manager,
                container=self.panel_left,
                object_id="#search"
                ) as st:
            with otro(
                initial_text="",
                relative_rect=rect,
                manager=self.ui_manager,
                container=self.panel_left,
                object_id="#search"
                ) as st2:


        self.add(
            UITextEntryLine(
                initial_text="",
                relative_rect=rect,
                manager=self.ui_manager,
                container=self.panel_left,
                object_id="#search"
                )
            )
        """
        #self.panel_right.background_colour="#ffffff"
        
        """
        UIButton(pygame.Rect((0,0),(100,30)),
            text="Hola mundo",container=self)
        """
    def update(self,timedelta):
        super().update(timedelta)
        self.image.fill([0,0,255,255])
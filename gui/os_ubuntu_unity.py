from collections import deque

from pygame_gui import UIManager, PackageResource
from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UIScreenSpaceHealthBar
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIImage
from pygame_gui.elements import UIPanel
from pygame_gui.elements import UISelectionList
from pygame_gui.windows import UIMessageWindow
import pygame, pygame_gui
from components.menu_home_plasma import UIMenu

class Options:
    def __init__(self):
        self.width=800
        self.height=600
        self.resolution = (self.width, self.height)
        self.fullscreen = False


class OptionsUIApp:
    def __init__(self):
        import variables

        pygame.init()
        pygame.display.set_caption("Options UI")
        self.options = Options()
        if self.options.fullscreen:
            self.window_surface = pygame.display.set_mode(self.options.resolution,
                                                          pygame.FULLSCREEN)
        else:
            self.window_surface = pygame.display.set_mode(self.options.resolution)

        self.ui_manager = UIManager(self.options.resolution,
                                    PackageResource(package='data.themes',
                                                    resource='custom.json'))
        self.ui_manager.preload_fonts([{'name': 'fira_code', 'point_size': 10, 'style': 'bold'},
                                       {'name': 'fira_code', 'point_size': 10, 'style': 'regular'},
                                       {'name': 'fira_code', 'point_size': 10, 'style': 'italic'},
                                       {'name': 'fira_code', 'point_size': 14, 'style': 'italic'},
                                       {'name': 'fira_code', 'point_size': 14, 'style': 'bold'}
                                       ])
        variables.MANAGER=self.ui_manager

        self.background_surface = None
        self.test_button = None
        self.test_button_2 = None
        self.test_button_3 = None
        self.test_slider = None
        self.test_text_entry = None
        self.test_drop_down = None
        self.test_drop_down_2 = None
        self.panel = None
        self.fps_counter = None
        self.frame_timer = None
        self.disable_toggle = None
        self.hide_toggle = None
        self.menu=None

        self.message_window = None

        self.recreate_ui()

        self.clock = pygame.time.Clock()
        self.time_delta_stack = deque([])

        self.button_response_timer = pygame.time.Clock()
        self.running = True
        self.debug_mode = False

        self.all_enabled = True
        self.all_shown = True
    def recreate_ui(self):
        import variables
        variables.COMPONENT=self.ui_manager
        self.ui_manager.set_window_resolution(self.options.resolution)
        self.ui_manager.clear_and_reset()
        self.background_surface = pygame.Surface(self.options.resolution)

        self.background_surface.fill(
            self.ui_manager.get_theme().get_colour('normal_bg'))
        
        rect=pygame.Rect((0, 0), (self.options.width, 50))#x,y , width,height
        rect.bottomright = (0, 0)
        self.ui_manager.get_theme().get_colour
        self.panel=UIPanel(
            rect,
            manager=self.ui_manager,
            object_id="#panel",
            anchors={'right': 'right',
                   'bottom': 'bottom'}
            )

        rect=pygame.Rect((0, 0), (50, 50))#x,y , width,height
        self.home_btn=UIButton(rect,
            text="Hola que tal",
            container=self.panel)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.ui_manager.process_events(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.debug_mode = False if self.debug_mode else True
                self.ui_manager.set_visual_debug_mode(self.debug_mode)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                print("self.ui_manager.focused_set:", self.ui_manager.focused_set)

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):
                print(event.text)

            if event.type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED:
                if event.link_target == 'test':
                    print("clicked test link")
                elif event.link_target == 'actually_link':
                    print("clicked actually link")

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.test_button:
                    self.test_button.set_text(random.choice(['', 'Hover me!',
                                                             'Click this',
                                                             'A Button']))
                    self.create_message_window()
                if event.ui_element==self.home_btn:
                    print("oooo",self.options.height-20)
                    rect=pygame.Rect(
                        (0,0), (224, 300)
                        )
                    #rect.top=self.options.height-350
                    rect.bottomright=[0,0]

                    self.menu=UIMenu( 
                        width=224,height=300,
                        manager=self.ui_manager,
                       
                    )

                    
                    #self.menu._window_root_container=self.ui_manager.root_container


                if event.ui_element == self.test_button_3:
                    ScalingWindow(pygame.Rect((50, 50), (224, 224)), self.ui_manager)
                if event.ui_element == self.test_button_2:
                    EverythingWindow(pygame.Rect((10, 10), (640, 480)), self.ui_manager)

                if event.ui_element == self.disable_toggle:
                    if self.all_enabled:
                        self.disable_toggle.set_text('Enable')
                        self.all_enabled = False
                        self.ui_manager.root_container.disable()
                        self.disable_toggle.enable()
                        self.hide_toggle.enable()
                    else:
                        self.disable_toggle.set_text('Disable')
                        self.all_enabled = True
                        self.ui_manager.root_container.enable()

                if event.ui_element == self.hide_toggle:
                    if self.all_shown:
                        self.hide_toggle.set_text('Show')
                        self.all_shown = False
                        self.ui_manager.root_container.hide()
                        self.hide_toggle.show()
                    else:
                        self.hide_toggle.set_text('Hide')
                        self.all_shown = True
                        self.ui_manager.root_container.show()

            if (event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                    and event.ui_element == self.test_drop_down):
                self.check_resolution_changed()

    def run(self):
        while self.running:
            time_delta = self.clock.tick() / 1000.0
            self.time_delta_stack.append(time_delta)
            if len(self.time_delta_stack) > 2000:
                self.time_delta_stack.popleft()

            # check for input
            self.process_events()

            # respond to input
            self.ui_manager.update(time_delta)
            if self.menu:
                self.menu.update(time_delta)

            if len(self.time_delta_stack) == 2000:
                """
                self.fps_counter.set_text(
                    f'FPS: {min(999.0, 1.0/max(sum(self.time_delta_stack)/2000.0, 0.0000001)):.2f}')
                self.frame_timer.set_text(f'frame_time: {sum(self.time_delta_stack)/2000.0:.4f}')
                """
            # draw graphics
            self.window_surface.blit(self.background_surface, (0, 0))

            # Debug crap
            # chunk = self.test_slider.right_button.drawable_shape.text_box_layout.layout_rows[0].items[0]
            # pygame.draw.line(self.test_slider.right_button.image,
            #                  pygame.Color('#FFFFFF'),
            #                  self.test_slider.right_button.drawable_shape.text_box_layout.layout_rows[0].midleft,
            #                  self.test_slider.right_button.drawable_shape.text_box_layout.layout_rows[0].midright,#chunk.centering_rect,
            #                  1)

            self.ui_manager.draw_ui(self.window_surface)

            pygame.display.update()

if __name__ == '__main__':
    app = OptionsUIApp()
    app.run()
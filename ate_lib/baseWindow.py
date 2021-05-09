import maya.cmds as mc


class BaseWindow(object):

    WINDOW_NAME = "Base_Window"
    WINDOW_TITLE = "Base Window"
    WIDTH = 360
    HEIGHT = 240


    def __init__(self):
        """ """
        self.CreateUI()

    def CreateUI(self):
        """ """
        if mc.window(self.WINDOW_NAME, exists = True):
            mc.deleteUI(self.WINDOW_NAME)

        # Window
        self.window = mc.window (self.WINDOW_NAME , 
                                title = self.WINDOW_TITLE, 
                                width = self.WIDTH, 
                                height = self.HEIGHT,
                                sizeable = False, 
                                minimizeButton = False, 
                                maximizeButton = False)

        mc.window(self.window, edit = True, w = self.WIDTH, h = self.HEIGHT)

        self.mainLayout = mc.columnLayout('mainLayout', width = self.WIDTH)

        self.CreateCustomUI()

        mc.showWindow(self.window)

    def CreateCustomUI(self):
        """ """
        print ('BaseWindow.CreateCustomUI override this fuction in child classes'),

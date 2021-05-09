from package.ate_lib.paths import Paths
from package.ate_lib.baseWindow import BaseWindow
from package.ate_gs.lampostPanel.bbox import BboxInfo, MeshInfo, TexInfo
from functools import partial
import maya.cmds as mc
import csv
import os

class Lamp_Posts_Window(BaseWindow):

    WINDOW_NAME = "Lampost_Selector_Panel"
    WINDOW_TITLE = "LAMPOST selector panel"
    WIDTH = 720 + 20
    COLUMN_WIDTH = 360
    HEIGHT = 395
    INDEX = 0
    PATH = Paths.database
    MODEL_DEPOT = Paths.MODEL_DEPOT
    LAMP_POST_LIST = os.listdir(Paths.database)
    LIGHTS = Paths.MODEL_WORK

    BBOX = BboxInfo()
    xBBOX_LIST = BBOX.axisX_list()
    yBBOX_LIST = BBOX.axisY_list()
    zBBOX_LIST = BBOX.axisZ_list()

    MESH = MeshInfo()
    VERTEX = MESH.vertex()
    TRIS = MESH.tris()

    TEX = TexInfo()
    TEX_RES = TEX.resolution()

    def prev_img (self, index):
        if self.INDEX == 0:
            self.INDEX = len(self.LAMP_POST_LIST) - 1
        else:
            self.INDEX = self.INDEX - 1
        
        previous = self.LAMP_POST_LIST[self.INDEX]
        mc.frameLayout(self.lampost_name, edit = True, label = previous)
        mc.image(self.lampost_snap, edit = True, image = Paths.SNAPSHOTS_WEB +  previous + '.jpg')  
        mc.text(self.airportfeatures_path, edit = True, label='Path: ../../AIRPORT_FEATURES/' + previous)
        mc.text(self.axisX_label, edit = True, label='X: ' + self.xBBOX_LIST[self.INDEX] + 'm')
        mc.text(self.axisY_label, edit = True, label='Y: ' + self.yBBOX_LIST[self.INDEX]  + 'm')
        mc.text(self.axisZ_label, edit = True, label='Z: ' + self.zBBOX_LIST[self.INDEX]  + 'm')
        mc.text(self.vertex_label, edit = True, label = 'Vertex: ' + str(self.VERTEX[self.INDEX]))
        mc.text(self.tris_label, edit = True, label = 'Tris: ' + str(self.TRIS[self.INDEX]))
        mc.text(self.texture_label, edit = True, label = 'Texture: ' + self.TEX_RES[self.INDEX])


        if len(self.testlist) == 0:
            self.hie(self.LAMP_POST_LIST[self.INDEX])

        else:
            mc.deleteUI(self.layout_hie_version, layout = True)
            self.layout_hie_version = mc.columnLayout('layout_hie_version', width = self.COLUMN_WIDTH - 16, parent = 'scrollLayout_hie')
            self.hie(self.LAMP_POST_LIST[self.INDEX])

        return previous

    def next_img (self, index):
        if self.INDEX == len(self.LAMP_POST_LIST) - 1:
            self.INDEX = 0
        else:
            self.INDEX = self.INDEX + 1
        
        next = self.LAMP_POST_LIST[self.INDEX]
        mc.frameLayout(self.lampost_name, edit = True, label = next)
        mc.image(self.lampost_snap, edit = True, image = Paths.SNAPSHOTS_WEB +  next + '.jpg')  
        mc.text(self.airportfeatures_path, edit = True, label='Path: ../../AIRPORT_FEATURES/' + next)
        mc.text(self.axisX_label, edit = True, label='X: ' + self.xBBOX_LIST[self.INDEX] + 'm')
        mc.text(self.axisY_label, edit = True, label='Y: ' + self.yBBOX_LIST[self.INDEX]  + 'm')
        mc.text(self.axisZ_label, edit = True, label='Z: ' + self.zBBOX_LIST[self.INDEX]  + 'm')
        mc.text(self.vertex_label, edit = True, label = 'Vertex: ' + str(self.VERTEX[self.INDEX]))
        mc.text(self.tris_label, edit = True, label = 'Tris: ' + str(self.TRIS[self.INDEX]))
        mc.text(self.texture_label, edit = True, label = 'Texture: ' + self.TEX_RES[self.INDEX])


        if len(self.testlist) == 0:
            self.hie(self.LAMP_POST_LIST[self.INDEX])

        else:
            mc.deleteUI(self.layout_hie_version, layout = True)
            self.layout_hie_version = mc.columnLayout('layout_hie_version', width = self.COLUMN_WIDTH - 16, parent = 'scrollLayout_hie')
            self.hie(self.LAMP_POST_LIST[self.INDEX])

        return next

    def lampostList_buttons_menu (self, lamposts):
        for lampost in lamposts:
            self.lampost_button = mc.menuItem(label = lampost)

        return self.lampost_button

    def lampostList_selection(self, lampost_selected):
        print(lampost_selected)
        if lampost_selected in self.LAMP_POST_LIST:
            self.INDEX = self.LAMP_POST_LIST.index(lampost_selected)

            mc.frameLayout(self.lampost_name, edit = True, label = self.LAMP_POST_LIST[self.INDEX])
            mc.image(self.lampost_snap, edit = True, image = Paths.SNAPSHOTS_WEB + self.LAMP_POST_LIST[self.INDEX] + '.jpg')  
            mc.text(self.airportfeatures_path, edit = True, label='Path: ../../AIRPORT_FEATURES/' + self.LAMP_POST_LIST[self.INDEX])
            mc.text(self.axisX_label, edit = True, label='X: ' + self.xBBOX_LIST[self.INDEX] + 'm')
            mc.text(self.axisY_label, edit = True, label='Y: ' + self.yBBOX_LIST[self.INDEX]  + 'm')
            mc.text(self.axisZ_label, edit = True, label='Z: ' + self.zBBOX_LIST[self.INDEX]  + 'm')
            mc.text(self.vertex_label, edit = True, label = 'Vertex: ' + str(self.VERTEX[self.INDEX]))
            mc.text(self.tris_label, edit = True, label = 'Tris: ' + str(self.TRIS[self.INDEX]))
            mc.text(self.texture_label, edit = True, label = 'Texture: ' + self.TEX_RES[self.INDEX])

        if len(self.testlist) == 0:
            self.hie(self.LAMP_POST_LIST[self.INDEX])

        else:
            mc.deleteUI(self.layout_hie_version, layout = True)
            self.layout_hie_version = mc.columnLayout('layout_hie_version', width = self.COLUMN_WIDTH - 16, parent = 'scrollLayout_hie')
            self.hie(self.LAMP_POST_LIST[self.INDEX])

    def hie(self, lampost):

        lampost_folder = self.PATH + lampost + '/'
        lampost_folder_files = os.listdir(lampost_folder)

        self.testlist = []
        for file in lampost_folder_files:
            extension = file[-4:]

            if extension == '.hie':
                self.testlist.append(file)

        for hie in self.testlist:
            self.hie_version_checkBox = mc.checkBox(label = hie, parent = 'layout_hie_version')

    def import_lampost(self, index):
        self.import_lampost = mc.file(self.MODEL_DEPOT + self.LAMP_POST_LIST[self.INDEX] + '/GEO/' + self.LAMP_POST_LIST[self.INDEX] + '_lod1.obj', 
                                    i = True,
                                    defaultNamespace = False,
                                    type = 'OBJ')

        if self.option_group == True:
            self.createGroup(self.LAMP_POST_LIST[self.INDEX])

        selection = mc.ls('Mesh')
        mc.parent(selection,self.group)
        mc.rename(selection, self.LAMP_POST_LIST[self.INDEX])

        self.applyMaterial((self.LAMP_POST_LIST[self.INDEX]))

        mc.checkBox(self.option_group, edit = True, value = False)

    def applyMaterial(self,lamposts):

        if mc.objExists(lamposts):

            fileimage = self.MODEL_DEPOT + lamposts + '/TEX/' + lamposts + '.rgb'
            
            MAT  =  mc.shadingNode('lambert', name = "MAT_" + lamposts, asShader = True)
            
            GS  =  mc.sets(name = 'GS_' + MAT[4:], empty = True, renderable = True, noSurfaceShader = True)
            mc.connectAttr(MAT + '.outColor', GS + '.surfaceShader')
            mc.sets(lamposts, e = True, forceElement = GS)
            
            TEX = mc.shadingNode('file', name='TEX_' + lamposts, asTexture=True)
            mc.connectAttr(TEX + '.outColor', MAT +'.color', force=True)
            mc.setAttr(TEX + '.fileTextureName' ,fileimage,  type = 'string')
            
    def createGroup(self,lamposts):
        self.group = mc.group(name = self.LAMP_POST_LIST[self.INDEX] + '_001', empty = lamposts, world = True)

    def omnilights_buttons_menu (self):
        mc.menuItem(label = '< Select Ominlight >')
        lights_folder = os.listdir(self.LIGHTS)

        for omni in lights_folder:
            if omni.endswith('.mb'):
                if omni.startswith('OMNILIGHT'):
                    self.omnilights_button = mc.menuItem(label = omni[:-3])
        
        return self.omnilights_button

    def spotlights_buttons_menu (self):
        mc.menuItem(label = '< Select Spotlight >')
        lights_folder = os.listdir(self.LIGHTS)

        for spot in lights_folder:
            if spot.endswith('.mb'):
                if spot.startswith('SPOTLIGHT'):
                    self.spotlight_button = mc.menuItem(label = spot[:-3])
        
        return self.spotlight_button

    def test_omni(self, omni_selected):
        print(omni_selected)
    def test_spot(self, spot_selected):
        print(spot_selected)


    def toggleOmniLightsMenuEnable(self, index):
        if mc.optionMenu(self.omnilights_optionMenu, query = True, enable = False):
            mc.optionMenu(self.omnilights_optionMenu, edit = True, enable = False)
        else:
            mc.optionMenu(self.omnilights_optionMenu, edit = True, enable = True)

    def toggleSpotLightsMenuEnable(self, index):
        if mc.optionMenu(self.spotlights_optionMenu, query = True, enable = False):
            mc.optionMenu(self.spotlights_optionMenu, edit = True, enable = False)
        else:
            mc.optionMenu(self.spotlights_optionMenu, edit = True, enable = True)



    def CreateCustomUI (self):
        """ """
        

        mc.rowLayout('main_row_layout', numberOfColumns = 3, parent = self.mainLayout, width = self.WIDTH)

        #! column_left --------------------------------------------------------------------

        mc.columnLayout('column_left', parent = 'main_row_layout', w = self.COLUMN_WIDTH, h = self.HEIGHT)


        self.lampost_name = mc.frameLayout('frame_name_lampost_layout', label = self.LAMP_POST_LIST[self.INDEX], w = self.COLUMN_WIDTH , parent = 'column_left')
        mc.separator(style = 'out', w = self.COLUMN_WIDTH, parent = 'frame_name_lampost_layout')


        self.lampost_snap = mc.image('snapshot', image = Paths.SNAPSHOTS_WEB +  self.LAMP_POST_LIST[self.INDEX] + '.jpg', w = self.WIDTH, parent = 'column_left')

        mc.rowLayout('select_buttons', numberOfColumns = 2, parent = 'column_left')
        self.previous_button = mc.button('Previous', label = '<- Previous', parent = 'select_buttons', w = self.COLUMN_WIDTH//2 - 1, height = 30, exists = False, 
                                        command = self.prev_img)
        self.next_button = mc.button('Next', label = 'Next ->', parent = 'select_buttons', w = self.COLUMN_WIDTH//2 - 1, height = 30, exists = False,
                                        command = self.next_img)

        mc.separator(style = 'out', w = self.COLUMN_WIDTH, parent = 'column_left')
        
        mc.frameLayout('list_lampost_menu', label = 'LAMP POSTS LIST', w = self.COLUMN_WIDTH , parent = 'column_left')
        self.lampostList_optionMenu = mc.optionMenu(label = '  LAMP POST: ', w = self.COLUMN_WIDTH , parent = 'list_lampost_menu', changeCommand = self.lampostList_selection)
        self.lampostList_buttons_menu(self.LAMP_POST_LIST)

        #! column_center --------------------------------------------------------------------
        mc.columnLayout('column_center', parent = 'main_row_layout', w = 10)

        #! column_right --------------------------------------------------------------------

        mc.columnLayout('column_right', parent = 'main_row_layout', w = self.COLUMN_WIDTH, h = self.HEIGHT)
        mc.frameLayout('properties', label = 'PROPERTIES', w = self.COLUMN_WIDTH, h = 120, parent = 'column_right', cll = False)
        mc.separator(style = 'out', w = self.COLUMN_WIDTH, parent = 'properties')
        self.airportfeatures_path = mc.text( 'airportfeatures_path', label='Path: ../../AIRPORT_FEATURES/' + self.LAMP_POST_LIST[self.INDEX], parent = 'properties', al = 'left' )
        mc.rowLayout('properties_row_id', parent = 'properties', numberOfColumns = 4, w = self.COLUMN_WIDTH//2)
        mc.columnLayout('properties_column_left_id', parent = 'properties_row_id', w = self.COLUMN_WIDTH//2)
        mc.columnLayout('properties_column_right_id', parent = 'properties_row_id', w = self.COLUMN_WIDTH//2)
        self.tris_label = mc.text( label='Tris: ' + str(self.TRIS[self.INDEX]), parent = 'properties_column_left_id', al = 'left', h = 15 )
        self.vertex_label = mc.text( label='Vertex: ' + str(self.VERTEX[self.INDEX]), parent = 'properties_column_left_id', al = 'left', h = 15 )
        self.texture_label = mc.text( label='Texture: ' + self.TEX_RES[self.INDEX], parent = 'properties_column_left_id', al = 'left', h = 15 )
        self.axisX_label = mc.text( label='X: ' + self.xBBOX_LIST[self.INDEX] + 'm', parent = 'properties_column_right_id', al = 'left', h = 15 )
        self.axisY_label = mc.text( label='Y: ' + self.yBBOX_LIST[self.INDEX]  + 'm', parent = 'properties_column_right_id', al = 'left', h = 15 )
        self.axisZ_label = mc.text( label='Z: ' + self.zBBOX_LIST[self.INDEX]  + 'm', parent = 'properties_column_right_id', al = 'left', h = 15 )
        mc.text( label='', parent = 'properties', al = 'left' )



        mc.frameLayout('import_version', label = 'IMPORT VERSION', w = self.COLUMN_WIDTH, parent = 'column_right', cll = False, h = 88)
        mc.separator(style = 'out', w = self.COLUMN_WIDTH, parent = 'import_version')
        mc.scrollLayout('scrollLayout_hie', width = self.COLUMN_WIDTH, parent = 'import_version')
        self.layout_hie_version = mc.columnLayout('layout_hie_version', width = self.COLUMN_WIDTH - 16, parent = 'scrollLayout_hie')
        
        self.hie(self.LAMP_POST_LIST[self.INDEX])

        mc.text( label='', parent = 'import_version', al = 'left', h = 5 )



        mc.frameLayout('import_preferences', label = 'IMPORT PREFERENCES', w = self.COLUMN_WIDTH, parent = 'column_right', cll = False, cl = False, h = 140)
        mc.separator(style = 'out', w = self.COLUMN_WIDTH)
        
        mc.rowLayout('outliner_structure', numberOfColumns = 3, parent = 'import_preferences', w = self.COLUMN_WIDTH//3, h = 15)
        mc.text( label='Create Group: ', parent = 'outliner_structure', al = 'left', w = self.COLUMN_WIDTH//3 - 1 )
        self.option_group = mc.checkBox(label = 'Yes', parent = 'outliner_structure', w = self.COLUMN_WIDTH//3 - 1, changeCommand = self.createGroup)
        mc.checkBox(label = 'No', parent = 'outliner_structure', w = self.COLUMN_WIDTH//3 - 1)

        mc.rowLayout('texture_option', numberOfColumns = 3, parent = 'import_preferences', w = self.COLUMN_WIDTH//3, h = 15)
        mc.text( label='Texture: ', parent = 'texture_option', al = 'left', w = self.COLUMN_WIDTH//3 - 1 )
        mc.checkBox(label = 'Yes', parent = 'texture_option', w = self.COLUMN_WIDTH//3 - 1, onCommand = self.applyMaterial)
        mc.checkBox(label = 'No', parent = 'texture_option', w = self.COLUMN_WIDTH//3 - 1)

        mc.rowLayout('import_omnilight_light', numberOfColumns = 3, parent = 'import_preferences', w = self.COLUMN_WIDTH//3, h = 15)
        self.checkOmnilight = mc.checkBox(label = 'Omnilight              ', parent = 'import_omnilight_light', onc = self.toggleOmniLightsMenuEnable, ofc=self.toggleOmniLightsMenuEnable)
        self.omnilights_optionMenu = mc.optionMenu(w = self.COLUMN_WIDTH//2 + 55 , parent = 'import_omnilight_light', enable = False, changeCommand = self.test_omni)
        self.omnilights_buttons_menu()

        mc.rowLayout('import_spotlight_light', numberOfColumns = 3, parent = 'import_preferences', w = self.COLUMN_WIDTH//3, h = 15)
        self.checkSpotlight = mc.checkBox(label = 'Spotlight               ', parent = 'import_spotlight_light', onc = self.toggleSpotLightsMenuEnable, ofc=self.toggleSpotLightsMenuEnable)
        self.spotlights_optionMenu = mc.optionMenu(w = self.COLUMN_WIDTH//2 + 55, parent = 'import_spotlight_light', enable = False, changeCommand = self.test_spot)
        self.spotlights_buttons_menu()


        mc.text( label='', parent = 'import_preferences', al = 'left', h = 5 )
        mc.rowLayout('final_buttons', numberOfColumns = 2, parent = 'column_right', h = 52)
        button_clear = mc.button('Clear', label = 'Clear', parent = 'final_buttons', w = self.COLUMN_WIDTH//2 - 1, height = 30)
        button_import = mc.button('Import', label = 'Import', parent = 'final_buttons', w = self.COLUMN_WIDTH//2 - 1, height = 30, command = self.import_lampost)


panel = Lamp_Posts_Window()

















import maya.cmds as mc

def create_window():


    window_name = "AechelonUI_ATELights"
    window_title = "ATELights Info"
    window_w = 1056
    window_h = 828
    if mc.window(window_name, query = True, exists = True):
        mc.deleteUI(window_name)
    mc.window(window_name)
    mc.window(window_name, edit = True, title = window_title, w = window_w, h = window_h, minimizeButton = False, maximizeButton = False)

    mc.scrollLayout('main_layout', w = window_w, h = window_h, verticalScrollBarAlwaysVisible=False)
    create_customUI()
    mc.showWindow(window_name)

def create_customUI():
    
    mc.frameLayout('Light_Info_type', label = 'Light Info type', w = window_w, parent = 'main_layout')
    mc.separator(style = 'shelf')
    mc.frameLayout('OMNILIGHTS_info', label = 'OMNILIGHTS', w = window_w, parent = 'main_layout', collapse = True, collapsable = True)
    mc.separator(style = 'in')
    mc.image(image = 'D:/Scripts/DB/DB_DATA/LIGHTS/OMNILIGHTS_SCHEME_0.30.jpg', h = window_h, parent = 'OMNILIGHTS_info')
    mc.frameLayout('SPOTLIGHTS_info', label = 'SPOTLIGHTS', w = window_w, parent = 'main_layout', collapse = False, collapsable = True)
    mc.separator(style = 'in')
    mc.image(image = 'D:/Scripts/DB/DB_DATA/LIGHTS/SPOTLIGHTS_SCHEME_0.30.jpg', h = window_h, parent = 'SPOTLIGHTS_info')

create_window()
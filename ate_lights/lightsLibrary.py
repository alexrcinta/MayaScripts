import maya.cmds as mc

class LightsLibrary(object):

    self.LIGHT_NAME = LIGHT_NAME
    LIGHT_PATH = 'D:/Scripts/DB/DB_DATA/LIGHTS/'

    
    # IMPORT FILE

    mc.file(LIGHT_PATH + LIGHT_NAME + '.mb', 
            i = True, 
            type = 'mayaBinary', 
            ignoreVersion = True, 
            mergeNamespacesOnClash = False,
            options = 'v=0')

    # RENAME-IT!
    lights_group = mc.ls('LIGHTS')
    print(lights_group)
    mc.ls(None)
    mc.parent(LIGHT_NAME, 'LIGHTS')
    mc.rename(LIGHT_NAME, LIGHT_NAME + '_01')
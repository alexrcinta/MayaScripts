import maya.cmds as mc


class Lights():
    
    LIGHT_PATH = 'D:/Scripts/DB/DB_DATA/LIGHTS/'

    #### SPOTLIGHTS

    def SPOTLIGHT_ORANGE_10m(self):
        
        LIGHT_NAME = 'SPOTLIGHT_ORANGE_10m'
        
        mc.file(self.LIGHT_PATH + LIGHT_NAME + '.mb', i = True, type = 'mayaBinary', ignoreVersion = True, mergeNamespacesOnClash = False, options = 'v=0')
        mc.rename(LIGHT_NAME, LIGHT_NAME + '_001')
